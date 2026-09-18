# Edit Log — Per-Reel Outcomes and Learnings

This is the memory that makes the taste profile compound instead of reset. `references/taste-profile.md` holds the *general* creative defaults; this file holds the *specific* history — every finished edit, what was tried, how the user reacted, and what that should change next time.

## How to use this log

**When starting a new edit:** read the most recent 5-10 entries after reading the taste profile. Recent verdicts override older habits — if the user rejected a device two edits ago, do not reach for it again by default.

**When finishing an edit:** append a new entry at the top of Entries using the template below. Fill in every field you actually know; write `not recorded` rather than guessing. Never invent a verdict the user did not give.

**When the user reacts to a cut** — approves, rejects, asks for a tweak, says "love this" or "too much" — update that edit's entry with the exact feedback the same session. Verbatim short quotes beat paraphrase.

**When a pattern recurs across 2-3 entries** (a device that keeps landing, a hook pattern that keeps getting cut), propose promoting it into `references/taste-profile.md` as a general default, and note the promotion in the entry's `promoted` field. The log is the evidence base; the taste profile is the distilled law.

**If performance data arrives later** (views, saves, comments, DM keyword count), backfill the `performance` field — this is the only field expected to be edited long after the entry is written.

## Entry template

```markdown
### YYYY-MM-DD — <project-name>
- **project dir:** <path>
- **source:** <raw footage / script / transcript origin>
- **mode:** Repurpose | Explain | Hybrid
- **anchor/skin:** <Primary Aesthetic Anchor or style skill used>
- **hook pattern:** <from Hook Pattern Library>
- **length / aspect:** <e.g. 48s / 9:16>
- **CTA:** <keyword or "payoff-close">
- **tried:** <the 1-3 notable creative decisions in this edit>
- **verdict:** <user's reaction, verbatim where possible; or "not recorded">
- **performance:** <platform numbers once known; or "not recorded">
- **learnings:** <what to repeat / avoid next time>
- **promoted:** <yes → what moved into taste-profile.md; or "no">
```

## Entries

### 2026-09-11 — style-explainers
- **project dir:** `C:\Users\nici\brand-design-system\videos\style-explainers`
- **source:** not recorded (outputs only in folder: `2d-illustrator.mp4`, `hand-drawn.mp4`)
- **mode:** Explain
- **anchor/skin:** two style variants rendered — 2D illustrator and hand-drawn
- **hook pattern:** not recorded
- **length / aspect:** not recorded
- **CTA:** not recorded
- **tried:** same explainer content rendered in two visual styles for comparison
- **verdict:** not recorded — backfill welcome
- **performance:** not recorded
- **learnings:** not recorded
- **promoted:** no

### 2026-09-11 — pro-hub-announcement
- **project dir:** `C:\Users\nici\brand-design-system\videos\pro-hub-announcement`
- **source:** scripted VO (`SCRIPT.md` → `audio.mp3`), not repurposed footage
- **mode:** Explain
- **anchor/skin:** not recorded
- **hook pattern:** not recorded
- **length / aspect:** not recorded
- **CTA:** not recorded
- **tried:** full local pipeline — script → generated VO → 16 kHz transcription pass (`audio16k.wav`, `transcript_raw.json`) → SFX bed built from key/pop one-shots via an ffmpeg filter script (`pha_sfx_filter.txt` → `sfx-bed.wav`); an intermediate `output-notion.mp4` cut preceded the final `output.mp4` (rendered 2 days after the first pass)
- **verdict:** not recorded — backfill welcome
- **performance:** not recorded
- **learnings:** the transcribe-then-SFX-bed pipeline worked end to end and is reusable for scripted announcements
- **promoted:** no

### 2026-09-08 — levels four-style bake-off
- **project dirs:** `videos\levels-default`, `videos\levels-editorial`, `videos\levels-tactile`, `videos\levels-cinematic`
- **source:** the "AI levels" explainer content (see also `videos\ai-levels-explainer`, 2026-09-07)
- **mode:** Explain
- **anchor/skin:** the same content rendered four ways — default, quiet-editorial, tactile-collage, cinematic-caption — as a side-by-side test of the style skills
- **hook pattern:** not recorded
- **length / aspect:** not recorded
- **CTA:** not recorded
- **tried:** first full comparison of all three brand-tuned style skills against a default treatment on identical content
- **verdict:** not recorded — which style won this bake-off is the single most valuable missing datum in this log; backfill welcome
- **performance:** not recorded
- **learnings:** not recorded
- **promoted:** no
