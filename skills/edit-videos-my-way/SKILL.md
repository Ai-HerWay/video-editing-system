---
name: edit-videos-my-way
description: Turn long-form recordings, masterclasses, interviews, podcasts, webinars, and their transcripts into high-retention short-form videos, direct-to-camera yap-style social clips, and accessible branded animated explainers. Use when Codex needs to mine strong hooks, restructure truthful source audio, remove fumbles and dead space, create timestamped cut plans, edit source footage, write captions, plan clicks/sound bites/image flashes/stickers/emoji/punch-ins every 2-3 seconds, create Ai Her Way editorial motion-collage graphics, generate supporting footage or voice with Higgsfield, or refine a video style from references the user loves. Supports MP4/MOV audio-video, SRT/VTT/TXT transcripts, 9:16 reels, 1:1 posts, and 16:9 explainers.
---

# Edit Videos My Way

Act as a sharp creative director, story producer, and hands-on editor. Preserve the user's intelligence and natural voice while making the work fast, visually addictive, emotionally clear, and beautiful rather than frantic or gimmicky.

## Start Here

1. Read `references/taste-profile.md` for the current creative defaults. It is derived from a frame-by-frame study of 12 curated high-performing reference reels and names three Primary Aesthetic Anchors, a Hook Pattern Library, a Caption System Spec, and CTA Mechanics — treat these as the default toolkit rather than inventing generic social-video conventions from scratch.
2. Pick one Primary Aesthetic Anchor as the skin and one Hook Pattern for the opening before drafting a beat map. Name both choices explicitly in the creative treatment. Do not mix skins within one edit (e.g. frosted-glass panels with torn-paper stickers).
3. If the user provides new reference videos or describes a new preference, compare them with the profile and propose precise profile updates to `references/taste-profile.md`. Treat explicit current-turn preferences as authoritative over the file.
4. Normalize transcript files with `scripts/normalize_transcript.py` when useful.
5. Choose one mode:
   - **Repurpose:** find and edit the best moments from a real recording.
   - **Explain:** turn one core concept into a standalone animated explainer.
   - **Hybrid:** lead with the real speaker and use generated or motion-designed visuals to clarify the idea.
6. Read `references/edit-playbook.md` for the chosen mode. For Repurpose mode, also read `references/retention-repurposer.md`. For Explain mode, also read `references/motion-design-system.md`. Follow the mode-specific reference as the stricter specification.
7. Read `references/higgsfield-workflow.md` before using Higgsfield.
8. Produce an approval-friendly creative treatment before spending credits or rendering a large batch.

If only a transcript is available, create a complete editorial plan but label all timestamps as transcript-derived or unavailable. Never pretend a text transcript is enough to make frame-accurate cuts.

## Analyse the Source

Build a concept map before selecting clips:

- core promise and audience transformation
- 3-7 signature ideas or frameworks
- surprising claims, reversals, confessions, tensions, stories, evidence, quotable lines, and practical steps
- moments that sound uniquely like the speaker rather than generic advice
- prerequisites that make a clip incomprehensible when removed

Score each candidate from 1-5 on:

- hook strength
- standalone clarity
- emotional or intellectual charge
- specificity
- usefulness
- visual potential
- brand fit

Prefer moments with a strong first sentence or a clean preceding setup. Do not select a bland fragment merely because it is short.

## Design the Output

For each proposed video, deliver:

1. **Title and thesis** - one idea only.
2. **Audience and job** - why someone would stop and what changes for them.
3. **Hook options** - spoken, on-screen, and visual, drawn from the Hook Pattern Library in `references/taste-profile.md` (versus/comparison, cold-open narrative, borrowed comment, full-payload preview, contrarian claim, prop-driven).
4. **Exact source range** - start/end timestamps plus transcript excerpt when available.
5. **Paper edit** - exact spoken words retained, removed, or reordered, with a source-to-edit audio move map. Clearly disclose reordered speech.
6. **Beat map** - time, picture, crop/motion, on-screen text, sound, attention event, and purpose.
7. **Asset list** - source footage, screenshots, diagrams, generated shots, music, sound cues, and brand elements.
8. **Higgsfield prompts** - only for shots that benefit from generation.
9. **Caption and CTA** - two-register captions per the Caption System Spec, and a CTA per the CTA Mechanics in `references/taste-profile.md`; natural, specific, and proportionate to the content.
10. **Render specs** - duration, aspect ratio, resolution, caption treatment, and audio target.

Use JSON when an edit will be rendered or validated. Follow `references/edit-plan-schema.md`, then run:

```bash
python3 scripts/validate_edit_plan.py edit-plan.json
```

## Retention Rules

- Build a **persistent visual spine** for the whole runtime — a held prop, a locked numbered-chip HUD, a floating title card, frosted-glass panels — rather than relying on the talking head alone to carry attention. Every reference reel studied keeps one recurring overlay element alive throughout; cuts and punch-ins happen around it, not instead of it.
- Create a meaningful sensory or information change every 2-3 seconds. A change can be a cut, punch-in, composition change, caption switch, floating proof-card swap, micro sound bite, image flash, screenshot, sticker, diagram movement, silence, or deliberate performance beat. Do not make every change equally loud — alternate intensity to create rhythm.
- The first 1-3 seconds must front-load the payoff, not just tension: preview the full value contract (a chip grid of all N items, a stated count, a versus framing) or open on a cold-open pattern-interrupt (see `references/taste-profile.md` Hook Pattern Library). Never open on a slow verbal windup.
- Substitute claims with **proof** wherever the footage allows it: real screen-recordings, an annotated screenshot (arrows/boxes/circles), an actual typed prompt, a split-screen before/after, a real metric. Proof beats promise in every reference reel studied.
- Remove throat-clearing, duplicated setup, filler, long pauses, and low-value qualifiers without distorting meaning. Keep micro-pauses that make the speaker sound human and credible.
- Caption in **two registers**, per the Caption System Spec in `references/taste-profile.md`: a plain undesigned meta layer (title card, karaoke word-by-word) plus a styled content layer that carries the chosen aesthetic anchor's skin. Keep most caption cards to 2-7 words; never let captions dump the transcript.
- Change visuals at the moment an idea changes, not arbitrarily on a metronome.
- Use silence and a held shot only when intentional; document the reason.
- Use stickers, floating cards, and graphic devices as purposeful proof, labels, or visual shorthand from the Visual/Animation Device Library — not random decoration, generic stock, AI spectacle, or template-like motivational editing.
- If the content has a countable structure (a list, a set of steps, a set of tools), state the count in the hook and pay it off progressively with a visible remaining-count device (a chip grid, a highlighted numbered list) — this is the strongest completion-loop mechanic observed across the reference set.
- Close on a single short keyword comment-CTA ("Skill," "Repo," "+") held on screen for the final 2-3 seconds, unless the piece is authority/portfolio-building, in which case end on the payoff itself. See CTA Mechanics in `references/taste-profile.md`.
- Never fabricate a quote, outcome, anecdote, or spoken sentence.

## Repurpose Mode

Read `references/retention-repurposer.md` and treat it as required.

Mine the entire source for the strongest complete hook, even when it appears later. Open with that line when it truthfully represents the clip, then backfill only the context needed to understand it. Remove fumbles, filler, duplicated thoughts, dead pauses, and low-value transitions. Reorder complete clauses or sentences for clarity and retention; use J-cuts, L-cuts, jump cuts, B-roll, image flashes, captions, stickers, emoji, and sound accents to hide seams. Never splice words into a statement the speaker did not make or change causality, certainty, chronology, or meaning.

Give every beat an explicit `attention_event`. Default to a new event every 2-3 seconds, with an opening event in the first second. Vary the interrupt type and intensity so the edit feels playful and native to social video rather than mechanically overloaded.

Create a ranked clip slate before rendering. Default slate:

- 3 short clips at 20-35 seconds
- 2 medium clips at 35-60 seconds
- 1 deeper clip at 60-90 seconds

Adapt the mix to the source. Seek variety: contrarian insight, story, framework, practical step, and identity/emotion. When source video is provided, inspect audio and framing as well as transcript meaning.

For approved cuts, use `scripts/render_cut.py` for clean source assembly when appropriate. Use an NLE or equivalent workflow for complex layering, tracked graphics, multi-camera edits, or manual performance choices. Render a draft, watch it end-to-end, then revise pacing, captions, audio, and visual logic.

## Explain Mode

Read `references/motion-design-system.md` and treat it as required. Use the **Ai Her Way Editorial Motion Collage** system: calm editorial brand foundations, tactile paper-and-photo collage, bold type, stop-motion-inspired movement, cut-out objects, and controlled high-energy colour flashes. Keep it recognisably Ai Her Way rather than copying any single reference design.

Choose concepts that can be understood without the full masterclass. Build the explainer around:

1. a tension or misconception
2. a visual model or metaphor
3. the mechanism in 2-4 steps
4. one concrete example
5. a memorable conclusion

Use code-native motion graphics for exact diagrams, numbers, axes, typography, collage assembly, and accessibility-critical information. Use Higgsfield for cinematic metaphors, atmospheric transitions, illustrative scenarios, character-consistent sequences, animated textures, or motion derived from an approved style frame. Do not ask a generative video model to render important typography; overlay exact text in post.

Default length is 30-75 seconds for social and 60-180 seconds for a deeper explainer. Prefer hybrid explainers when the speaker's face and authority improve trust.

## Higgsfield Use

- Use the connected Higgsfield tools when generation or source analysis materially improves the result.
- Check the active workspace and balance before a large batch.
- Estimate video cost before submitting generations.
- Generate small proof-of-style shots first; do not spend credits on a full batch before the visual direction is accepted.
- Preserve real identity only with user-supplied references and explicit intent.
- Display completed generation jobs for review, then incorporate only approved assets.

## Finish and Review

Review every final cut against this checklist:

- hook lands within 1-3 seconds and previews the payoff or delivers a cold-open pattern-interrupt, not just a slow windup
- a persistent visual spine is identifiable across the whole runtime, not just talking-head + occasional cutaway
- one Primary Aesthetic Anchor is used consistently; skins are not mixed
- clip makes sense without the masterclass
- no factual or rhetorical distortion
- visual or sonic pattern changes roughly every 2-3 seconds
- claims are backed by visible proof (screen-recording, screenshot, real number) wherever the footage allows it
- captions run in two registers (plain meta layer + styled content layer) and are legible on a phone as an overlay, never a reserved band the composition avoids
- text/background pairs pass WCAG contrast guidance; meaning never depends on colour or sound alone
- no unsafe strobing, excessive flashing, or unreadably fast motion
- generated visuals clarify rather than decorate
- sound supports attention without overwhelming speech
- speaker still feels intelligent, warm, human, and recognisably themselves
- CTA is a single short held keyword (or, for authority/portfolio pieces, the payoff itself) and earns its place instead of being stapled on

Return the final media when rendering is possible. Otherwise return the edit decision list, asset pack, generation prompts, and exact next production action rather than implying the video has been edited.
