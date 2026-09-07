# Tactile Paper Collage for HyperFrames

A portable AI skill for applying a warm, tactile paper-collage editing style to HyperFrames videos.

It turns narrative beats into paper cards, folders, taped photos, stamps, dotted routes, hand-drawn connectors, checklists, and document handoffs while preserving the source story, footage, timing, claims, and approved brand assets.

## Install

Clone the repository into the skills directory used by your AI coding agent.

### Codex and compatible agents

```bash
git clone https://github.com/audrey-560/hyperframes-tactile-collage.git \
  ~/.agents/skills/hyperframes-tactile-collage
```

### Claude Code

```bash
git clone https://github.com/audrey-560/hyperframes-tactile-collage.git \
  ~/.claude/skills/hyperframes-tactile-collage
```

Restart the agent after installation so it can discover the skill.

## Use

Invoke it directly:

```text
$hyperframes-tactile-collage
```

It also responds to requests such as:

- “Use a tactile paper collage edit.”
- “Make this feel like an animated scrapbook.”
- “Add mixed-media notebook graphics.”
- “Apply a paper-cutout editorial style.”

The skill supports graphics behind an existing transparent subject, direct overlays on intact footage, and full-frame collage scenes when no subject cutout is available.

## Validate

```bash
node scripts/validate-package.mjs .
```

The validator checks required files, bundled font data, portability, and source isolation.

## License

The skill instructions, scripts, templates, and components are available under the MIT License. Bundled fonts retain their original open-font licenses in `assets/fonts/`.
