#!/usr/bin/env python3
"""
halo_reddit_coder.py — Free, legal, ToS-compliant r/vadodara research coder.

WHAT THIS IS
------------
Reads PUBLIC r/vadodara threads via Reddit's OFFICIAL API (free tier,
app-only/read-only OAuth) and writes ONLY aggregate, anonymized codes to CSV.
It NEVER stores usernames, URLs, comment/post text, phone numbers, or any PII.

WHY IT'S FREE & LEGAL
---------------------
- Reddit's API free tier covers low-volume reads (well within limits for this).
- App-only OAuth (grant_type=client_credentials) = read public data, no login.
- We pace requests (sleep) and run at most every 6-12h, never hourly.
- We do NOT bypass any block or rate limit. If Reddit says no, we stop.

ONE-TIME SETUP (no money needed)
--------------------------------
1. Log in to Reddit (free account).
2. Go to https://www.reddit.com/prefs/apps  ->  "create another app...".
3. Choose type "script". Name it (e.g. "halo-vadodara-research").
   redirect uri: http://localhost:8080  (unused, but required).
4. After creating, copy the client id (under the app name) and the secret.
5. In your terminal:
       export REDDIT_CLIENT_ID="your_id"
       export REDDIT_CLIENT_SECRET="your_secret"
       export REDDIT_USER_AGENT="halo-research by u/your_username"
6. Run:  python3 halo_reddit_coder.py --limit 100 --with-comments

CADENCE
-------
Run once or twice a day (the script enforces a >=6h gap via a timestamp file).
Stop the whole study at saturation (new runs stop producing new codes).

OUTPUT (in ../instruments/)
---------------------------
Appends anonymized rows to pain-coding-sheet.csv, trust-coding-sheet.csv,
language-tone-log.csv. thread_id is an internal counter (R001...). No way to
map a row back to a Reddit post or person is stored.

DEPENDENCIES: Python 3.8+ standard library only (urllib). No pip install.
"""

import argparse
import csv
import os
import re
import sys
import time
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SUBREDDIT = "vadodara"
INSTRUMENTS = Path(__file__).resolve().parent.parent / "instruments"
STATE_FILE = Path(__file__).resolve().parent / ".coder_state.json"
MIN_HOURS_BETWEEN_RUNS = 6
REQUEST_PAUSE_SEC = 2.0  # human-pace; well under free-tier limits

# --------------------------------------------------------------------------
# PII GUARDS — these patterns are detected ONLY to (a) set boolean code flags
# and (b) ensure we never write them. The matched text is NEVER stored.
# --------------------------------------------------------------------------
PHONE_RE = re.compile(r"(?:\+?91[\-\s]?)?\b[6-9]\d{9}\b")
EMAIL_RE = re.compile(r"\b[\w.\-]+@[\w\-]+\.\w+\b")
URL_RE = re.compile(r"https?://\S+")

# --------------------------------------------------------------------------
# CATEGORY KEYWORDS  (C1..C12) — heuristic; verify a sample by hand.
# --------------------------------------------------------------------------
CATEGORY_KEYWORDS = {
    "C1": ["electrician", "plumber", "carpenter", "ac repair", "ac service",
           "pest control", "deep clean", "appliance", "ro service", "geyser"],
    "C2": ["contractor", "interior", "false ceiling", "painter", "painting",
           "fabrication", "renovation", "civil work", "tiles"],
    "C3": ["doctor", "dentist", "physio", "pediatric", "paediatric", "clinic",
           "diagnostic", "lab test", "elder care", "physiotherap", "hospital",
           "gym", "trainer", "dietician"],
    "C4": ["tutor", "tuition", "coaching", "classes", "teacher", "music class",
           "guitar", "language class", "ielts", "exam prep"],
    "C5": ["photographer", "photography", "decorator", "decoration", "caterer",
           "catering", "makeup", "mehndi", "dj", "tailor", "boutique"],
    "C6": ["tiffin", "mess", "home baker", "bakery", "cake", "homemade food",
           "khichdi", "thali"],
    "C7": ["mechanic", "garage", "car wash", "driver", "two wheeler", "bike service",
           "packers", "movers", "car service", "puncture"],
    "C8": ["chartered accountant", " ca ", "lawyer", "advocate", "architect",
           "web developer", "designer", "freelancer", "marketing", "gst"],
    "C9": ["vet", "veterinary", "pet groom", "gardener", "nursery", "plants",
           "dog", "cat"],
    "C10": ["where can i", "where to", "how do i", "passport", "rto", "license",
            "process", "office", "government", "documents"],
    "C11": ["flat", "rent", "pg ", "broker", "second hand", "resale", "for sale",
            "buy", "sell", "1bhk", "2bhk", "3bhk"],
}

INTENT_KEYWORDS = {
    "seek": ["suggest", "recommend", "anyone know", "looking for", "need a",
             "where can i", "best ", "good ", "trusted", "reliable"],
    "vent": ["worst", "cheated", "fraud", "scam", "overcharged", "avoid",
             "terrible", "horrible", "ripped off", "warning"],
    "info": ["how do i", "how to", "process", "is it possible", "what is the"],
    "offer": ["dm me", "i provide", "we offer", "contact me", "available for",
              "i do ", "services available"],
    "review": ["i used", "i tried", "my experience", "review of", "went to"],
}

PAIN_KEYWORDS = {
    "P1": ["can't find", "cant find", "unable to find", "no one", "nowhere"],
    "P2": ["too many", "which one", "confused", "how to choose", "ten names",
           "can't decide", "cant decide", "so many options"],
    "P3": ["reliable", "trustworthy", "will they show", "dependable", "show up"],
    "P4": ["overcharge", "price", "expensive", "rate", "cost", "charges",
           "quotation", "too much", "cheaper"],
    "P5": ["quality", "bad work", "poor work", "not good", "shoddy", "ruined"],
    "P6": ["doesn't pick", "not answering", "no response", "ghost", "didn't show",
           "didnt show", "no reply"],
    "P7": ["near me", "nearby", "too far", "my area", "distance", "far away"],
    "P8": ["language", "doesn't understand", "english", "hindi", "gujarati only"],
    "P9": ["specific", "specialist", "rare", "niche", "hard to find", "unusual"],
    "P10": ["urgent", "emergency", "asap", "immediately", "today", "right now"],
}

TS_KEYWORDS = {
    "TS1": ["anyone actually", "anyone used", "has anyone", "personally used",
            "real experience"],
    "TS2": ["reliable", "show up", "dependable", "on time", "complete the work"],
    "TS3": ["fair price", "reasonable", "transparent", "honest rate", "not overcharge"],
    "TS4": ["portfolio", "past work", "photos", "samples", "previous work"],
    "TS5": ["local", "trusted", "known", "from our area", "barodian"],
    "TS6": ["safe", "trust them in", "elderly", "kids", "alone at home", "hygien"],
}

# first-hand vouch language => TP1 (the high-trust signal)
TP1_KEYWORDS = ["i used", "i hired", "we got", "i tried", "personally", "my experience",
                "i go to", "we use", "been using", "i recommend"]
# self-promo => TP3
TP3_KEYWORDS = ["dm me", "contact me", "i provide", "we offer", "available for hire",
                "message me", "ping me"]


def load_credentials():
    """
    Beginner-friendly: read credentials from a simple text file
    `credentials.txt` next to this script, with three lines like:
        client_id=xxxxx
        client_secret=yyyyy
        user_agent=halo-research by u/yourname
    Falls back to environment variables if the file is absent.
    """
    cfg = {}
    cred_file = Path(__file__).resolve().parent / "credentials.txt"
    if cred_file.exists():
        for line in cred_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            cfg[k.strip().lower()] = v.strip()
    cid = cfg.get("client_id") or os.environ.get("REDDIT_CLIENT_ID")
    secret = cfg.get("client_secret") or os.environ.get("REDDIT_CLIENT_SECRET")
    ua = (cfg.get("user_agent") or os.environ.get("REDDIT_USER_AGENT")
          or "halo-vadodara-research/1.0")
    return cid, secret, ua


def get_token():
    cid, secret, ua = load_credentials()
    if not cid or not secret:
        sys.exit("ERROR: missing credentials.\n"
                 "Create a file named 'credentials.txt' in this folder with:\n"
                 "  client_id=YOUR_ID\n"
                 "  client_secret=YOUR_SECRET\n"
                 "  user_agent=halo-research by u/yourname\n"
                 "(See STEP-BY-STEP.md. It's free — no money needed.)")
    data = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode()
    auth = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    req = urllib.request.Request("https://www.reddit.com/api/v1/access_token",
                                 data=data, method="POST")
    creds = f"{cid}:{secret}".encode()
    import base64
    req.add_header("Authorization", "Basic " + base64.b64encode(creds).decode())
    req.add_header("User-Agent", ua)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            tok = json.load(r)["access_token"]
        return tok, ua
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR getting token ({e.code}). Check credentials. "
                 "Do NOT retry aggressively — respect rate limits.")


def api_get(path, token, ua, params=None):
    url = "https://oauth.reddit.com" + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url)
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("User-Agent", ua)
    time.sleep(REQUEST_PAUSE_SEC)  # human-pace
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 429:
            sys.exit("Rate limited (429). STOP — we never bypass limits. "
                     "Try again in a few hours.")
        raise


def match_codes(text, keyword_map):
    """Return list of codes whose keywords appear. Text is used in-memory only."""
    t = " " + text.lower() + " "
    hits = [code for code, kws in keyword_map.items() if any(k in t for k in kws)]
    return hits


def best_category(text):
    hits = match_codes(text, CATEGORY_KEYWORDS)
    return hits[0] if hits else "C12"


def first_or_blank(lst):
    return lst[0] if lst else ""


def detect_language(text):
    """Crude script/language detection. Pattern only — no text stored."""
    has_gujarati = bool(re.search(r"[઀-૿]", text))
    has_devanagari = bool(re.search(r"[ऀ-ॿ]", text))
    # romanized gujarati/hindi heuristic
    roman_local = any(w in text.lower() for w in
                      [" che ", " nathi ", " karvu", " joiye", " kya ", " apde",
                       " bhai", " yaar", " chho", " kaam", "halo"])
    if has_gujarati:
        script = "gujarati-script"
        mix = "guj-eng" if re.search(r"[a-zA-Z]", text) else "gujarati"
    elif has_devanagari:
        script = "devanagari"
        mix = "hin-eng" if re.search(r"[a-zA-Z]", text) else "hindi"
    elif roman_local:
        script = "roman"
        mix = "guj-eng"
    else:
        script = "roman"
        mix = "english"
    return mix, script


def detect_tone(text):
    t = text.lower()
    if any(w in t for w in ["urgent", "emergency", "asap", "immediately"]):
        return "urgent"
    if any(w in t for w in ["worst", "cheated", "fraud", "scam", "avoid", "angry"]):
        return "frustrated"
    if any(w in t for w in ["sorry", "please help", "any help"]):
        return "apologetic"
    if any(w in t for w in ["fellow", "guys", "friends", "apna", "our city"]):
        return "communal"
    return "casual"


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"next_id": 1, "last_run": None}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state))


def enforce_cadence(state, force):
    last = state.get("last_run")
    if last and not force:
        elapsed = (datetime.now(timezone.utc) -
                   datetime.fromisoformat(last)).total_seconds() / 3600
        if elapsed < MIN_HOURS_BETWEEN_RUNS:
            sys.exit(f"Last run was {elapsed:.1f}h ago. Min gap is "
                     f"{MIN_HOURS_BETWEEN_RUNS}h (no hourly scraping). "
                     "Use --force only if you truly mean to.")


def ensure_headers():
    """Create CSVs with headers if missing (does not overwrite existing data)."""
    files = {
        "pain-coding-sheet.csv": ["thread_id", "category", "intent", "pain_code",
            "search_effort", "specificity", "unmet_need_paraphrase",
            "got_usable_answer", "halo_relevance", "notes"],
        "trust-coding-sheet.csv": ["thread_id", "trust_signal_sought",
            "trust_proof_offered", "trust_breakdown", "trusted_source_type",
            "verification_gap_paraphrase"],
        "language-tone-log.csv": ["thread_id", "language_mix", "romanized_or_script",
            "emotion_language", "logistics_language", "local_vocab_paraphrase",
            "quality_words_paraphrase", "ask_tone", "ask_length", "formatting_habit"],
    }
    INSTRUMENTS.mkdir(parents=True, exist_ok=True)
    for name, header in files.items():
        p = INSTRUMENTS / name
        if not p.exists() or p.stat().st_size == 0:
            with p.open("w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(header)


def append_row(filename, row):
    with (INSTRUMENTS / filename).open("a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(row)


def code_thread(post, comments_text):
    """
    Derive codes from post + comments held IN MEMORY ONLY.
    Returns three dict rows. NOTHING identifying is returned or stored.
    """
    title = post.get("title", "") or ""
    body = post.get("selftext", "") or ""
    blob = f"{title}\n{body}\n{comments_text}"

    # PII presence flags (we store the FLAG, never the value)
    has_phone = bool(PHONE_RE.search(blob))
    has_contact_only = has_phone and not any(k in blob.lower() for k in TP1_KEYWORDS)

    category = best_category(title + " " + body)
    intent = first_or_blank(match_codes(blob, INTENT_KEYWORDS)) or "seek"
    pain = first_or_blank(match_codes(blob, PAIN_KEYWORDS))

    # specificity
    spec = "vague"
    if any(w in blob.lower() for w in ["near", "area", "alkapuri", "manjalpur",
            "gotri", "akota", "fatehgunj", "sayajigunj", "waghodia", "old padra"]):
        spec = "area"
    if PHONE_RE.sub("", blob) and any(w in blob.lower() for w in
            ["budget", "under ", "rs ", "₹", "rupees", "price range"]):
        spec = "budget"

    # trust signals
    ts = first_or_blank(match_codes(blob, TS_KEYWORDS))
    tp = ""
    if any(k in blob.lower() for k in TP1_KEYWORDS):
        tp = "TP1"
    elif any(k in blob.lower() for k in TP3_KEYWORDS):
        tp = "TP3"
    elif has_phone:
        tp = "TP2"
    tb = ""
    if has_contact_only:
        tb = "TB1"
    elif any(w in blob.lower() for w in ["justdial", "sulekha", "urban company",
            "apps are", "useless app", "fake review"]):
        tb = "TB6"

    mix, script = detect_language(title + " " + body)
    tone = detect_tone(blob)
    length = "one-liner" if len(body) < 40 else ("short" if len(body) < 300 else "detailed")

    pain_row = ["", category, intent, pain, "", spec, "", "", "", "auto-coded; verify"]
    trust_row = ["", ts, tp, tb, "unknown" if tp in ("TP2", "") else "i-used-them", ""]
    lang_row = ["", mix, script, "", "", "", "", tone, length, ""]
    return pain_row, trust_row, lang_row


def main():
    ap = argparse.ArgumentParser(description="Free/legal r/vadodara aggregate coder.")
    ap.add_argument("--limit", type=int, default=100, help="posts to scan (<=100/listing)")
    ap.add_argument("--listing", default="new", choices=["new", "hot", "top"])
    ap.add_argument("--time", default="week", help="for top: hour/day/week/month/year/all")
    ap.add_argument("--with-comments", action="store_true",
                    help="also read comment text in-memory for trust coding")
    ap.add_argument("--force", action="store_true", help="override 6h cadence gate")
    ap.add_argument("--dry-run", action="store_true", help="print counts, write nothing")
    args = ap.parse_args()

    state = load_state()
    enforce_cadence(state, args.force)
    ensure_headers()

    token, ua = get_token()
    params = {"limit": min(args.limit, 100), "raw_json": 1}
    if args.listing == "top":
        params["t"] = args.time
    data = api_get(f"/r/{SUBREDDIT}/{args.listing}", token, ua, params)

    posts = [c["data"] for c in data.get("data", {}).get("children", [])]
    coded = 0
    for post in posts:
        comments_text = ""
        if args.with_comments and post.get("num_comments", 0) > 0:
            cid = post.get("id")
            try:
                cdata = api_get(f"/r/{SUBREDDIT}/comments/{cid}", token, ua,
                                {"limit": 50, "depth": 3, "raw_json": 1})
                # concatenate comment bodies IN MEMORY ONLY (never written)
                def walk(node):
                    out = []
                    for ch in node.get("data", {}).get("children", []):
                        d = ch.get("data", {})
                        if "body" in d:
                            out.append(d["body"])
                        if d.get("replies"):
                            out.extend(walk(d["replies"]))
                    return out
                if len(cdata) > 1:
                    comments_text = "\n".join(walk(cdata[1]))
            except Exception:
                comments_text = ""

        pain_row, trust_row, lang_row = code_thread(post, comments_text)
        # delete in-memory text ASAP
        comments_text = None

        if args.dry_run:
            coded += 1
            continue

        tid = f"R{state['next_id']:03d}"
        state["next_id"] += 1
        pain_row[0] = trust_row[0] = lang_row[0] = tid
        append_row("pain-coding-sheet.csv", pain_row)
        append_row("trust-coding-sheet.csv", trust_row)
        append_row("language-tone-log.csv", lang_row)
        coded += 1

    if not args.dry_run:
        state["last_run"] = datetime.now(timezone.utc).isoformat()
        save_state(state)

    print(f"Coded {coded} threads from r/{SUBREDDIT}/{args.listing}. "
          f"{'(dry-run, nothing written)' if args.dry_run else 'Rows appended to ../instruments/'}")
    print("Reminder: spot-check auto-codes by hand; heuristics are approximate. "
          "No usernames, URLs, quotes, or PII were stored.")


if __name__ == "__main__":
    main()
