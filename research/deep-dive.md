# Halo — Deep Dive: Category Pain Map, Provider Economics & Questionnaires

> **Layer 3 of the research stack.** Builds on `reddit-research-plan.md` (method)
> and `market-research.md` (market + gaps). This document goes from
> market-level abstractions to **operational, category-level detail**: where
> trust actually breaks per service type, the unit-economics case that drives
> provider supply, and the fully-drafted questionnaires Halo can use.
>
> **Note on Reddit access:** live Reddit reading is *blocked* in this
> environment (and automated harvesting is barred by the plan anyway), so the
> category map below is an **evidence-informed prediction** to be confirmed by
> manual human reading — not observed data. It tells the researcher *what to
> look for* and *what would confirm/refute each hypothesis_.
> _Compiled June 2026._

---

## 1. Category-level pain & trust prediction matrix

For each demand category (codes from the research plan), the predicted
**dominant pain**, **where trust breaks**, the **stakes** (why trust matters
here), and the **Halo lever** that closes it. This is the lens the manual
Reddit reader uses — confirm or refute each row.

| Cat | Service | Predicted dominant pain | Where trust breaks | Stakes | Halo lever |
|-----|---------|--------------------------|--------------------|--------|------------|
| C1 | Home & repair (electrician, plumber, AC, cleaning) | **P3** reliability / **P6** ghosting | Will they show up, finish, not overcharge? Stranger enters home | Money + home + safety | Local Score (show-up + completion), area+price transparency |
| C2 | Trades & construction (contractor, interior, painter) | **P4** price opacity / **P5** quality | Big spend, hard to judge quality upfront; cost overruns | High ₹, hard to reverse | Verified past-work photos, score from finished jobs |
| C3 | Health & care (dentist, physio, peds, elder care) | **P2** choice paralysis / **TS6** safety | Credentials + bedside trust; care of kids/elders | Health, irreversible | First-hand reviews, "actually used them" weighting |
| C4 | Education & coaching (tutors, exam, music) | **P5** quality / **P2** | Results-based; hard to assess before months in | Child's outcomes, time | Outcome-tagged reviews, local parent trust |
| C5 | Events & lifestyle (photographer, decor, makeup, caterer) | **P5** quality / **P4** price | One-shot event, no redo; portfolio may be fake | One-time, high emotion | Portfolio + real-event reviews |
| C6 | Food & home kitchens (tiffin, bakers) | **P5** consistency / **TS6** hygiene | Daily consistency, food safety, taste fit | Health, daily | Repeat-customer reviews, hygiene signals |
| C7 | Auto & transport (mechanic, movers, drivers) | **P4** overcharge / **P3** reliability | Classic "padded bill" fear; handling of goods | Money, possessions | Transparent pricing, score from repeat use |
| C8 | Professional (CA, lawyer, architect, freelancers) | **P2** / **P9** long-tail | Credibility, confidentiality, niche fit | High ₹, legal/financial | Verified outcomes, specialization tags |
| C9 | Pets, plants, niche (vet, grooming, gardener) | **P9** can't find specialist | Thin supply, no obvious source | Pet welfare | Surfaces hidden long-tail supply |
| C10 | Local info / "where do I…" | **P1** / info gap | No person needed — process unclear | Time | AI answers + routes to a person if needed |
| C11 | Buy/sell/rent (PG, flats, brokers) | **P4** broker distrust / **P3** | Broker incentives misaligned; deposit risk | High ₹, fraud risk | Reviewed, no-commission intermediaries |

**Reading instruction:** when a real thread is logged, note whether its actual
pain matches the *predicted* dominant pain. A high match rate validates the
taxonomy; mismatches reveal where Halo's category assumptions are wrong —
those mismatches are the most valuable findings.

---

## 2. Provider-economics teardown — why supply switches to Halo

The hardest side of any marketplace is **supply** (providers). Halo's "0%
commission, you set your price, you own your profile" must be quantified to be
a recruiting weapon. Illustrative comparison on a single ₹1,000 job:

| Line item | Managed marketplace (Urban Company model) | Halo |
|-----------|-------------------------------------------|------|
| Headline job value | ₹1,000 | ₹1,000 |
| Platform commission | up to **25%** → −₹250 | **0%** → −₹0 |
| Pay-to-work fees (training/onboarding/products/subscription, amortized) | material per-job drag (industry: ~₹50k upfront load reported) | none |
| Price control | platform-set | **provider-set** |
| Profile ownership | platform owns customer + ratings | **provider owns profile + score** |
| Net to provider on ₹1,000 | ≈ ₹750 *minus* amortized fees | ≈ ₹1,000 *minus* own costs |
| Downside risk | ID-blocking, surge pressure, opaque algorithm | reputational only (the score) |

**Recruiting message that falls out of this:**
> "Keep your full price. Own your reputation. Let Vadodara find you — no
> commission, no fighting an algorithm."

**Strategic caveat for Halo's own model:** 0% commission means Halo cannot
monetize per-transaction. The research implication is that Halo's eventual
revenue must come from elsewhere (e.g. optional provider visibility/tools,
verticalized lead products) **without** compromising the Local Score's
integrity — because score integrity is the entire moat (market-research §6.4).
Flag this as a business-model question, not a research finding.

---

## 3. Drafted questionnaires (derived from gaps → ready to test)

Two instruments. **Seeker** questions power AI matching; **Provider** questions
build the profile + Local Score inputs. Wording is draft and bilingual-aware
(English + Gujarati gloss); final copy is locked only **after** the §5
language analysis in the Reddit plan confirms native phrasing.

### 3.1 Seeker questionnaire ("Tell Halo what you need")
Principle: ask only what's needed to *choose* (plan §7). Keep to ≤5 taps.

1. **What do you need help with?** (free text + AI category detect)
   _શું કામ છે? / તમને શેની જરૂર છે?_
2. **Which area?** (map/pin or area picker) → closes P7 distance
3. **How soon?** Today · This week · Flexible → closes P10 urgency
4. **Budget feel?** Cheapest that works · Best value · Best quality regardless
   → calibrates against P4 price sensitivity (not a hard filter)
5. **Anything specific that matters?** (optional free text — language, gender
   of provider, brand, etc.) → captures long-tail (P9) + safety (TS6)

> Everything else (who's trusted, fair price, who shows up) Halo *infers* from
> the Local Score — the user should not have to ask for trust; it's the
> default.

### 3.2 Provider questionnaire ("Claim your spot")
Principle: answerable by a busy tradesperson in minutes; choices over essays;
capture *verifiable* trust inputs, never self-rated quality.

1. **What do you do?** (own words → category + long-tail tags)
   _તમે શું કામ કરો છો?_
2. **Which areas of Vadodara do you serve?** (multi-select areas)
3. **How do you price?** Fixed · Per visit · Hourly · "Depends — I'll quote"
   → P4 transparency, without forcing false precision
4. **Typical response time?** Within an hour · Same day · 1–2 days
   → P6 reachability
5. **Show your work** (optional photos of past jobs) → P5/TS4 proof
6. **Languages you work in?** Gujarati · Hindi · English · other → P8
7. **How should people reach you?** (in-app / call / WhatsApp)
   → closes "finding → reaching" gap
8. **Years doing this / anything else Vadodara should know?** (short free text)

> **Not asked:** "rate your own quality," star self-ratings, or anything that
> lets a provider manufacture trust. Quality enters **only** through the Local
> Score, built from real reviews after real jobs.

### 3.3 Post-job review (the Local Score engine — the crown jewel)
Triggered only after a confirmed job. Keep it to 2 taps + optional text:
1. **Did the work get done well?** 👍 / 👎 (+ optional star)
2. **Would you call them again?** Yes / No  → the single most predictive trust
   signal
3. **One line for other Barodians?** (optional, moderated)

> Integrity rules to validate later: review only after a verified job; one
> review per job; weight "would call again" + repeat customers; surface
> recency; flag/limit anonymous unverifiable praise (the failure mode that
> sank JustDial/Sulekha trust — market-research §4 Gap 1).

---

## 4. Handoff: what manual Reddit reading should now confirm

Use the coding-sheet CSV templates in `research/instruments/`. Specifically
test the §1 matrix predictions and the H1–H7 hypotheses (market-research §7).
Highest-value confirmations:
- **H1 / P2** — is "can't tell who's good" really the dominant pain? (drives
  whole strategy)
- **§3.1 Q4** — do askers actually signal price sensitivity, or trust-first?
- **§3.2 Q5** — do providers/recommenders share proof (photos, "I used them"),
  or just drop numbers? (TP1 vs TP2 ratio = how learnable trust is)
- **§1 mismatches** — any category whose real pain differs from predicted.
