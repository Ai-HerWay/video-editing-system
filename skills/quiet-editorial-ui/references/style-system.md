# Style system

The normative values live in `assets/frame.md`. This page is for the judgement calls the tokens can't make for you.

## The feeling to aim for

Quiet Editorial UI is what you get when you set literary display type against the structure of a well-made piece of software. It should read as composed, calm, useful, and slightly tactile — never nostalgic, never ornamental. If a frame feels like a magazine spread that happens to contain an interface, you are close. If it feels like a template, start again.

## Building hierarchy

- Give each beat a single dominant thing — one sentence, one object, or one state change. Not two.
- Playfair Display is the display voice; Montserrat is the operational voice. Never blur the two.
- One italic display word per beat is the ceiling, not a target.
- Small labels are Montserrat 700, uppercase, tracked `0.12em–0.18em`.
- Reach for size and serif/sans contrast first. Colour and weight are later resorts, not first moves.
- Protect the negative space. An open region is doing work; don't fill it because you can.

## Working with surfaces

- The warm canvas runs continuously underneath graphic-only scenes.
- Active white is the selected or foreground surface; quiet grey is for supporting surfaces.
- Borders read as 2px at 1080px short-edge; scale that proportionally at other sizes.
- Cards and windows take 16–26px radii. Full pills are only for compact labels or controls.
- Shadows stay black at 6–12% opacity with a broad, soft falloff.
- Nothing glassy, gradient, neon, glowing, thickly outlined, or particle-strewn.

## What the colours mean

- Ink is hierarchy.
- Secondary grey is metadata and anything deliberately de-emphasised.
- The success green means complete / confirmed / ready / passed, and it appears once at a time.
- A system-object colour may describe a real object — a file type, a status — but must never leak into general decoration.
- When a supplied brand colour has to stay, keep it on the supplied brand entity or its semantic state, nowhere else.

## The component grammar

- **Editorial headline** — large Playfair Display, sentence case, exactly one restrained Playfair-italic accent word (Walnut on light, Dusty Blue on dark).
- **Kicker** — Montserrat 700 uppercase, tracked, optionally led by a short gold hairline rule.
- **Document card** — active white, grey hairline, modest radius, soft shadow.
- **Window** — quiet toolbar, thin divider, a centred utility label, no ornamental chrome.
- **Progress path** — an ink hairline with compact nodes and one semantic success state.
- **Cursor** — a crisp black-and-white pointer, present only when it drives a visible change.
- **Selection** — signalled by a change in border, scale, clarity, underline, or position, never by a loud glow.

## Signs you have drifted

- SaaS dashboard grids.
- Repeated cards of equal weight.
- Every headline italicised.
- Green used as decoration.
- Interface copy so small it only works at desktop zoom.
- Fades with no causal action behind them.
- Empty footage covered simply because an overlay was available.
