# Halo — Vadodara Reddit Research Plan

> **Status: PLAN ONLY.** No scraping, no automated collection, no code changes.
> This document defines *how* to study Vadodara Reddit conversations before any
> research begins. Execution is deliberately gated until this plan is approved.

---

## 0. Purpose & guardrails (read first)

**Why we're doing this.** Halo's core thesis is that Vadodara doesn't have a
talent shortage — it has a *trust and clarity* problem. To build the right
product and the right onboarding questionnaire, we need to understand, in
locals' own words: what they ask for, what they can't find, how they write,
what answers they get, where trust breaks, and which gaps Halo can close.

**How we behave while doing it.** Reddit is a community of real people, not a
dataset. We study it the way a respectful observer would: reading public
threads, learning patterns, and writing down *aggregated, anonymized*
insights — never harvesting people. The rules in §8 are not optional.

**Non-negotiables for this phase:**
- No automated scraping. Manual reading only.
- No usernames, handles, or other identifiers recorded — ever.
- No personal data stored. No DMs. No contacting anyone.
- No verbatim quotes that could be searched back to a person.
- No website/product code changes as part of research.
- Public subreddits only; nothing private, restricted, or gated.

---

## 1. Reddit research framework

A four-stage, observation-only method. Each stage has a clear stop/go.

### Stage A — Scoping (define before reading)
- Lock the research questions (the 7 goals below).
- Define the unit of analysis: a **thread** (the original post + its reply
  tree), treated as one anonymized observation.
- Decide sample size up front: target **60–100 threads** across categories,
  enough for pattern saturation without over-collecting.
- Set a time window: prioritize the **last 12–18 months** so findings reflect
  current behavior, with a small sample of older "evergreen" threads for
  contrast.

### Stage B — Source survey (where to look — see §1.1)
- Primary: **r/vadodara**.
- Secondary (only if they add signal): r/Baroda, r/gujarat, r/india,
  r/IndiaTech, r/AskIndia, and city analogs (r/ahmedabad, r/surat, r/pune,
  r/bangalore) used **only** for comparative pattern-checking, never as a
  substitute for Vadodara-specific behavior.

### Stage C — Structured observation (how to read)
- Read threads in their natural form on the public web.
- For each thread, fill a single row in the coding sheets (§3–§5) using
  **categorical codes and paraphrase**, not copied text.
- Capture *patterns*, not posts: "multiple threads ask for X with no Y" beats
  any single example.
- Stop when new threads stop producing new codes (**saturation**), not when a
  quota is hit.

### Stage D — Synthesis (turn observation into product input)
- Roll codes up into themes.
- Map each theme to a Halo capability or gap (§6).
- Translate themes into questionnaire principles and draft questions (§7).
- Write the findings as aggregate statements only.

### 1.1 Source-selection rule
Include a secondary subreddit **only** when it answers a question r/vadodara
can't — e.g. comparing how trust is established in a larger metro. If a
secondary source merely repeats r/vadodara signal, drop it. Vadodara behavior
is the ground truth; everything else is a sanity check.

---

## 2. Categories to track

Tag every observed thread with **one primary category** (and optional
secondary). These are the demand buckets Halo cares about.

| Code | Category | Examples of what locals seek |
|------|----------|------------------------------|
| C1 | Home & repair services | electrician, plumber, carpenter, AC repair, pest control, deep cleaning |
| C2 | Trades & construction | contractor, interior, false ceiling, painter, fabrication |
| C3 | Health & care | dentist, physio, pediatrician, diagnostic lab, elder care, gym/trainer |
| C4 | Education & coaching | tutors, exam coaching, music/art, language, skill classes |
| C5 | Events & lifestyle | photographer, decorator, caterer, makeup artist, DJ, tailoring |
| C6 | Food & home kitchens | tiffin/mess, home bakers, regional specialties |
| C7 | Auto & transport | mechanic, car wash, driver, two-wheeler service, packers & movers |
| C8 | Professional services | CA, lawyer, architect, web/design freelancers, marketing |
| C9 | Pets, plants, niche | vet, pet grooming, gardener, nursery |
| C10 | Local info / "where do I…" | govt processes, where to buy X, area recommendations |
| C11 | Buy/sell/rent | second-hand goods, flats/PG, brokers |
| C12 | Other / uncategorized | catch-all; review periodically to spawn new codes |

**Also tag each thread with intent type:**
- `seek` — asking for a recommendation/provider
- `vent` — frustration about a bad experience or being unable to find someone
- `info` — asking how/where (process, not a person)
- `offer` — someone advertising their own service
- `review` — sharing an experience (good or bad) unprompted

---

## 3. Pain-point coding sheet

One row per thread. **Codes and paraphrase only — no quotes, no usernames.**

| Field | Values / notes |
|-------|----------------|
| Thread ID | Internal sequential number (R001…). NOT a Reddit ID or URL stored long-term. |
| Category | C1–C12 (§2) |
| Intent | seek / vent / info / offer / review |
| Pain type | see pain codes below |
| Search effort described | none / asked friends / Google/JustDial / tried apps / asked here as last resort |
| Specificity of ask | vague ("good electrician") / area-specific / budget-specific / time-specific / quality-specific |
| Unmet need (paraphrase) | one neutral sentence, no identifying detail |
| Did they get a usable answer? | yes / partial / no / only DMs offered |
| Halo relevance | high / medium / low |

**Pain codes (P-series):**
- `P1` Can't find anyone at all
- `P2` Found names but can't tell who's good (choice paralysis)
- `P3` Found someone but unsure they're trustworthy/will show up
- `P4` Price opacity / fear of being overcharged ("non-local price")
- `P5` Quality inconsistency / past bad experience
- `P6` Reachability — listed but doesn't answer / ghosting
- `P7` Distance/area mismatch — found someone, too far
- `P8` Language/communication barrier
- `P9` Niche/long-tail need with no obvious source
- `P10` Time-sensitive/urgent need with no fast option

---

## 4. Trust-gap coding sheet

Trust is Halo's central wedge, so it gets its own sheet. One row per thread
where trust signals appear.

| Field | Values / notes |
|-------|----------------|
| Thread ID | R-number (links to §3 row) |
| Trust signal sought | see TS codes |
| Trust proof offered in replies | see TP codes |
| Trust breakdown observed | see TB codes |
| Who is trusted as the source | friend-of-friend / commenter with history / "I used them" / unknown |
| Verification gap | what would have made the asker confident but was missing |

**Trust-signal-sought codes (TS):**
- `TS1` "Has anyone *actually* used them?"
- `TS2` Wants proof of reliability (shows up, finishes work)
- `TS3` Wants fair/transparent pricing
- `TS4` Wants quality evidence (photos, past work)
- `TS5` Wants someone local/known to the community
- `TS6` Wants safety assurance (entering home, handling money/kids/elders)

**Trust-proof-offered codes (TP):**
- `TP1` First-hand "I used them and…" account
- `TP2` Contact number drop with no context
- `TP3` Self-promotion / "DM me"
- `TP4` Vouching for a known local
- `TP5` Photos/portfolio shared
- `TP6` Warning / "avoid this person" (negative proof)

**Trust-breakdown codes (TB):**
- `TB1` Only unverifiable contacts offered (numbers, no experience)
- `TB2` Suspected self-promotion / sockpuppeting
- `TB3` Conflicting recommendations, no way to adjudicate
- `TB4` Recommendation is stale (worked years ago)
- `TB5` No follow-through proof (no one confirms outcome)
- `TB6` Asker explicitly distrusts existing apps/directories

> **Insight target:** map each `TB` to a Halo feature that would close it
> (e.g. TB5 → Halo Local Score from verified post-job reviews).

---

## 5. Language / tone observations

Halo's copy already mixes Gujarati and English ("આપણું વડોદરા", "Ae halo").
Research must capture *how locals actually write* so the product and
questionnaire sound native, not translated.

Track (as aggregate notes, not quotes):
- **Code-mixing patterns** — Gujarati/Hindi/English blend; script vs.
  Romanized Gujarati; where each language shows up (emotion vs. logistics).
- **Local vocabulary** — terms for areas, services, money, "trustworthy",
  bargaining; how people name neighborhoods.
- **Tone of asks** — casual, urgent, apologetic, frustrated, communal
  ("apna shbehar mein koi…").
- **How they describe quality** — what words signal "good" vs. "avoid".
- **Politeness/formality norms** — how requests and thanks are phrased.
- **Length & structure** — one-liners vs. detailed context posts.
- **Emoji / formatting habits.**

Output: a one-page **"how Vadodara talks" style note** — recurring phrasings
(generalized, never attributable) that inform UI microcopy and question
wording. We capture the *pattern* ("asks often open with the area name"), never
a specific person's sentence.

---

## 6. Local gaps Halo can solve (synthesis map)

For each recurring pain/trust theme, record:

| Field | Notes |
|-------|-------|
| Theme | rolled-up from §3/§4 codes |
| Frequency | how common across the sample (high/med/low) |
| Current workaround | what locals do today (asking Reddit, JustDial, word of mouth) |
| Why it fails | the gap |
| Halo lever | which Halo capability addresses it (Local Score, AI match, area+price transparency, verified reviews, direct reach, no-commission supply) |
| Confidence | how strongly the data supports this (so we don't over-claim) |

**Hypotheses to test against the data (not assume):**
- The dominant problem is *adjudication* (P2/P3), not discovery (P1).
- Trust is conferred socially (friend-of-friend), and Reddit is a *last
  resort* when that network fails — Halo can systematize that social proof.
- Price opacity (P4) is a recurring trust wound a transparent score + local
  pricing can heal.
- A meaningful share of demand is long-tail/niche (P9) that directories
  serve poorly.

Each hypothesis is **confirmed / refuted / unclear** by the end, with
aggregate evidence — never anecdote-driven.

---

## 7. Questionnaire design principles

The onboarding questionnaire ("What you tell Halo" → "What Vadodara sees")
should be derived from observed demand and trust signals, so providers supply
exactly what seekers look for.

### Design principles
1. **Ask only what a seeker needs to choose.** Every question must map to a
   real decision factor seen in §3/§4 (area, price, proof, reliability).
2. **Mirror local language.** Use the words and code-mix locals actually use
   (from §5), not corporate category names.
3. **Lead with trust inputs.** Capture the things that close trust gaps:
   service area, price transparency, proof of past work, response speed.
4. **Low friction for non-marketers.** Halo's pitch is "you don't have to
   become a marketer" — questions should be answerable by a busy tradesperson
   in minutes; prefer choices over essays.
5. **Structured > free text** where it powers AI matching, but leave room for
   the human voice.
6. **Feed the Local Score honestly.** Don't ask providers to self-rate
   quality; capture verifiable inputs and let reviews build the score.
7. **Bilingual-first.** Questions and answers should work in Gujarati and
   English.

### Candidate question themes (to validate against data, not final copy)
- What do you do, in your own words? (maps to category + long-tail)
- Which areas of Vadodara do you serve? (P7 distance gap)
- How do you price — fixed, hourly, per-visit, "depends"? (P4 transparency)
- Typical response/availability time? (P6/P10 reachability & urgency)
- Show your work — photos/examples? (P5/TS4 quality proof)
- Languages you work in? (P8/TS communication)
- How should people reach you? (closes "finding → reaching" gap)

> Final wording is produced *after* §5 language analysis so it sounds native.

---

## 8. Safe, rule-respecting research method

This is the binding method for the execution phase. If a step here conflicts
with anything above, this section wins.

**Reddit rules & ethics**
- Read **public content only**, in a normal browser, as a logged-out or
  ordinary reader. No private/quarantined/restricted communities.
- **No automated scraping, crawling, or bulk export.** No scripts, no API
  pulls for harvesting, no headless browsers. Manual reading and manual notes
  only. (If we ever need scale later, that requires a *separate* decision and
  Reddit's official API under its terms — out of scope for this phase.)
- Respect rate of a human reader; do not hammer the site.
- Do not post, comment, vote, DM, or otherwise interact while researching —
  observe only.
- Follow r/vadodara's own community rules.

**Data minimization (privacy by design)**
- Record **only** aggregated, categorical codes and neutral paraphrase.
- **Never** store: usernames, handles, profile links, post URLs (beyond a
  transient working tab), avatars, timestamps tied to a person, or any PII
  that appears in a thread (phone numbers, addresses, names of providers).
- If a provider's phone number or name appears in a thread, it is **not**
  captured — that is exactly the kind of personal data we exclude.
- Coding sheets contain internal R-numbers only; no key links R-numbers back
  to real threads after analysis.
- No verbatim quotes in any output. Paraphrase to the point where it cannot be
  reverse-searched.

**§8.1 What NOT to copy or expose**
- Don't copy real reviews, posts, or comments into Halo or any output.
- Don't reproduce or seed Halo with scraped recommendations or contact lists.
- Don't expose, screenshot, or republish identifiable user content.
- Don't import provider names/numbers found on Reddit into Halo's listings.
- Don't quote phrasing so distinctive it identifies an author.
- Don't present any single person's experience as a finding — only patterns.

**§8.2 Outputs of the execution phase (when approved)**
1. Filled coding sheets (anonymized, R-numbered, no PII).
2. Theme synthesis with frequency + confidence (§6).
3. "How Vadodara talks" style note (§5).
4. Validated questionnaire principles + draft question set (§7).
5. A short ethics log confirming §8 was followed.

---

## 9. Open decisions before execution
- Approve the sample size (proposed: 60–100 threads to saturation).
- Confirm secondary subreddits are comparison-only, not data sources.
- Confirm we capture **zero** verbatim quotes (recommended) vs. a tightly
  controlled paraphrase-only allowance.

> **Nothing in this plan runs until explicitly approved.** This phase is
> design-paused and research is plan-only by request.
