# AI Her Way — Video Editing System

A public, versioned collection of Claude Skills for turning raw talking-head/WhatsApp footage into finished, on-brand reels. Built on [HyperFrames](https://hyperframes.heygen.com) (HTML-driven video composition + render). All four skills are original AI Her Way work — see [LICENSE](LICENSE) and each skill's own `LICENSE` file.

## Brand system (locked)

- **Typography:** Playfair Display (headlines, stats, pull quotes, italic accent) + Montserrat (body, labels, eyebrows). No exceptions.
- **Palette:** Espresso `#35241F` · Ink `#2B1E19` · Linen Cream `#F2EBDD` · Ivory `#FAF6EF` · Dusty Blue `#C4D6DA` · Stone `#C0CACE` · Sage `#AAB6A0` · Deep Olive `#46513D` · Walnut `#7B5A49` · Gold `#B08A62`.
- **Signature devices:** one Playfair-italic accent word per headline (Walnut on light / Dusty Blue on dark) · a 2px Gold hairline under headlines · highlight-marker color blocks · rationed torn-paper + washi tape.

Full spec: `C:\Users\nici\brand-design-system\AI-Her-Way-Social-Design-System.md` (source of truth — these skills are downstream of it, not the other way round). Each style skill also ships its own `assets/frame.md` token file (colours + typography) — edit that file (and swap the webfonts in `assets/fonts/`) to re-skin a skill to a different brand entirely; see "Adapting to a different brand" below.

## Skills in this repo — two different jobs, not four interchangeable options

| Skill | Job |
|---|---|
| `skills/edit-videos-my-way/` | **The editor.** Does the actual editing work: mines the transcript for the strongest hook, decides what gets cut/reordered/removed (fumbles, dead space, duplicated setup), plans the beat map and timestamped cuts, then picks which style skill below to invoke for the visual treatment. Run this first — it's the entry point, not an alternative to the other three. |
| `skills/quiet-editorial-ui/` | **A visual/caption style.** Calm, editorial software-interface look — restrained cards, progress paths, serif captions. Assumes the cut/hook/structure decisions are already made (by `edit-videos-my-way` or a manual edit) and only designs what sits on top of that edit. |
| `skills/hyperframes-tactile-collage/` | **A visual/caption style.** Warm paper/scrapbook collage look — ink marks, tape, cutout captions. Same assumption: styles an existing edit, doesn't create one. |
| `skills/cinematic-caption/` | **A visual/caption style.** Hero-word caption system — scoring, placement, and motion for large dynamic captions. Same assumption: styles an existing edit, doesn't create one. |

In short: **`edit-videos-my-way` does the editing fundamentals** (hooks, cuts, pacing, retention structure) that have nothing to do with captions, graphics, or colour. The other three only decide how the already-edited video *looks* — none of them will cut footage, restructure a transcript, or place a hook for you on their own.

## How they fit together

`edit-videos-my-way` is the entry point for a new edit: it reads the raw footage/transcript, decides the hook and beat structure, plans the cuts, then invokes one of the three style skills for the visual treatment (see `taste-profile.md`'s "Primary Aesthetic Anchors"). All three style skills were originally forked from third-party HyperFrames skills, then rewritten from scratch — original prose, renamed code structure, proprietary license — into AI Her Way's own systems; nothing in this repo is a third-party reskin.

## Works with Claude Code and OpenAI-compatible agents

Every skill ships an `agents/openai.yaml` alongside its `SKILL.md`, so the same skill folder is usable from either Claude Code (`SKILL.md`) or Codex/OpenAI-style agent tooling (`agents/openai.yaml`) without any changes.

## Adapting to a different brand

Two ways to do it:

1. **Ask the agent to do it.** Install the skills, then before your first edit say something like: *"Before we use these skills, adapt them to my own brand — here's my brand kit / mood board / reference images."* Point it at your brand doc or attach reference images; the agent edits each style skill's `assets/frame.md` token values (and swaps the bundled webfonts) to match.
2. **Do it yourself.** Open `assets/frame.md` in any style skill, change the hex values and font names to your own brand, and swap the webfont files in `assets/fonts/` for your own (same filenames). The motion/layout logic underneath doesn't change — only the skin does.

## Installing locally

Each skill directory should be symlinked or copied into `~/.claude/skills/<name>/` (Claude Code) or your agent's equivalent skills directory, to be auto-discovered.
