---
name: cinematic-caption
description: Design cinematic, editorial captions inside a HyperFrames video rather than parking every line in a fixed subtitle bar. Promotes the words that actually carry a claim into large mixed-case hero moments, stacks each sentence in the order it is spoken, anchors type to the speaker, and layers depth, translucent glass fills, and sparing sound accents around the subject. Use for cinematic or editorial captions, dynamic real-estate and creator-reel captions, or any request to make a key word, number, place, or figure large, layered, animated, or wrapped around a person.
---

# Cinematic Caption

This is AI Her Way's house method for treating captions as part of the picture. Speech becomes a small run of designed editorial beats that sit inside the frame and move with the subject, not a bottom strip the eye ignores. Work as a caption designer first and a subtitle transcriber second: decide which handful of words deserve to become the image, and let everything else stay quiet.

Leave the underlying edit, footage, narration, music, and brand alone unless the request is explicitly to change them. You are dressing an existing composition, not rebuilding it.

Before you plan or touch a single cue, read `references/style-system.md` end to end — it holds the brand pins, the scoring rules, and the treatment catalogue. Once a passage carries three or more designed cues, also read `references/dynamic-layout-recipes.md` end to end, because the difficulty shifts from styling one moment to sequencing many.

## What you can be handed

Expect the active HyperFrames project, plus any mix of:

- source footage or an existing composition to caption;
- a transcript, an SRT/VTT file, or word-level timing JSON;
- a target time range;
- brand fonts, colours, or a tone note;
- optional asks for glow, inserted graphics, or sound effects.

Read `$ARGUMENTS` as the project pointer, media, range, and style steer. Fill in missing project facts yourself when it is safe to do so, and only stop to ask when a genuinely unknown choice would change the outcome.

## How to run the job

Work through this order. Earlier steps protect later ones, so do not skip ahead to markup.

**1 — Load the framework.** Read the active project's own instructions and the mandatory `hyperframes` skill. Pull in `talking-head-recut`, `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`, and `hyperframes-cli` where they exist. If you will add or alter audio, also load `media-use` and `hyperframes-audio`.

**2 — Read the composition before changing it.** Inspect the duration, dimensions, tracks, media paths, current type, palette, and motion sidecar. Note what is already there so you extend it rather than overwrite unrelated scenes.

**3 — Get word-level timing you can trust.** Prefer a transcript that already exists. If there is none, run the documented HyperFrames transcription workflow and keep the result as a project artifact. If a single long transcription pass drifts from what you can hear, re-transcribe short overlapping windows and align each window locally. Never stretch bad timings proportionally across the whole clip to make them "fit" — that hides the drift rather than fixing it.

**4 — Turn speech into scored cues.** Cut the transcript into semantic groups and the ordered fragments that display inside them. Give each cue a role and an emphasis level using `references/style-system.md`. For every hero candidate, run the score in that reference — semantic load, proof value, spoken stress, legibility — and write down the reason the winning word won. A word does not earn hero scale just for being a noun or looking good large.

**5 — Map the subject before you place type.** Sample each designed cue at its start, middle, and end. Record where the face, mouth, hair, shoulders, hands, any product, UI, and existing text travel across that span, and where the usable calm space sits. Pick a coherent run of subject-relative anchor zones from that map. Change layout between argument beats, but hold one steady anchor for fragments that belong to the same sentence or the same parallel list. When a cue will use a foreground cutout, additionally check the cutout's start time, frame rate, duration, scale, and crop against the base footage, and inspect moving hair, hands, and shoulders at several timestamps. If a faint doubled edge survives even with timing matched, rebuild the cutout from the original source pixels plus the matte alpha rather than compositing an independently compressed RGB copy.

**6 — Commit the design to a plan file.** Write `caption-design-plan.json` before implementation. Each cue records its timing, the exact displayed text, `semanticGroupId`, `orderIndex`, role, emphasis, `heroReason`, placement, `anchorZone`, `layoutState`, `buildMode`, `flowDirection`, optional `persistenceGroup`, `foregroundText`, `heroText`, `stackGap`, the subject motion envelope, the depth strategy, `fillSource`, palette, `occlusionBudget`, motion preset, optional graphic support, and optional audio accent. The schema lives in `references/style-system.md`.

**7 — Reuse before you rebuild.** Search the local HyperFrames catalogue for caption blocks that fit before hand-authoring anything. Adapt a strong match to this composition and this brand. Never lift another creator's logo, identity, or proprietary assets.

**8 — Implement with the lightest touch.** Add captions either as one dedicated high-numbered overlay track in the current composition, or as a reusable `compositions/editorial-captions.html` sub-composition. Namespace every new ID and variable with `ecap-`.

**9 — Keep timing outside, motion inside.** Let the outer clip elements own timing, placement, and bounds; animate only the inner wrapper. Drive everything from one paused, seek-safe timeline on the HyperFrames time source, and record every animated selector in the motion sidecar. When a phrase is built up in speech, reveal its words or semantic fragments at their real word starts instead of dropping the finished lockup in early.

**10 — Handle sound as punctuation.** If accents are requested, source local files through `media-use`, place them on their own audio tracks, land each transient on the visual moment it marks, and keep them mixed under intelligible narration. Choosing silence is always allowed.

**11 — Verify against the frame, not the DOM.** Run HyperFrames lint/check at cue midpoints and motion boundaries. Capture early, middle, and late frames for any subject-layered hero, plus one chronological contact sheet of the whole passage. Judge semantic timing, reading order, within-group spacing, controlled variation, face clearance, occlusion, and legibility from those frames, and iterate until the checks pass.

**12 — Preview, then stop.** Start a local preview and hand the user the URL. Render only after the normal HyperFrames preview-and-approval gate.

## What to leave behind

A finished job leaves the project with:

- `caption-design-plan.json`;
- caption markup or a reusable caption sub-composition;
- a complete motion sidecar;
- only local media and SFX references;
- representative cue snapshots;
- a chronological contact sheet for judging variation;
- a passing HyperFrames check;
- a preview URL and a short note on the hero and audio choices you made.

## Non-negotiables

These are the rules that keep the output editorial rather than gimmicky.

**On the writing**

- Keep every phrase short and semantic. Do not caption filler word for word.
- Use mixed case for ordinary support copy. Reserve all caps for acronyms, tight proof labels, or one deliberately forceful CTA keyword.
- Give a cue one primary visual idea, and give a sentence or argument beat one dominant hero moment.
- Do not caption every spoken word large. Hero treatments must stay outnumbered by clean support cues.

**On the type**

- Build a real hierarchy: a clean sans for support, a genuinely heavy or condensed display face for heroes, and an occasional serif or italic accent for a conversational action such as a CTA. Bundle every face locally.
- Only declare weights that exist in the bundled font file. Never synthesise a heavy weight from a lighter one, fake thickness with an oversized stroke, or crush tracking until glyphs touch. Check repeated, narrow, and crossbar-heavy letters at full resolution.
- Default support copy to white. Switch to black only when the actual frame makes white illegible even after a restrained outline, shadow, or local scrim.

**On placement and depth**

- Never cover a face, mouth, key gesture, product, UI, or a property detail that matters.
- When a clean matte exists, build power through proximity: sit important hero words close to the subject so depth reads as intentional, rather than floating them in dead space up top. Aim for 10–22% overlap around hair or the outer head contour, and move the word the moment identifying letters turn ambiguous.
- Only claim text sits behind a person when a real matte, cutout, or defensible occlusion mask actually creates that depth. Without one, place the oversized word in verified negative space.
- Keep a subject cutout frame-locked to the base footage and free of halos, doubled silhouettes, cast shadows, or colour shifts. Do not drop-shadow the subject layer. Prefer original source RGB recombined with the matte alpha, encoded locally with a real alpha channel.
- Protect identifying letters in hero words. Depth may cross an outer stroke, but reposition or resize the moment the overlap makes spelling uncertain.
- Hold creator-safe margins and the project's platform safe zone.

**On the sequence**

- Do not replay one full layout recipe across unrelated argument beats. When adjacent fragments form one sentence or a parallel list, lock them to a single anchor and treatment unless the subject or shot changes; vary timing or scale a touch instead of sending the eye chasing.
- Pick one reading direction per semantic group and keep every later fragment on that path. No down, back-up, down-again zigzag for the sake of motion.
- Keep captions level by default. Rotate only when the source brand or an explicit instruction makes the angle meaningful.
- For step-by-step instructional graphics, keep completed evidence on screen while the next action still depends on it. Place standalone screenshots, folders, and files natively rather than wrapping every asset in a generic card.
- Build a CTA as one compact ordered cluster — setup, action, keyword, closing line — revealed in reading order, with the action word visually next to its keyword so they read as one instruction.

**On effects**

- Do not default to bottom-centre karaoke, word pills, rainbow colour, permanent neon, or a giant word on every cue.
- Treat glow as a brief accent, never the base style.
- Default translucent heroes to neutral silver-white glass: visible source footage through the fill, a fine rim, and an optional soft light sweep. Bring in a hue only when brand, footage, or meaning justifies it. Skip repeating scan lines or banded textures unless the user explicitly asks. Avoid pastel rainbow fills, heavy bevel or extrusion, and decorative depth that turns a word into a detached title card.
- Use sound as punctuation, not wallpaper. Do not accent every phrase. Rotate the palette across adjacent hero beats — reserve shimmer for a single luminous reveal, allow at most one primary accent per landing, and only stack effects when the combination serves a specific narrative purpose.
- Match the user's brand before any reference aesthetic.
- Do not publish, upload, or replace source media without explicit approval.

## When it is done

The captions are finished when they are timed to meaning, integrated with the subject, restrained enough to hold their hierarchy, seek-safe, reproducible from local assets, and verified inside HyperFrames. A technically valid fixed subtitle strip does not count as a cinematic-caption result.
