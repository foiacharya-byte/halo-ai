# Halo — Safe r/vadodara Research Workflow

> **Scope & stance.** This is a *compliant* observation workflow. It does **not**
> bypass technical blocks, defeat rate limits, or scrape against Reddit's
> Terms. Two allowed paths only: (A) **manual browser reading** by a human, and
> (B) **optional official Reddit API** under Reddit's posted terms and rate
> limits. Everything is aggregate, anonymized, and PII-free.
> Pairs with `reddit-research-plan.md` (method), `market-research.md` (gaps),
> `deep-dive.md` (category map + questionnaires), `instruments/` (coding CSVs).
> _Compiled June 2026._

---

## 0. Hard rules (apply to BOTH paths)

| ✅ Always | ❌ Never |
|----------|---------|
| Read public content only | Bypass blocks, logins, paywalls, or rate limits |
| Aggregate / categorical coding | Store usernames or handles |
| Neutral paraphrase | Store verbatim quotes |
| Internal `thread_id` (R001…) | Store profile links, post URLs (beyond a transient tab) |
| Observe only | Post, comment, vote, DM, or contact anyone |
| Respect robots.txt & ToS | Harvest phone numbers, names, addresses |
| Human-pace, 1 pass per 6–12h | Hourly polling or bulk crawling |

If a step ever requires defeating a block to proceed, **stop** — that's the
signal you've left the compliant path.

---

## 1. Exact manual workflow (primary path)

A human reads r/vadodara in a normal browser and records codes. ~20–30 min
per session, once or twice a day.

**Cadence:** one pass every **6–12 hours** (e.g. morning + evening), or once
daily. Never hourly. The goal is pattern saturation across ~60–100 threads
over days/weeks — not a live feed.

**Per-session steps:**
1. Open r/vadodara in a normal browser, logged out or as an ordinary reader.
2. Sort/browse: `New` for fresh demand, `Top → This week/Month` for high-signal
   threads. Use the subreddit's own search for recurring terms:
   `recommendation`, `suggest`, `best`, `where`, `trusted`, `avoid`, plus
   category words (electrician, tiffin, dentist, tutor, mechanic, PG…).
3. For each relevant thread (an *ask* or *experience* about a local service):
   - Assign the next `thread_id` (R001, R002…). Do **not** save the URL or any
     username.
   - Skim the post + reply tree once.
   - Fill one row in each coding CSV (`instruments/`): pain, trust, language.
   - Paraphrase the unmet need / verification gap in **one neutral sentence**.
     If you can't paraphrase without identifying someone, write the code only.
4. Close the tab. Nothing about the person leaves the page.
5. Stop the session when you hit your time box; stop the *study* when new
   threads stop producing new codes (saturation).

**What "human-pace" means:** you read like any visitor. No scripts opening
tabs, no copy-paste of comment text into the sheet, no downloading pages.

---

## 2. Optional official API workflow (only if scale is needed)

Use **only** Reddit's official API under its current terms — never an
unofficial scraper or a block workaround. This path is optional; the manual
path is sufficient for this study.

**Preconditions (all required):**
- Registered Reddit API app + OAuth credentials.
- Compliance with Reddit's API Terms and the **posted rate limits** (do not
  exceed; back off on 429s).
- Read-only use; **no** storage of user-level data.

**Allowed use — listing/metadata only, then human reads the rest:**
1. Pull *listing metadata* for r/vadodara (e.g. `new`/`top` listings): use it
   only to get a queue of **post titles + internal counters** to triage which
   public threads a human should read.
2. **Drop every user field on ingest.** Discard `author`, `author_fullname`,
   profile fields, exact timestamps tied to a user, and any free-text body
   before it is written anywhere. Keep only: title, category guess, score,
   num_comments, subreddit, an internal `thread_id`.
3. **Do not** fetch or persist comment bodies via API for storage. Trust/proof
   coding is still done by a **human reading the public thread**, recording
   codes only — the API is a *triage queue*, not a content store.
4. Cadence: a single scheduled pull every **6–12 hours**. No tighter. No
   continuous streaming.
5. Persist nothing but the anonymized coding CSVs.

**Where the API must NOT be used:** building a dataset of comments, mapping
users, storing post text, re-publishing content, or seeding Halo with any
contact/recommendation found on Reddit.

> If the API terms or rate limits make a step awkward, that's a stop signal —
> fall back to manual reading. We never "make it work" by bypassing limits.

---

## 3. Fields to collect

Only these. All are aggregate/categorical or neutral paraphrase. (Full legends
live in `instruments/*.csv`.)

**Demand / pain (`pain-coding-sheet.csv`):**
`thread_id` · `category` (C1–C12) · `intent` (seek/vent/info/offer/review) ·
`pain_code` (P1–P10) · `search_effort` · `specificity` ·
`unmet_need_paraphrase` (1 neutral sentence) · `got_usable_answer` ·
`halo_relevance` · `notes`

**Trust (`trust-coding-sheet.csv`):**
`thread_id` · `trust_signal_sought` (TS1–TS6) · `trust_proof_offered`
(TP1–TP6) · `trust_breakdown` (TB1–TB6) · `trusted_source_type` ·
`verification_gap_paraphrase`

**Language / tone (`language-tone-log.csv`):**
`thread_id` · `language_mix` · `romanized_or_script` · `emotion_language` ·
`logistics_language` · `local_vocab_paraphrase` (generalized) ·
`quality_words_paraphrase` · `ask_tone` · `ask_length` · `formatting_habit`

---

## 4. Fields NEVER to collect

- Usernames, handles, display names, `author`/`author_fullname`.
- Profile links, avatars, karma, account age.
- Post/comment **URLs** or permalinks (beyond a transient open tab).
- **Verbatim quotes** of any post or comment.
- Phone numbers, email, addresses, social handles.
- Personal names or **provider/business names** mentioned in threads.
- Exact timestamps tied to an individual.
- Screenshots of identifiable content.
- Any field that, combined with others, could re-identify a person or a
  specific thread.

> **Reverse-search test:** before saving any paraphrase, ask "could someone
> paste this into search and find the original post/author?" If yes, generalize
> further or keep the code only.

---

## 5. Coding template (quick reference)

One row per thread across the three CSVs, linked by `thread_id`.

```
thread_id : R001
category  : C1            # home & repair
intent    : seek
pain_code : P3            # reliability doubt
search    : last-resort   # tried apps/friends first
specificity: area
unmet     : "asked for someone dependable nearby; unsure who will show up"  # paraphrase, no PII
answer    : only-dms
relevance : high
---
TS_sought : TS1           # "has anyone actually used them?"
TP_offered: TP2           # bare number, no experience
TB_break  : TB1           # only unverifiable contacts
source    : unknown
gap       : "wanted proof of past reliability; none given"  # paraphrase
---
lang_mix  : guj-eng
script    : roman
emotion   : gujarati
logistics : english
tone      : casual
length    : short
```

Legends: see `instruments/pain-coding-sheet.csv`, `trust-coding-sheet.csv`,
`language-tone-log.csv` (codes defined inline).

---

## 6. Turning findings into Halo questionnaire insights

The pipeline from coded rows → product decisions:

1. **Aggregate the codes.**
   - Pain frequency: which `pain_code` dominates? (Tests **H1** — is it P2
     choice-paralysis, not P1 discovery?)
   - Trust learnability: ratio of **TP1** (first-hand "I used them") to
     **TP2/TP3** (bare numbers/self-promo). High TP1 = trust is socially
     conferred and *systematizable* by the Local Score.
   - Breakdown map: most common `trust_breakdown` → the gap Halo must close.

2. **Map each dominant code to a questionnaire field** (drafts in
   `deep-dive.md` §3):
   | Finding | Questionnaire response |
   |---------|------------------------|
   | P4 price-opacity is common | Provider Q3 "How do you price?" + Seeker Q4 budget-feel |
   | P6/P10 ghosting & urgency | Provider Q4 "response time" + Seeker Q3 "how soon" |
   | TS4 wants quality evidence | Provider Q5 "show your work" (photos) |
   | TS6 safety / TB for home entry | Local Score weighting on repeat + verified jobs |
   | P8 language barrier | Provider Q6 languages + bilingual UI copy |
   | P9 long-tail demand | Seeker Q1 free-text + provider long-tail tags |
   | TB6 distrusts apps | Lead with the Local Score, not listings, in onboarding |

3. **Tune the question *wording* from the language log.** Use the dominant
   `language_mix`, `tone`, and generalized `local_vocab` to phrase questions
   the way Barodians actually write (e.g. open with area, code-mix Guj/Eng).
   Lock final copy only after this step.

4. **Prune ruthlessly.** Any drafted question that no coded finding supports
   gets cut — the questionnaire asks *only* what seekers demonstrably use to
   choose, and captures *only* what closes a documented trust gap.

5. **Validate the review engine.** If TB1/TB5 (unverifiable / no-follow-through)
   dominate, that confirms the post-job review (`deep-dive.md` §3.3) and its
   integrity rules are the highest-priority build, not a nice-to-have.

**Output of the study:** an updated, evidence-backed questionnaire spec +
"how Vadodara talks" copy note — all from aggregate codes, zero PII, zero
quotes.

---

## 7. Stop conditions
- New threads stop producing new codes → **saturation**, end the study.
- A step requires bypassing a block/limit → **stop**, you've left the compliant
  path.
- Any PII would need to be stored to proceed → **stop**, recode without it.
