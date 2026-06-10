# halo_reddit_coder.py — the free, legal way to get the data

## The key point: this costs ₹0
Reddit's **official API has a free tier**. Low-volume reads (one r/vadodara
study, a couple runs a day) are well within it. You do **not** need the paid
plan — that's only for high-volume commercial pulls. No credit card, no money.

This script uses the official API the legal way and writes out **only
aggregate codes** — never usernames, URLs, quotes, phone numbers, or PII.

## Why I can't just run it for you
- This cloud environment is network-blocked from Reddit (by design).
- It has no Reddit credentials.
So you run it on **your own machine** — free — with your own free API app.

## Setup (one time, ~3 minutes, free)
1. Log in to Reddit (free).
2. Visit https://www.reddit.com/prefs/apps → **create another app…**
3. Type: **script**. redirect uri: `http://localhost:8080` (unused).
4. Copy the **client id** (small text under the app name) and the **secret**.
5. In your terminal:
   ```bash
   export REDDIT_CLIENT_ID="your_id"
   export REDDIT_CLIENT_SECRET="your_secret"
   export REDDIT_USER_AGENT="halo-research by u/yourusername"
   ```

## Run it
```bash
# scan latest 100 posts + their comments, code them, append to ../instruments/*.csv
python3 halo_reddit_coder.py --listing new --limit 100 --with-comments

# high-signal threads from the past month
python3 halo_reddit_coder.py --listing top --time month --limit 100 --with-comments

# see counts without writing anything
python3 halo_reddit_coder.py --dry-run --with-comments
```

## What it does / doesn't store
- **Reads** post titles, bodies, and comments **in memory only** to derive codes.
- **Writes** only: `thread_id` (internal R001…), category, intent, pain code,
  trust codes, language/tone — to the three CSVs in `../instruments/`.
- **Never writes**: usernames, profile links, post URLs, any verbatim text,
  phone numbers, emails, names. Phone/email are *detected* only to set a code
  flag (e.g. TP2 "bare contact"), then discarded.

## Built-in guardrails
- **Free-tier-safe pacing**: 2s between requests, far under limits.
- **No hourly scraping**: refuses to run if <6h since last run (a state file
  tracks this). Use `--force` only if you really mean to.
- **Stops on 429**: if Reddit rate-limits, it exits — it never bypasses limits.
- **App-only OAuth**: read-only, no login, can't post/vote/comment.

## Accuracy note (be honest with yourself)
The data is **real** (the actual threads). The *coding* is keyword-heuristic, so
it's a strong first pass, not perfect. Spot-check ~10–15% of rows by hand and
adjust the keyword maps at the top of the script for Vadodara-specific slang.
For the deepest accuracy, combine: let the script triage + bulk-code, then read
the highest-`halo_relevance` threads yourself (manual workflow in
`../reddit-workflow.md`).

## Then: turn it into questionnaire insights
Follow `../reddit-workflow.md` §6 — aggregate the codes, map dominant pains to
questionnaire fields (`../deep-dive.md` §3), and tune wording from the language
log. Zero PII leaves the pipeline.
