---
name: quiet-editorial-ui
description: Apply AI Her Way's Quiet Editorial styling layer to an existing HyperFrames project. Use when someone asks to dress a HyperFrames composition in the quiet editorial look, restyle it with serif-led editorial graphics, sit refined overlays in negative space or directly over footage, or build a full-frame graphic beat in the same editorial system.
---

# Quiet Editorial UI

This is AI Her Way's in-house editorial styling layer. It sits on top of an existing HyperFrames project once the owning narrative workflow is already chosen. Treat the project's story, timing, footage, audio, copy, and signed-off brand assets as fixed — only touch them if the user separately asks for editorial changes.

The look is deliberately calm: literary Playfair Display headlines, precise Montserrat interface copy, warm paper surfaces, restrained depth, and motion that only ever exists to show a state change. Nothing decorates for the sake of it.

## What to read before you start

Load the HyperFrames contracts in this order, because this skill assumes them:

1. `/hyperframes` — the entry point for any composition work.
2. `/hyperframes-core` — required before you touch composition HTML.
3. `/hyperframes-creative` — tells you how design-spec precedence works on this project.
4. `/hyperframes-animation` — required before you author any motion.
5. `/media-use` — the caption guidance, whenever captions are asked for or already in the cut.

Then pull in this skill's own references only as each one becomes relevant. Resolve the skill folder as `<skill-dir>`:

- `references/style-system.md` — the visual language and how the component grammar hangs together.
- `references/layout-modes.md` — how to pick a mode and slot the style into the project.
- `references/captions.md` — building and timing captions.
- `references/safe-zones.md` — platform-safe rectangles and the collision order.
- `references/motion-language.md` — the motion vocabulary and its limits.
- `references/font-setup.md` — installing the bundled Playfair Display and Montserrat faces.

## The working sequence

Work through these steps in order. Each one assumes the one before it is done.

**1 — Read the project as it stands.** Open the composition directory. Read its brief, its storyboard or motion board, its design spec, the transcript, the composition files, and a spread of representative frames. Build a mental picture of what is already there before you add anything.

**2 — Inventory what you must protect.** Note every face, logo, piece of source UI, and load-bearing source line, plus the negative space you might be able to use. Do not assume this is a talking-head layout — this style makes no such assumption.

**3 — Pick a layout mode.** Take the first one that genuinely fits:
- `available-area` — there is a stable unused region big enough to hold the whole graphic idea.
- `direct-overlay` — footage owns the frame, so graphics have to ride on top of it.
- `full-frame` — there is no footage, or a beat deliberately hands the whole frame to graphics.

**4 — Install the design spec.** If the project already has a `frame.md` that would conflict, preserve it once as `frame.pre-quiet-editorial-ui.md` (never back up a backup). Then copy this skill's `assets/frame.md` in as the working `frame.md`, and fold only the approved logos, copy rules, and semantic brand colours into its `Approved Entities` section. Everything else — type, surfaces, spacing, hierarchy, captions, motion — is owned by this style.

**5 — Install the fonts.** Copy the bundled Playfair Display and Montserrat WOFF2 files from `assets/fonts/` into the composition's `public/fonts/`, following `references/font-setup.md`. Both ship under the SIL Open Font License, so nothing extra is needed from the user.

**6 — Preflight the fonts.** Before any command that can trigger a render, run:

   ```bash
   node <skill-dir>/scripts/preflight.mjs <composition-dir>
   ```

   If it reports a missing or malformed font, stop and fix it. Never quietly fall back to a different serif or sans.

**7 — Build the beats.** Apply the chosen mode. One dominant idea per beat, token values used exactly as written, source content left recognisable.

**8 — Add captions if they belong.** Copy `assets/components/quiet-editorial-caption.html` into the project and follow `references/captions.md`. If you are unsure where a lane is safe, drop `assets/components/quiet-editorial-safe-zones.html` in temporarily as a top-track sub-composition, then remove or hide it before delivery.

**9 — Validate.** Run `npx hyperframes lint`, `npx hyperframes check`, and take snapshots at the beats that matter. Check the result at phone size as well as full resolution.

## Hard boundaries

- Do not choose or swap the owning narrative workflow — that decision belongs elsewhere.
- Do not alter cuts, timing, audio, narration, claims, or copy purely to make the style sit more easily.
- Do not assume footage, a speaker, a fixed speaker size, or a split-screen arrangement.
- Do not import product names, logos, toggles, prompts, interface replicas, sample files, or branded icons from any outside reference.
- Do not spend the confirmation green as a general accent.
- Do not shrink a caption below its documented floor to dodge a collision — move to another safe lane instead.
- Do not render on a fallback display face when the bundled Playfair Display files are absent.

## What ships in this skill

- `assets/frame.md` — the working design specification.
- `assets/components/quiet-editorial-caption.html` — a transcript-timed caption sub-composition.
- `assets/components/quiet-editorial-safe-zones.html` — a removable safety overlay for layout checks.
- `assets/examples/golden-frames.html` — a reference sheet showing the look across three aspect ratios.
- `assets/fonts/PlayfairDisplay-var.woff2`, `PlayfairDisplay-Italic-var.woff2`, `Montserrat-var.woff2` — the OFL display and UI faces.

After changing anything in the skill itself, revalidate the package:

```bash
node <skill-dir>/scripts/validate-package.mjs <skill-dir>
```
