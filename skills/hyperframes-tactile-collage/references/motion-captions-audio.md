# Motion, captions, and audio

## Motion language

Motion should make paper objects feel placed, drawn, passed, opened, or stamped.

- Primary card entrances: `0.42-0.75s`, usually `power3.out`.
- Compact stickers and verdicts: `0.32-0.58s`, restrained `back.out(1.25-1.5)`.
- Routes and scribbles: draw over `0.5-1.2s` with a synchronous SVG stroke animation.
- Handed-off objects: preserve the same object's position and scale across the transition when possible.
- Exits: `0.16-0.3s`; move with a reason instead of fading in place.
- Rotational settling: begin within roughly `8deg` of the final angle and correct toward the intended resting tilt.

Keep one hero move, one supporting move, and a quiet background. Animate transforms, opacity, color, border color, radius, or SVG stroke properties; avoid layout-property animation.

Register a paused, seek-safe timeline under the exact composition id. Do not use runtime clocks, infinite CSS animations, unseeded randomness, delayed DOM work, or callbacks whose result exists only after forward playback.

## Captions

Use `assets/components/tactile-caption.html` as a starting point.

1. Replace the neutral `words` array with corrected word-level timings.
2. Group at punctuation, meaningful pauses, or four words—whichever comes first.
3. Remove punctuation from displayed text unless it changes meaning.
4. Keep one or two compact lines and one cue visible at a time.
5. Use the sheet surface over busy footage and unboxed ink only over a clean paper ground.
6. Highlight at most one meaningful word per cue with a project accent.
7. Keep the caption lane stable while a cue is visible.

If a caption collides, shorten the phrase or choose another safe lane. Do not solve collisions by shrinking below the documented floor.

## Audio

- Preserve narration unless the user requests a recut.
- Use a quiet instrumental bed with acoustic, percussive, or lightly mechanical texture; keep it subordinate to speech.
- Add sparse local effects only for causal events: paper placement, stamp, route draw, file handoff, check, or page turn.
- Do not add an effect to every entrance.
- Fade the bed at the beginning and end on the registered timeline.
- Follow the owning audio skill for mixing, gain automation, and ducking.
