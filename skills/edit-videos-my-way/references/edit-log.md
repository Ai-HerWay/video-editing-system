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

### 2026-09-29 — V7 final signature approval
- **verdict:** "yes so much better love it! lets code this all so its repeatable skill"
- **approved:** V7 visual treatment, gentle camera variation, raised captions, sticker pops and recorded pencil sounds. Three drawing cues; one continuous long-arrow sound.
- **implementation:** Portable editable starter, local-input setup script and bundled approved CC0 pencil excerpts; style v1.2.0.
- **reference:** Packaged approved-pilot-v7.mp4. Earlier V5 sound is superseded; no new performance data reported.

### 2026-09-29 — Drawing sound correction V7
- **verdict:** "It sounds like someone spraying rather than drawing." "Otherwise, that's looking really good."
- **learnings:** Reject the procedural pencil timbre while preserving the visual/camera treatment and three drawing cue positions. Use dry recorded pencil strokes. V5 approval is qualified by this later sound correction.
- **tried:** CC0 sketchbook pencil foley by thisisjoewells, Freesound 463848; two short excerpts and one continuous longer excerpt. Replacement listening verdict pending.
- **promoted:** Sound-direction correction, style v1.1.1.

### 2026-09-29 — Signature camera refinement V6
- **mode:** Hybrid; same 9.6-second source and V5 sound
- **requested:** "slow zoom ins" and "1-2 second cuts" in some places, "not overly", for a cinematic effect.
- **tried:** Gentle presenter push-ins, tighter crop at 1.26 s, wider crop on return from diagram; overlays stay fixed.
- **verdict:** Direction requested; rendered V6 approval not yet recorded.
- **learnings:** Selective camera variation, not constant metronomic cutting. Single-source crops are not genuine alternate angles.
- **promoted:** Camera preference in signature style v1.1.0; V5 remains the approved sample.


### 2026-09-29 — Signature style pilot V5
- **source:** How to Build your first OS, source range 28.2–37.8 s
- **mode:** Hybrid
- **anchor/skin:** AI Her Way signature illustrated editorial style
- **hook pattern:** Contrast — separate files to one connected system
- **length / aspect:** 9.6 s / 9:16, 1080 × 1920 at 30 fps
- **CTA:** Payoff close; style test
- **tried:** Hand-drawn spring stickers; paper diagram; raised Advercase captions; action-matched sound.
- **verdict:** User: "yes this is great!" after V5 preview. Requested reusable skills in GitHub afterwards.
- **performance:** Not recorded
- **learnings:** V4's nine drawing cues were reduced to three: two connectors and one continuous long arrow. Keep pops and other accepted effects. Typewriter for featured typed questions/quotes is a separately confirmed preference, not demonstrated in this sample. The three-cue count is pilot-specific.
- **promoted:** Yes — current default is `ai-her-way-signature-reels` v1.0.0, with a packaged approved sample.


### 2026-09-19 — skills-vs-os (Her Way Cut pilot #1)
- **project dir:** `C:\Users\nici\brand-design-system\videos\skills-vs-os`
- **source:** raw WhatsApp clip R05 (`4.24.41 PM.mp4`, 93.3s) — "custom GPT/Claude skill vs AI operating system"
- **mode:** Repurpose
- **anchor/skin:** The Her Way Cut spec v1 (first full outing) — quiet-editorial panels + marginalia + gold structure
- **hook pattern:** borrowed comment/question — client-call question card supplied verbatim by Nici
- **length / aspect:** 89.6s / 9:16 1080×1920
- **CTA:** COMMENT "OS SYSTEM" → full 90-min workshop ⚠ keyword heard as "O P system"/"up system" by whisper — MUST be confirmed by Nici before posting
- **tried:** (1) two-panel skill-vs-OS comparison as the persistent spine, with the skill panel collapsing to compact state after its section; (2) karaoke registers (Montserrat meta + Playfair-italic accent words) with a soft scrim, single home at 67%; (3) caption suppression wherever a designed element carries the words (✗-rows section, heroes, marginalia echo, CTA) — the reel-B "tags are the captions" move; (4) marginalia: "≠ staff", "you have to notice the *noticing*", greyed "noticed. nothing happens."; (5) two hero lockups ("not staff." / "it's not smarter → connected." with gold underline draw + ding); (6) espresso veils top/bottom for contrast + cinema; (7) step punch-in hiding the splice at 39.28s; (8) typed CTA chip in the top band after the title retires
- **verdict:** v1 draft — Nici (2026-09-19, verbatim): "tiny edits - can we lower exposure, we can drop exposure and up clarity tiny bit more and slight more coffee wash - can we move the captions down a bit so they arent so high - and are you using advercase and one word at a time is usually better". Applied in v2: darker/clearer/coffee grade; captions 67%→71%; captions switched to Advercase, ONE WORD AT A TIME; hero lockup big lines switched to Advercase (Playfair keeps titles/panels).
- **performance:** not recorded
- **learnings:** close-framed footage forces adaptive captions DOWN to the 67% chin band and makes mid-frame caption homes unusable — check subject scale before planning caption zones; designed panels can replace captions entirely for list-y sections; contrast checker demands veils/scrims over bright footage — build them in from the start
- **promoted:** no (pending verdict)

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
