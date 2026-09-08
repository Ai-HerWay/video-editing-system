# Motion, captions, and audio

## How things should move

Motion exists to make a paper object read as placed, drawn, passed, opened, or
stamped — a physical action, never a slide.

- **Primary card entrances** — `0.42-0.75s`, usually `power3.out`.
- **Compact stickers and verdicts** — `0.32-0.58s`, a restrained `back.out(1.25-1.5)`.
- **Routes and scribbles** — draw across `0.5-1.2s` with a synchronous SVG stroke animation.
- **Handed-off objects** — hold the same object's position and scale through the transition wherever you can.
- **Exits** — `0.16-0.3s`; give them a reason to leave rather than fading in place.
- **Rotational settling** — start within roughly `8deg` of the final angle and correct into the intended resting tilt.

Budget one hero move, one supporting move, and a quiet background per beat.
Animate transforms, opacity, colour, border colour, radius, or SVG stroke
properties — never layout properties.

Register a single paused, seek-safe timeline under the exact composition id.
No runtime clocks, no infinite CSS animations, no unseeded randomness, no delayed
DOM work, and no callbacks whose result only exists after the timeline plays
forward.

## Captions

Start from `assets/components/tactile-caption.html`.

1. Swap the placeholder `words` array for corrected word-level timings.
2. Break cues at punctuation, a meaningful pause, or four words — whichever comes
   first.
3. Strip punctuation from the displayed text unless it changes the meaning.
4. Keep it to one or two compact lines, and one cue on screen at a time.
5. Use the card surface over busy footage; use unboxed ink only over clean paper.
6. Light at most one meaningful word per cue with a project accent.
7. Hold the caption lane steady for as long as a cue is visible.

If a cue collides with something, shorten the phrase or move it to another safe
lane. Never solve a collision by shrinking type below the documented floor.

## Audio

- Leave the narration alone unless the user asks for a recut.
- Keep any music bed quiet and subordinate to speech — acoustic, percussive, or
  lightly mechanical textures suit the paper world.
- Add local effects sparingly, and only for a real causal event: a paper
  placement, a stamp, a route drawing in, a file handoff, a check, a page turn.
- Don't put a sound on every entrance.
- Fade the bed in at the start and out at the end, on the registered timeline.
- Defer to the owning audio skill for mixing, gain automation, and ducking.
