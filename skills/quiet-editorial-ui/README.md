# Quiet Editorial UI

An installable, brand-neutral design skill for applying a refined editorial software look to
HyperFrames projects.

It works with talking heads, B-roll, screen recordings, mixed media, empty-space overlays,
direct-to-footage graphics, and full-frame motion compositions. It does not change the project's
story, timing, footage, audio, or approved identity.

## Install

```bash
npx skills add audrey-560/quiet-editorial-ui
```

Or clone the repository into your agent's skills directory.

## Use

Invoke the skill directly:

```text
/quiet-editorial-ui [HyperFrames project path]
```

You can also ask naturally:

```text
Apply Quiet Editorial UI to this HyperFrames project.
```

The skill automatically chooses between three layout modes:

- `available-area` for unused regions around footage
- `direct-overlay` for graphics placed over footage
- `full-frame` when graphics own the complete canvas

## Visual system

- Playfair Display (regular and italic) for editorial display typography
- Montserrat for interface copy, labels, body text, and captions
- Warm near-white surfaces, black ink, thin rules, subtle depth, and generous negative space
- Green reserved for genuine completion or confirmation
- Cursor-led interactions, selections, document objects, cards, and progress paths

## Captions and safety

The skill includes reusable caption and safe-zone components with:

- Natural 2–4 word phrase grouping
- One visible line at a time
- Word-level timing and hard cue exits
- Face, mouth, logo, source-UI, and load-bearing-text avoidance
- Safe placement guidance for 9:16, 16:9, and 1:1 compositions
- An optional debug overlay for collision checks

## Fonts

Both fonts are bundled under the SIL Open Font License, so no user-supplied files are required. Before rendering, copy the bundled WOFF2 files from `assets/fonts/` into the composition at:

```text
public/fonts/PlayfairDisplay-var.woff2
public/fonts/PlayfairDisplay-Italic-var.woff2
public/fonts/Montserrat-var.woff2
```

The included preflight blocks rendering when any file is missing or invalid. See
[`references/font-setup.md`](references/font-setup.md) for setup details.

## Package contents

- `SKILL.md` — skill entrypoint and workflow
- `assets/frame.md` — machine-readable design specification
- `references/` — style, layout, caption, motion, font, and safe-zone guidance
- `assets/components/` — reusable caption and safety overlays
- `assets/examples/` — brand-neutral golden frames
- `scripts/` — font preflight and package validation

## Validate

```bash
node scripts/validate-package.mjs .
```
