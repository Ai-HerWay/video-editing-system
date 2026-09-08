---
name: Tactile Paper Collage
styleAuthority: presentation
---

# Design specification

## Intent

Build each narrative beat as a single readable physical metaphor cut from paper,
marked in ink, and set in restrained editorial type. Keep supplied media
recognisable and leave approved identity assets intact.

## Semantic colour roles

```css
:root {
  --ahw-ground: #F2EBDD;
  --ahw-card: #FAF6EF;
  --ahw-ink: #2B1E19;
  --ahw-accent: #C4D6DA;
  --ahw-flag: #7B5A49;
  --ahw-spark: #B08A62;
  --ahw-seal: #AAB6A0;
  --ahw-cast: rgba(43, 30, 25, 0.22);
}
```

Role guide:

- `--ahw-ground`: the warm continuous paper the beat sits on.
- `--ahw-card`: lighter foreground paper for cards, notes, and documents.
- `--ahw-ink`: near-black structure and primary copy.
- `--ahw-accent`: the main explanatory colour.
- `--ahw-flag`: contradiction, warning, or urgency.
- `--ahw-spark`: emphasis and discovery.
- `--ahw-seal`: completion, approval, or handoff.
- `--ahw-cast`: the shared paper-lift shadow.

These are AI Her Way's locked brand colours (see Approved Entities below), not
neutral defaults — keep their contrast and their semantic roles intact when you
use them. Keep the ground and card surfaces warm enough to read as physical
paper and dark enough to hold their edges against pure-white platform chrome.

## Type

- Handwritten emphasis: Permanent Marker, short phrases only. Ink these in Gold
  `#B08A62` (not plain `--ahw-ink`) to match the brand's "hand-drawn in gold"
  signature device.
- Operational copy and captions: Montserrat Bold.
- Display statements: Playfair Display (bold/black weight) — the brand's locked
  headline face for every headline, stat, pull quote, and italic accent, with no
  exceptions.

## Geometry

- Ink outlines: 3-6px at a 1080px short edge.
- Resting rotation: normally within `-5deg` to `5deg`.
- Paper shadows: one consistent down-right direction.
- Texture: low-contrast grain, dots, fibres, or ruled lines; never over
  load-bearing copy.
- One hero object per beat; supporting objects must earn their place by showing
  sequence, evidence, grouping, or state.

## Layout modes

- `behind-subject`: graphic plates below a transparent speaker, captions above.
- `direct-overlay`: bounded paper objects in stable negative space over intact
  footage.
- `full-frame`: the paper world owns the beat when footage is absent or unhelpful.

## Approved entities

AI Her Way's palette and typography ARE the approved, supplied brand system for
this project. Typography: Playfair Display (every headline, stat, pull quote,
italic accent) and Montserrat (body copy, small-caps eyebrows, labels, footers,
list items) — no exceptions. Palette: Espresso `#35241F`, Ink `#2B1E19`, Linen
Cream `#F2EBDD`, Ivory `#FAF6EF`, Dusty Blue `#C4D6DA`, Stone `#C0CACE`, Sage
`#AAB6A0`, Deep Olive `#46513D`, Walnut `#7B5A49`, and Gold `#B08A62`. These are
the retained brand colours and identity constraints for all implementation here.

## Motion

Every move should read as a paper action: placed, drawn, passed, opened,
stacked, checked, or stamped. Keep entrances short, hierarchy obvious, and all
render-critical motion deterministic and seek-safe.
