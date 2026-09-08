---
name: hyperframes-tactile-collage
description: Dress a HyperFrames video in AI Her Way's tactile paper-collage look — warm paper grounds, cut-out cards, ink marks, tape, stamps, notebook diagrams, editorial type, and movement that reads as physically placed. Use when someone asks for a tactile paper collage edit, an animated scrapbook, mixed-media notebook graphics, paper-cutout editorial styling, analog collage motion, or this treatment applied to talking-head footage or a full-frame HyperFrames composition.
---

# Tactile Paper Collage

This is a styling companion, not a story workflow. Run it after the owning
HyperFrames workflow is already chosen. It decides how each beat looks in paper;
it never touches the underlying story, timing, footage, audio, spoken claims,
copy, or approved brand assets unless the user separately asks for an editorial
change.

## What this style is

A HyperFrames beat rebuilt as a small physical scene: paper cards, folders,
taped photographs, ink marks, stamps, dotted routes, checklists, and documents
that get handed across the frame. It should feel assembled by hand — warm,
legible, and deliberately composed — and never slide like flat digital panels.
One clear metaphor per beat carries the idea; decoration never stands in for
that metaphor.

## Read before you build

Load the HyperFrames contracts in this order:

1. `/hyperframes` — the entry point.
2. `/hyperframes-core` — required before editing any composition HTML.
3. `/hyperframes-creative` — how design-spec precedence works.
4. `/hyperframes-animation` — required before authoring motion.
5. `/media-use` — required before changing footage, cutting a subject out, or styling captions.

Then resolve this skill's own directory as `<skill-dir>` and read its four
references:

- `references/style-system.md` — the visual tokens, surfaces, and component vocabulary.
- `references/scene-grammar.md` — how to turn a narrative function into a paper scene.
- `references/layering-safe-zones.md` — layout modes, subject layering, fallbacks, and platform-safe regions.
- `references/motion-captions-audio.md` — before you animate, caption, or add sound.

## Working sequence

1. **Open the project.** Resolve the HyperFrames composition directory and read
   its brief, design spec, storyboard or motion board, transcript, composition
   files, and a spread of representative frames.
2. **Inventory what must survive.** List faces, gestures, logos, source UI,
   load-bearing text, approved brand colours, negative space, and any media
   treatment already in place. These set the collision limits.
3. **Break the story into beats.** Give each beat one dominant idea, and for each
   record the physical metaphor you will use and the layout mode you will build in.
4. **Pick a layout mode per beat**, choosing the first that fits:
   - `behind-subject` — a photographic base underneath illustrated plates, with a transparent subject floating above them.
   - `direct-overlay` — intact footage as the base, with bounded paper objects placed only in regions that stay clear across the whole beat.
   - `full-frame` — the paper world takes the entire canvas when no footage or cutout is useful.
5. **Adopt the design spec.** Copy `assets/frame.md` into the project as the
   active specification. If a conflicting spec already exists, preserve it once
   as `frame.pre-tactile-paper-collage.md` before overwriting. Merge in approved
   identity assets and semantic brand colours; do not import content from the
   source project.
6. **Install the fonts** before rendering:

   ```bash
   node <skill-dir>/scripts/install-fonts.mjs <composition-dir>
   ```

7. **Build static hero frames first.** Compose each coherent scene as its own
   sub-composition, and reserve the caption lane before dropping any decoration.
8. **Add captions when needed.** Copy `assets/components/tactile-caption.html`
   into the project's compositions directory and replace its placeholder word
   array with real timings. To check portrait collisions, mount
   `assets/components/tactile-safe-zones.html` on the top track temporarily, then
   remove or hide it before delivery. For other aspect ratios, update its
   internal dimensions and rectangles from `references/layering-safe-zones.md`
   first.
9. **Animate last.** Only start motion once every paused hero frame reads
   clearly at phone size. Keep all render-critical behaviour deterministic and
   seek-safe.
10. **Check the result.** Run the project's current HyperFrames lint/check
    commands, capture representative snapshots, and inspect the opening frame,
    every transition, the densest frame, and the final frame.

## Hold these lines

- Do not replace the owning narrative workflow.
- Do not change cuts, narration, timing, facts, claims, or copy just to fit the style.
- Do not require a transparent subject; fall back to overlay or full-frame instead.
- Do not override approved brand colours with the default palette. Keep the paper/ink contrast roles and remap accents by meaning, not by hue.
- Do not reproduce people, screenshots, transcripts, filenames, folder trees, palettes, or story concepts from any reference video.
- Do not let decorative clutter stand in for a clear metaphor.
- Do not use unseeded randomness, infinite loops, runtime clocks, or forward-only animation callbacks.
- Do not place critical content outside the destination platform's safe region.

## What ships in this skill

- `assets/frame.md` — the design-spec template.
- `assets/components/tactile-caption.html` — a configurable, transcript-timed caption treatment.
- `assets/components/tactile-safe-zones.html` — a removable safe-zone overlay for collision checks.
- `assets/fonts/*.woff2.b64` — encoded open-licensed Permanent Marker, Playfair Display, and Montserrat. (Courier Prime is retained under its OFL license for history but is no longer installed or applied by default.)
- `scripts/install-fonts.mjs` — decodes and installs the fonts into a composition.
- `scripts/validate-package.mjs` — validates structure, portability, licenses, and source isolation.

After changing anything in the skill, revalidate the package:

```bash
node <skill-dir>/scripts/validate-package.mjs <skill-dir>
```
