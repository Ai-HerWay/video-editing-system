# Style system

Treat the tokens in `assets/frame.md` as normative. Use this reference for visual judgment.

## Identity

Quiet Editorial UI combines literary display typography with precise software-interface structure. It should feel composed, calm, useful, and tactile without becoming nostalgic or ornamental.

## Hierarchy

- Give each beat one dominant sentence, object, or state change.
- Use Playfair Display for display language and Montserrat for everything operational.
- Use italic display type once per beat at most.
- Set small labels in Montserrat 700 uppercase with `0.12em–0.18em` tracking.
- Use size and serif/sans contrast before adding color or weight.
- Preserve generous negative space; do not fill every open region.

## Surfaces

- Use the warm canvas continuously across graphic-only scenes.
- Use active white for the selected or foreground surface and quiet gray for supporting surfaces.
- Use 2px borders at 1080px short-edge resolution; scale proportionally.
- Use 16–26px radii for cards and windows, full pills only for compact labels or controls.
- Keep shadows black at 6–12% opacity with broad, soft falloff.
- Avoid gradients, glass blur, neon, heavy glow, thick borders, and decorative particles.

## Color semantics

- Ink carries hierarchy.
- Secondary gray carries metadata and de-emphasized copy.
- The success green means complete, confirmed, ready, or passed. Use it once at a time.
- A system-object color may describe a real object, such as a file type or status, but must not spread into general decoration.
- When a supplied brand color must remain, use it only on the supplied brand entity or its semantic state.

## Components

- Editorial headline: large Playfair Display, sentence case, exactly one restrained Playfair-italic accent word (Walnut on light grounds, Dusty Blue on dark grounds).
- Kicker: Montserrat 700 uppercase, tracked, optionally preceded by a short gold hairline rule.
- Document card: active white, gray hairline, modest radius, soft shadow.
- Window: quiet toolbar, thin divider, centered utility label, no ornamental chrome.
- Progress path: ink hairline with compact nodes and one semantic success state.
- Cursor: crisp black-and-white pointer; use only when it causes a visible state change.
- Selection: change border, scale, clarity, underline, or position rather than adding a loud glow.

## Failure signatures

- Generic SaaS dashboard grids.
- Repeated equal-weight cards.
- Every headline italicized.
- Green applied decoratively.
- Tiny interface copy that works only at desktop zoom.
- Floating fades with no causal action.
- Empty footage covered merely because an overlay is available.
