---
name: Tactile Paper Collage
styleAuthority: presentation
---

# Design specification

## Intent

Turn each narrative beat into one legible physical metaphor assembled from paper, ink, and restrained editorial typography. Keep supplied media recognizable and preserve approved identity assets.

## Semantic color roles

```css
:root {
  --tpc-paper: #F2EBDD;
  --tpc-sheet: #FAF6EF;
  --tpc-ink: #2B1E19;
  --tpc-primary: #C4D6DA;
  --tpc-signal: #7B5A49;
  --tpc-spark: #B08A62;
  --tpc-resolve: #AAB6A0;
  --tpc-shadow: rgba(43, 30, 25, 0.22);
}
```

These are AI Her Way's locked brand colors (see Approved Entities below), not neutral defaults — retain the contrast and semantic roles when using them. Keep paper and sheet surfaces warm enough to read as physical media and dark enough against pure white platform chrome.

## Type

- Handwritten emphasis: Permanent Marker, short phrases only. Render this handwritten emphasis in Gold `#B08A62` ink (not plain black/`--tpc-ink`) to match the brand's "hand-drawn in gold" signature device.
- Operational copy and captions: Montserrat Bold.
- Display statements: Playfair Display (bold/black weight) — the brand's locked headline face, used for every headline, stat, pull quote, and italic accent with no exceptions.

## Geometry

- Ink outlines: 3-6px at a 1080px short edge.
- Resting rotation: normally within `-5deg` to `5deg`.
- Paper shadows: one consistent down-right direction.
- Texture: low-contrast grain, dots, fibers, or ruled lines; never over load-bearing copy.
- One hero object per beat; supporting objects must explain sequence, evidence, grouping, or state.

## Layout modes

- `behind-subject`: graphic plates below a transparent speaker and captions above.
- `direct-overlay`: bounded paper objects in stable negative space over intact footage.
- `full-frame`: paper world owns the beat when footage is absent or unhelpful.

## Approved entities

AI Her Way's palette and typography ARE the approved, supplied brand system for this project. Typography: Playfair Display (every headline, stat, pull quote, italic accent) and Montserrat (body copy, small-caps eyebrows, labels, footers, list items) — no exceptions. Palette: Espresso `#35241F`, Ink `#2B1E19`, Linen Cream `#F2EBDD`, Ivory `#FAF6EF`, Dusty Blue `#C4D6DA`, Stone `#C0CACE`, Sage `#AAB6A0`, Deep Olive `#46513D`, Walnut `#7B5A49`, and Gold `#B08A62`. These are the retained brand colours and identity constraints for all implementation here.

## Motion

Use placed, drawn, passed, opened, stacked, checked, and stamped actions. Keep entrances short, hierarchy obvious, and all render-critical motion deterministic and seek-safe.
