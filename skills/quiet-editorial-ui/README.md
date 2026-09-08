# Quiet Editorial UI

AI Her Way's quiet editorial system for HyperFrames videos — a restrained, serif-led software look for graphics that sit beside or over footage without ever fighting for attention.

It works with talking heads, B-roll, screen recordings, mixed media, empty-space overlays, direct-to-footage graphics, and full-frame motion compositions. It does not change the project's story, timing, footage, audio, or approved identity.

## What you need

- A local [HyperFrames](https://github.com/heygen-com/hyperframes) project
- An AI coding agent that supports installable `SKILL.md` skills
- Source footage or an existing HyperFrames composition to style

## Install

This skill is distributed to AI Her Way Pro Hub members. Copy the `quiet-editorial-ui` folder into your agent's skills directory, then restart the agent so it discovers the skill.

- **Claude Code:** copy it into `~/.claude/skills/quiet-editorial-ui`
- **Other compatible agents:** copy it into that agent's skills directory (commonly `~/.agents/skills/quiet-editorial-ui`)

## Use

Invoke it directly:

```text
$quiet-editorial-ui [HyperFrames project path]
```

Or just ask:

- "Apply Quiet Editorial UI to this HyperFrames project."
- "Give this a refined editorial software look."
- "Add restrained serif overlays in the negative space around the footage."

The skill automatically chooses between three layout modes:

- `available-area` for unused regions around footage
- `direct-overlay` for graphics placed over footage
- `full-frame` when graphics own the complete canvas

## Visual system

- Playfair Display (regular and italic) for editorial display typography
- Montserrat for interface copy, labels, body text, and captions
- Warm near-white surfaces, ink-dark text, thin rules, subtle depth, and generous negative space
- Sage green reserved for genuine completion or confirmation
- Cursor-led interactions, selections, document objects, cards, and progress paths — all pinned to AI Her Way's locked Social/Reels brand system

## Captions and safety

The skill includes reusable caption and safe-zone components (`ahw-editorial-*`) with:

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
- `assets/examples/` — golden frames illustrating each layout mode
- `scripts/` — font preflight and package validation

## Validate

```bash
node scripts/validate-package.mjs .
```

## License

Proprietary to AI Her Way. See [LICENSE](LICENSE). Provided to Pro Hub members for their own use; not for redistribution or resale.
