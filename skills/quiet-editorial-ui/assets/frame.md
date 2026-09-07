---
version: 1
name: Quiet Editorial UI
description: >
  The AI Her Way editorial frame system pairing literary Playfair Display typography with precise Montserrat UI
  structure, warm cream surfaces, restrained depth, and cause-and-effect motion.
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

## Overview

Build calm, editorial frames from literary display type, precise interface copy, warm paper-like
surfaces, and observable state changes. The frame should feel authored rather than decorated.

## Typography

- Use `Playfair Display` for every headline, stat, pull quote, and italic accent, and Montserrat for all operational language, small-caps eyebrows, labels, footers, and list items.
- Keep Playfair Display at weight 400. Use italic once per beat at most.
- Set labels and small-caps eyebrows in Montserrat 700 uppercase with generous tracking, coloured Walnut (`accent-light`).
- Make the display element at least three times the size of the nearest label.
- Keep load-bearing UI copy at least 20px at 1080px short-edge resolution.
- Keep captions at least 96px at 1080px portrait width and on one line.

### Italic accent

- Set exactly one Playfair-italic word per headline as the accent. This single italic word is the most recognisable element of the brand — never lose it in a retrofit.
- Colour the accent word Walnut (`accent-light`, #7B5A49) on light grounds and Dusty Blue (`accent-dark`, #C4D6DA) on dark grounds.
- Do not italicise more than one word per headline, and do not use the accent colour for anything other than the accent word.

## Color

- Use `canvas` (Linen Cream) as the warm graphic ground and `ink` (#2B1E19) for hierarchy.
- Use `surface-active` (Ivory) for foreground cards and `surface-quiet` (Linen Cream) for supporting chrome.
- Use `success` (Sage) only for complete, confirmed, ready, reassurance, or passed states, and `success-deep` (Deep Olive) for the strongest confirmed state.
- Use `hairline` (Gold, #B08A62) for the thin ~2px rule sitting directly under a headline, and for rare hand-drawn or script accents only.
- Use the italic accent colour — Walnut (`accent-light`) on light grounds, Dusty Blue (`accent-dark`) on dark grounds — only on the single italic accent word.
- A highlight marker is permitted: one word may sit on a colour block (Dusty Blue, Espresso, Sage, or Walnut). Use at most one per beat.
- These are the brand's signature devices, not free decoration — do not add any further decorative accent beyond the italic accent, the gold hairline, and one highlight marker.

## Depth and shape

- Use 2px-equivalent borders, restrained shadows, and 16–26px-equivalent radii.
- Use full pills only for compact labels, actions, or status.
- Avoid glass blur, gradients, thick outlines, neon, heavy glow, and decorative particles.
- Let the warm canvas show through; do not tile the frame with equal-weight cards.

## Frame treatments

### Available-area stage

Anchor one editorial headline and one operational object inside a stable negative-space region.
Keep the source subject and source UI untouched. Allow cursor travel only inside the verified region.

### Direct overlay

Place the message over footage only after mapping faces, source text, logos, and motion. Use a
localized warm-white surface on busy footage. Use unboxed ink only when contrast is stable across
the full beat.

### Full-frame editorial

Use the warm canvas, one dominant headline, and one secondary object such as a document card,
window, selection list, or progress path. Preserve substantial negative space.

### Progress and completion

Use an ink hairline, compact numbered nodes, and a single green completed state. Animate one object
continuously through the path instead of replacing it with disconnected cards.

### Closing action

Use a large serif phrase, one concise operational object, and a compact action or status. Do not
introduce new claims or product identity.

## Motion

- Reveal label, hero, then operational object.
- Use 12–42px translation over 0.35–0.62s for primary entrances.
- Use a cursor only when it selects, moves, groups, or confirms something.
- Preserve spatial continuity between states.
- Keep exits short and decisive.
- Use opacity as support, never as the sole choreography.

## Captions

- Use Montserrat 700, 2–4 words, one line, and no punctuation.
- Permit one Playfair Display italic emphasis word when editorially meaningful, coloured Walnut on light grounds or Dusty Blue on dark grounds.
- Reserve the caption lane before composing overlays.
- Use the clean treatment on quiet grounds and the card treatment on busy footage.
- Move the lane around faces and source UI; never reduce below the legibility floor.

## Aspect-ratio behavior

| Format | Behavior |
|---|---|
| 9:16 | Use a vertical hierarchy or bounded stage; do not assume a fixed speaker split |
| 16:9 | Use an asymmetric split when a stable subject occupies one side; otherwise use a low wide overlay |
| 1:1 | Use a compact vertical hierarchy and fewer simultaneous UI objects |

## Approved Entities

This is a project-specific fork for AI Her Way. The AI Her Way palette and typography specified in
this file — Playfair Display and Montserrat, and the ten-colour brand palette with its italic-accent,
gold-hairline, and highlight-marker devices — ARE the approved, supplied brand system for this
project. No other names, logos, products, vendors, or claims are approved by default; add only
further entities supplied or explicitly approved for the active project.

## Do

- Preserve one dominant idea per beat.
- Use exact tokens from the frontmatter.
- Inspect multiple source frames before placing overlays.
- Reserve captions and platform safety before graphics.
- Verify at phone scale.

## Don't

- Do not assume footage or talking-head placement.
- Do not recreate a reference product interface.
- Do not use success green decoratively.
- Do not fill every open area.
- Do not silently substitute the display font.
- Do not change narrative content to make the style easier to apply.

## Pre-render audit

- Typography: Playfair Display loaded; Montserrat loaded; display/label hierarchy is obvious; exactly one Playfair-italic accent word per headline.
- Palette: only declared neutrals, semantic success, and approved project exceptions.
- Layout: selected mode matches the actual frame and all motion envelopes remain safe.
- Captions: one line, safe lane, no collisions, hard cue exits.
- Motion: every cursor action has a visible consequence; no floaty fade sequence.
- Source: footage, copy, timing, audio, and approved identity remain intact.
