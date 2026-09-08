# Dynamic Layout Recipes

Reach for this reference the moment a passage carries three or more designed cues. One card is a styling problem; a run of cards is a sequencing problem. The aim is a passage that keeps recomposing around the speaker as the argument moves, instead of dropping the same centred template three times in a row.

## Think in passages, not cards

Plan the whole span as a sequence. Over eight to twelve seconds, move through roughly three to five distinct layout states wherever safe transitions exist. Change state at a real boundary — a new sentence, a new shot, a shift in the subject's position, a turn in the argument — never just because another word has arrived.

Set a `flowDirection` for every semantic group. A group can read upper-left to lower-right, top to bottom, or left to right, but once it has committed, its later fragments cannot double back. Do not manufacture energy with an up-down-up path; open a new path only when the sentence, shot, or section actually changes.

States worth rotating through include:

1. a compact upper-left or upper-right support stack;
2. a large background hero with small foreground support;
3. a foreground chest-level payoff over a background shoulder word;
4. an offset proof word or number spanning the calm side of the frame;
5. a wide headline above the subject with a slight hair or shoulder overlap;
6. a CTA keyword behind the subject paired with an unobstructed foreground instruction.

Move one or two structural properties per state, not all of them. Spend a variation budget across anchor zone, alignment, scale relationship, depth, font accent, fill, and motion — a new group rarely needs to change all seven.

When several adjacent heroes complete one parallel list, hold them in a single subject-relative anchor zone so the viewer can compare them without chasing type around the frame. Pick spatial variation back up once the sentence, subject position, or shot changes.

Keep the type system intentional across the whole passage: one clean support sans, one genuine heavy display face for heroes, and a serif or italic accent only where its editorial tone earns meaning. Variety comes from hierarchy, not from swapping typefaces at random. Keep the colour system just as disciplined: white support, neutral silver-white glass, and at most one accent family per short passage by default — reusing that neutral glass across a parallel hero run reads as continuity, not repetition. Keep text level by default, and find energy in scale contrast, alignment, foreground/background pairings, fill motion, and timing; rotate a caption only when a source design system or an explicit instruction makes the angle part of the language.

## Build phrases up, don't drop them in

Pick one `buildMode` per cue:

- `replace` — the previous phrase clears and a complete short phrase enters;
- `progressive` — semantic fragments appear at their word starts and accumulate into one lockup;
- `foreground-background-handoff` — support copy sets the idea, then the hero lands behind the subject;
- `proof-reveal` — a small label appears first, followed by a much larger number, place, or concrete noun;
- `cta-build` — conversational setup first, the action word in front next, and the keyword landing last as the hero.

Give the most important sentence a `progressive` or a handoff mode. Never show a finished phrase before it has been spoken.

For every group, sketch the final reading order before you assign a single coordinate. Use the group's `orderIndex` values to lay fragments out monotonically along its `flowDirection`. If the finished arrangement cannot be read in speech order while paused, rebuild the stack before you animate it.

Hold a CTA in one compact cluster. Reveal setup, action, keyword, and closing line in the same reading direction — a later keyword must not jump above an earlier action word. Keep the action word close enough to the keyword that they read as one instruction, and let the closing line follow immediately rather than drifting to a distant zone.

## Depth and occlusion

Behind-subject type needs a real matte or cutout. Stack base footage at the bottom, the hero on a middle layer, the subject matte above it, and ordinary support copy on the foreground layer.

Before you place type, confirm the cutout and base footage share start time, frame rate, duration, dimensions, crop, and scale. Review the moving silhouette edge at early, middle, and late depth cues. If the timing matches but a faint shadow or doubled contour lingers, treat it as an RGB/alpha encoding fault: recombine the original source pixels with the matte alpha and encode that foreground at high quality. Do not paper over the defect with blur, scale offsets, or a subject drop shadow.

Set an `occlusionBudget` for every background hero:

- `0.10–0.20` — light hair or shoulder crossing;
- `0.20–0.30` — strong depth while immediate readability holds;
- `0.30–0.35` — the ceiling, and only for very short, familiar words;
- above `0.35` — reject the placement; reposition or resize.

Face or mouth coverage never counts as acceptable overlap. Prefer crossing the lower third of the letters with hair, shoulders, arms, or torso, and keep a crisp rim or stroke around a translucent fill so the hidden and visible portions still resolve into one word. Protect the identifying internal letters: if the matte makes a correctly spelled word look wrong, the placement has failed — move the word so the overlap lands on an outer stroke, or lower the budget.

## Persistent instructional evidence

When captions ride along with a step-by-step workflow, give objects that should accumulate a shared `persistenceGroup`. Keep the source folder, footage file, and destination project visible, for instance, while the AI prompt is typed. Clear completed evidence only when the frame gets crowded or the next instruction no longer depends on it. Present native assets without decorative shells — a screenshot can carry a light shadow, folders and files can stand alone — and reserve cards for real browser, chat, dialog, or application surfaces.

## Fill hierarchy

Use a fill because it serves meaning or sequence variety, never as automatic decoration.

1. **Ordinary support** — clean mixed-case white text with a restrained shadow or local scrim.
2. **Anchor** — white plus one weight or scale shift, optionally one footage-derived accent.
3. **Tinted-glass hero** — neutral silver-white at 32–55% opacity by default, visible source footage, a fine rim, and an optional soft light sweep. A restrained hue joins only with semantic or brand justification; repeating scan lines or stripes need explicit intent.
4. **Video-through-type** — a duplicated local video moves inside the glyphs while the letter geometry stays fixed. Use it for words about motion, change, transparency, place, or visual proof.
5. **Image, map, or flag texture** — only when the spoken content actually names that place, region, country, property, or evidence source.

Unrelated hero cues must not replay the exact same palette, scale, and motion as one complete recipe. A documented parallel hero run may deliberately reuse neutral silver-white, scale, and placement so its items compare cleanly. For dimensional translucent type, reuse the exact same local font for the fill mask, rim, highlight, and extrusion; keep the animated texture visible from the word's first readable frame; and keep bevel and extrusion shallow enough that counters and crossbars stay clean.

## Sound palette rotation

Give adjacent hero landings distinct primary accents: low impact for mass, a single shimmer for the most luminous reveal, a servo or airy sweep for motion, a dry tick for timing, a mechanical clack for an action cue. Do not reuse the same ding or chime on neighbouring beats. Run one primary accent per landing unless the caption plan documents a deliberate layered event.

## Motion recipes

- **Support fragments** — 10–18 px directional rise, 0.16–0.24 seconds, 80–180 ms semantic stagger.
- **Hero handoff** — support establishes first; the hero lands on its spoken word with a 0.26–0.36 second firm settle.
- **Video-through-type** — the word settles first; the internal footage keeps moving while the outline stays crisp.
- **Foreground payoff** — enter from the nearest open side by 14–28 px, no bounce.
- **CTA build** — conversational setup, then action word, then hero keyword, with the final reading order obvious.

Use blur only for a short transition or bloom, and settle to sharp text within 0.4 seconds.

## Anti-repetition review

Build a chronological contact sheet of the cue midpoints, and reject the sequence if any of these are true:

- three unrelated groups share the same centreline and full layout recipe;
- two unrelated heroes use the same palette, scale, placement, and motion;
- adjacent hero beats reuse the same chime or stack multiple high-frequency accents;
- every phrase is already complete on its first visible frame;
- the subject hides a hero word's identifying letters;
- the foreground subject shows a halo, doubled silhouette, shadow, or colour shift against the base footage;
- a semantic group reverses its chosen reading direction;
- paused fragments do not read in spoken order, or use visibly inconsistent gaps;
- a caption is tilted with no explicit visual rationale;
- a CTA action and keyword are split into competing zones;
- a hero face is synthetically bolded, over-tracked inward, or shows merged strokes or false cross-lines;
- translucent words use pastel rainbow fills, excessive bevel or extrusion, or float above a large unused gap when a clean matte could create stronger proximity;
- sequential instructional assets vanish before the dependent action appears;
- all support copy shares the same width, alignment, and vertical zone;
- hero treatments outnumber clean support cues;
- a location, flag, or map texture appears with no semantic justification.

The finished sequence should feel authored as one editorial passage: related fragments share a clear spatial system, and every meaningful beat change gets controlled variation.
