# Research Instruments — how to use

Plug-and-play templates for the **manual, human** Reddit observation phase
(method defined in `../reddit-research-plan.md` §8). These make the study
executable without any automated scraping.

## Files
- `pain-coding-sheet.csv` — one row per thread; pain/demand coding.
- `trust-coding-sheet.csv` — one row per thread where trust signals appear;
  links to pain sheet via `thread_id`.
- `language-tone-log.csv` — one row per thread; how Vadodara writes (§5).

## How to run (per the plan)
1. Read a public thread in a normal browser (no scripts, no API harvesting).
2. Assign the next internal `thread_id` (R001, R002…). **Do not** store the
   Reddit URL or username anywhere in these sheets.
3. Fill categorical codes + neutral paraphrase. **Never** paste a sentence from
   the thread.
4. Stop when new threads stop producing new codes (saturation), target
   ~60–100 threads.
5. Roll up into themes → confirm/refute hypotheses H1–H7 (`../market-research.md` §7)
   and the category predictions (`../deep-dive.md` §1).

## Hard rules (non-negotiable)
- No usernames / handles / profile links.
- No verbatim quotes.
- No phone numbers, addresses, or personal/provider names.
- No URLs stored beyond a transient working tab.
- Aggregate patterns only — never present one person's experience as a finding.
- Public content only; observe, never post/comment/DM/vote.
