# AI Her Way — Video Editing System

A private, versioned collection of Claude Skills for turning raw talking-head/WhatsApp footage into finished, on-brand reels. Built on [HyperFrames](https://hyperframes.heygen.com) (HTML-driven video composition + render).

## Brand system (locked)

- **Typography:** Playfair Display (headlines, stats, pull quotes, italic accent) + Montserrat (body, labels, eyebrows). No exceptions.
- **Palette:** Espresso `#35241F` · Ink `#2B1E19` · Linen Cream `#F2EBDD` · Ivory `#FAF6EF` · Dusty Blue `#C4D6DA` · Stone `#C0CACE` · Sage `#AAB6A0` · Deep Olive `#46513D` · Walnut `#7B5A49` · Gold `#B08A62`.
- **Signature devices:** one Playfair-italic accent word per headline (Walnut on light / Dusty Blue on dark) · a 2px Gold hairline under headlines · highlight-marker color blocks · rationed torn-paper + washi tape.

Full spec: `C:\Users\nici\brand-design-system\AI-Her-Way-Social-Design-System.md` (source of truth — these skills are downstream of it, not the other way round).

## Skills in this repo

| Skill | Purpose |
|---|---|
| `skills/edit-videos-my-way/` | The orchestrating skill — turns a raw recording + transcript into a hook/beat-map/caption/CTA creative treatment, then a real HyperFrames render. Contains `references/taste-profile.md`, the reference-derived creative-defaults doc (12-reel study, hook patterns, structural rules). |
| `skills/quiet-editorial-ui/` | Calm, editorial software-interface look — frosted-glass panels, serif section cards, background rack-focus blur. Brand-tuned. |
| `skills/hyperframes-tactile-collage/` | Warm paper/scrapbook collage look — ink outlines, torn paper, hand-drawn gold accents. Brand-tuned. |
| `skills/cinematic-caption/` | Hero-word caption design system — scoring, placement, motion, sound-design mapping for dynamic captions. Brand-pinned (fonts/accent colors), methodology otherwise untouched. |

## How they fit together

`edit-videos-my-way` is the entry point for a new edit: it reads the raw footage/transcript, decides the hook and beat structure, and picks which of the three style skills to invoke for the actual visual treatment (see `taste-profile.md`'s "Primary Aesthetic Anchors"). The three style skills are general-purpose HyperFrames skills (not specific to this project) that have been forked here specifically to pin their colors/fonts to AI Her Way's brand — their structural/motion logic is otherwise the original, unmodified methodology.

## Installing locally

Each skill directory should be symlinked or copied into `~/.claude/skills/<name>/` to be auto-discovered by Claude Code.
