---
version: 1
name: Quiet Editorial UI
description: >
  AI Her Way's editorial frame system: literary Playfair Display type set against precise Montserrat interface
  structure, on warm cream surfaces, with restrained depth and motion that only ever reads as cause and effect.
unit: frame
principle: one clear idea · editorial hierarchy · operational precision

colors:
  canvas: "#F2EBDD"
  ink: "#2B1E19"
  text-secondary: "#7B5A49"
  border: "#C0CACE"
  surface-quiet: "#F2EBDD"
  surface-active: "#FAF6EF"
  success: "#AAB6A0"
  success-deep: "#46513D"
  accent-light: "#7B5A49"
  accent-dark: "#C4D6DA"
  hairline: "#B08A62"
  shadow-soft: "rgba(43,30,25,0.06)"
  shadow-raised: "rgba(43,30,25,0.12)"

typography:
  display-xl: { fontFamily: "Playfair Display", style: italic, weight: 400, cqw: 13.9, lineHeight: 0.88, tracking: "-0.06em", color: ink }
  display-lg: { fontFamily: "Playfair Display", style: italic, weight: 400, cqw: 8.9, lineHeight: 0.95, tracking: "-0.04em", color: ink }
  display-md: { fontFamily: "Playfair Display", style: normal, weight: 400, cqw: 4.4, lineHeight: 1.02, tracking: "-0.025em", color: ink }
  body: { fontFamily: "Montserrat", weight: 400, cqw: 2.6, lineHeight: 1.42, color: text-secondary }
  ui: { fontFamily: "Montserrat", weight: 400, cqw: 2.0, lineHeight: 1.3, color: ink }
  ui-strong: { fontFamily: "Montserrat", weight: 700, cqw: 1.9, lineHeight: 1.2, color: ink }
  label: { fontFamily: "Montserrat", weight: 700, cqw: 1.75, lineHeight: 1.1, tracking: "0.16em", upper: true, color: accent-light }
  caption: { fontFamily: "Montserrat", weight: 700, pxAt1080: 96, minPxAt1080: 96, lineHeight: 1.05, color: ink }
  caption-emphasis: { fontFamily: "Playfair Display", style: italic, weight: 400, scale: 1.06, color: accent-light }

spacing:
  edge-portrait: "8.33cqw"
  edge-landscape: "5cqw"
  edge-square: "6.67cqw"
  gap-xs: "1.1cqw"
  gap-sm: "2.2cqw"
  gap-md: "3.7cqw"
  gap-lg: "6cqw"

components:
  card:
    backgroundColor: "{colors.surface-active}"
    border: "0.185cqw solid {colors.border}"
    rounded: "1.5–2.4cqw"
    shadow: "0 1.5cqw 3.8cqw {colors.shadow-soft}"
  card-selected:
    border: "0.185cqw solid {colors.ink}"
    shadow: "0 1.8cqw 4.3cqw {colors.shadow-raised}"
  window:
    backgroundColor: "{colors.surface-active}"
    toolbar: "{colors.surface-quiet}"
    divider: "0.14cqw solid {colors.border}"
    border: "0.185cqw solid {colors.border}"
    rounded: "2.4cqw"
  kicker-rule:
    backgroundColor: "{colors.hairline}"
    size: "3.9cqw × 0.185cqw"
  progress:
    rail: "0.185cqw solid {colors.border}"
    active: "{colors.ink}"
    complete: "{colors.success}"
  caption-clean:
    backgroundColor: transparent
    color: "{colors.ink}"
    shadow: none
  caption-card:
    backgroundColor: "rgba(242,235,221,0.94)"
    border: "0.185cqw solid {colors.border}"
    rounded: "1.5cqw"
    shadow: "0 1.1cqw 2.8cqw rgba(43,30,25,0.10)"
---

# Quiet Editorial UI

## What this frame is for

Every frame should read as something authored, not something dressed up. You are composing calm editorial pages out of four ingredients: literary display type, precise interface copy, warm paper-like surfaces, and state changes you can actually see happen. If a frame looks decorated rather than composed, it is wrong.

## Type

- Playfair Display carries every headline, statistic, pull quote, and italic accent. Montserrat carries everything operational — small-caps eyebrows, labels, footers, list rows, and body copy.
- Hold Playfair Display at weight 400. Allow at most one italic word per beat.
- Set eyebrows and small-caps labels in Montserrat 700, uppercase, generously tracked, in Walnut (`accent-light`).
- The dominant display element should be at least three times the size of the nearest label.
- Keep any load-bearing UI copy at 20px or larger at 1080px short-edge resolution.
- Keep captions at 96px or larger at 1080px portrait width, always on a single line.

### The italic accent

- Exactly one Playfair-italic word per headline acts as the accent. This single italic word is the most recognisable signature in the whole system — never drop it in a retrofit.
- Colour that accent word Walnut (`accent-light`, #7B5A49) on light grounds and Dusty Blue (`accent-dark`, #C4D6DA) on dark grounds.
- Never italicise a second word in the same headline, and never spend the accent colour anywhere but on that one accent word.

## Colour

- `canvas` (Linen Cream) is the warm ground; `ink` (#2B1E19) carries hierarchy.
- `surface-active` (Ivory) is for foreground cards; `surface-quiet` (Linen Cream) is for supporting chrome.
- `success` (Sage) means only complete / confirmed / ready / reassured / passed. `success-deep` (Deep Olive) is the strongest confirmed state.
- `hairline` (Gold, #B08A62) is the thin ~2px rule that sits directly under a headline, and the colour for the rare hand-drawn or script accent — nothing else.
- The italic accent colour — Walnut on light, Dusty Blue on dark — belongs only to the one italic accent word.
- One highlight marker is allowed: a single word may sit on a colour block (Dusty Blue, Espresso, Sage, or Walnut), at most once per beat.
- These are signature devices, not a licence to decorate. Beyond the italic accent, the gold hairline, and one highlight marker, add no further accent.

## Depth and shape

- Borders read as roughly 2px, shadows stay restrained, radii land in the 16–26px range.
- Full pills are for compact labels, actions, or status only.
- No glass blur, gradients, thick outlines, neon, heavy glow, or decorative particles.
- Let the warm canvas breathe through — never tile the frame with equal-weight cards.

## Frame treatments

### Available-area stage

Anchor one editorial headline and one operational object inside a stable pocket of negative space. Leave the source subject and source UI untouched. Cursor travel stays inside the verified region.

### Direct overlay

Only place the message over footage after you have mapped faces, source text, logos, and motion. Drop a localised warm-white surface onto busy footage. Reserve unboxed ink for moments where contrast holds steady across the whole beat.

### Full-frame editorial

Warm canvas, one dominant headline, and one secondary object — a document card, a window, a selection list, or a progress path. Keep real negative space.

### Progress and completion

An ink hairline, compact numbered nodes, and a single green completed state. Move one object continuously along the path rather than swapping in disconnected cards.

### Closing action

A large serif phrase, one tidy operational object, and a compact action or status. Introduce no new claims and no product identity.

## Motion

- Reveal in order: label, then hero, then operational object.
- Primary entrances travel 12–42px over 0.35–0.62s.
- A cursor appears only when it selects, moves, groups, or confirms something.
- Keep spatial continuity between states.
- Exits are short and decisive.
- Opacity supports the move; it is never the whole move.

## Captions

- Montserrat 700, two to four words, one line, no punctuation.
- One Playfair Display italic emphasis word is allowed when it genuinely matters, Walnut on light grounds or Dusty Blue on dark.
- Reserve the caption lane before you compose the overlays.
- Clean treatment on quiet grounds; card treatment on busy footage.
- Shift the lane around faces and source UI; never drop below the legibility floor.

## Aspect-ratio behaviour

| Format | Behaviour |
|---|---|
| 9:16 | Vertical hierarchy or a bounded stage; never assume a fixed speaker split |
| 16:9 | Asymmetric split when a stable subject holds one side; otherwise a low wide overlay |
| 1:1 | Compact vertical hierarchy with fewer simultaneous UI objects |

## Approved Entities

This is AI Her Way's own editorial system. The palette and typography written into this file — Playfair Display and Montserrat, plus the ten-colour brand palette and its italic-accent, gold-hairline, and highlight-marker devices — ARE the approved, supplied brand system here. No other names, logos, products, vendors, or claims are approved by default; add only entities that are supplied or explicitly signed off for the active project.

## Do

- Hold one dominant idea per beat.
- Use the frontmatter tokens exactly.
- Study several source frames before placing overlays.
- Reserve captions and platform safety before graphics.
- Check at phone scale.

## Don't

- Don't assume footage or talking-head placement.
- Don't rebuild a reference product interface.
- Don't spend success green on decoration.
- Don't fill every open pocket.
- Don't quietly swap the display font.
- Don't reshape narrative content just to make the style land.

## Pre-render audit

- Type: Playfair Display loaded, Montserrat loaded, display/label hierarchy obvious, exactly one Playfair-italic accent word per headline.
- Palette: only the declared neutrals, the semantic success, and any signed-off project exceptions.
- Layout: the chosen mode matches the real frame, and every motion envelope stays safe.
- Captions: one line, safe lane, no collisions, hard cue exits.
- Motion: every cursor action has a visible consequence; no floaty fade sequences.
- Source: footage, copy, timing, audio, and approved identity all intact.
