# Design

## Concept

"One day in Vadodara." The page is a single scroll through a city day: pre-dawn intro, sunrise hero (the halo ring is the rising sun over the city skyline), white daylight for the living sections, terracotta dusk for the vision, lamp-lit night for join + footer. The body background transitions between scene skies; sections are transparent.

## Color (scene skies + roles)

- `--dawn` #20120C: pre-dawn / hero sky (dark espresso brown)
- `--day` #FBF9F6: daylight body (true off-white, near zero chroma; warmth lives in accents, not the bg)
- `--dusk` #A23D12: vision scene, drenched terracotta
- `--night` #150C07: intro, join, footer
- `--ink` #1F150D, `--ink-soft` #5C4D3E (on day)
- `--terra` #C24E1E (large display accents on day), `--terra-deep` #8F3414 (small accent text on day), `--btn` #A8400F (buttons, white text >= 4.5:1)
- `--maroon` #5E2114, `--leaf` #45522F, `--haldi-deep` #9A6A14 (gali shop-board plates)
- `--gold` #D9A441 (night/dawn accents), light text on dark: #F4E9DC / soft #C9B49E

Strategy: full palette, scene-drenched. No cream body backgrounds.

## Typography

- Display: "Young Serif" 400 (warm, sturdy, clay-and-bread; no italic, emphasis via color/size)
- Body/UI: "Hind Vadodara" 400/500/600 (Indian Type Foundry; named after the city; native Gujarati support)
- Display Gujarati: "Noto Serif Gujarati"
- Handwritten accents only: "Caveat" (vouch lines, tiny annotations)
- Scale ratio >= 1.3; h1 clamp max 5.5rem; `text-wrap: balance` on headings.

## Brand systems

- **City clock stamps**: every scene opens with a Gujarati-numeral time + a local label ("૦૭:૪૩ · chai round one"). This replaces uppercase eyebrows.
- **Parchi**: recommendation card as a paper chit; slight rotation, gold pin, rotated "HALO TRUSTED" ink stamp, Caveat vouch line.
- **Dhaago**: trust process drawn as a stitched thread (SVG dash drawn on scroll) with five beats.
- **Gali boards**: neighbourhoods as painted shop-board plates (saturated bg, double inset border) in a horizontal scrubbed strip; native swipe + scroll-snap on mobile.
- **Otla**: the society-group chat, scroll-scrubbed message reveal.

## Motion

- Scene skies: body background-color transition (.9s) driven by IntersectionObserver.
- Scroll scrubs (rAF, transform/opacity only): hero sunrise, otla chat reveal, gali horizontal pan, dhaago thread draw.
- Reveals: enhance-only (`html.js` gate), ease-out expo, no bounce.
- prefers-reduced-motion: intro skips, scrubs render final state, sticky scenes become static, all content visible.

## Layout

- Max content width 1100px; fluid edge padding clamp(20px, 5vw, 64px).
- One dominant idea per fold; asymmetric two-column scenes (artifact + words); no card grids.
- z-scale: nav 60 < intro 100; toasts/none.
