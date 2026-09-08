# AI Her Way — Tactile Paper Collage

AI Her Way's tactile paper-collage system for HyperFrames videos. It gives a
composition the warm, hand-assembled look of the studio's editorial craft:
paper grounds, cut-out cards, taped photographs, ink marks, stamps, dotted
routes, checklists, and document handoffs — with movement that feels physically
placed rather than digitally slid.

The style dresses the narrative without rewriting it. The source story, footage,
timing, spoken claims, copy, and the AI Her Way brand palette and typefaces all
carry through untouched; the skill only decides how each beat is built in paper.

## Install

This skill is distributed to AI Her Way Pro Hub members. It is not a public
repository — install it by copying the skill folder into your agent's skills
directory.

### Claude Code

Copy the `hyperframes-tactile-collage` folder into your project (or user) skills
directory:

```text
.claude/skills/hyperframes-tactile-collage
```

### Codex and compatible agents

Copy the same folder into the skills directory your agent reads, for example:

```text
~/.agents/skills/hyperframes-tactile-collage
```

Restart the agent afterwards so it discovers the skill.

## Use

Invoke it directly:

```text
$hyperframes-tactile-collage
```

It also answers to natural requests such as:

- "Give this a tactile paper collage edit."
- "Make it feel like an animated scrapbook."
- "Add mixed-media notebook graphics."
- "Style this in the paper-cutout editorial look."

The skill works three ways: layered behind an existing transparent subject,
dropped as bounded objects over intact footage, or handed the whole frame when
no subject cutout exists.

## Validate

```bash
node scripts/validate-package.mjs .
```

The validator confirms the required files are present, the bundled font data is
intact, and nothing machine-specific has leaked into the package.

## Colour tokens

Surfaces and accents are driven by the `--ahw-*` custom properties defined in
`assets/frame.md` (`--ahw-ground`, `--ahw-card`, `--ahw-ink`, `--ahw-accent`,
`--ahw-flag`, `--ahw-spark`, `--ahw-seal`, `--ahw-cast`). These carry AI Her
Way's locked brand palette; keep their contrast and semantic roles when adapting
them per project.

## License

Proprietary to AI Her Way — see `LICENSE`. Bundled fonts keep their own
open-font licenses in `assets/fonts/`.
