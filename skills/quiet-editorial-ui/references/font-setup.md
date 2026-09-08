# Font setup

This skill ships the two webfonts it depends on — Playfair Display (the display serif) and Montserrat (the UI sans). Both are licensed under the SIL Open Font License and are free to redistribute, so the user never has to supply their own. Copy them out of this skill's `assets/fonts/` directory into the composition's `public/fonts/` directory, keeping these exact filenames:

```text
PlayfairDisplay-var.woff2
PlayfairDisplay-Italic-var.woff2
Montserrat-var.woff2
```

Each is a variable font spanning the full 400–900 weight range. Never rename some other serif or sans onto these families.

Then run:

```bash
node <skill-dir>/scripts/preflight.mjs <composition-dir>
```

The preflight verifies the WOFF2 signatures and exits non-zero if any required face is missing. Treat a failure as render-blocking: HyperFrames renders inside a clean browser environment that may have no desktop fonts installed, so a system fallback is not an option.

Declare the faces in your compositions like this:

```css
@font-face {
  font-family: "Playfair Display";
  src: url("fonts/PlayfairDisplay-var.woff2") format("woff2");
  font-style: normal;
  font-weight: 400 900;
}

@font-face {
  font-family: "Playfair Display";
  src: url("fonts/PlayfairDisplay-Italic-var.woff2") format("woff2");
  font-style: italic;
  font-weight: 400 900;
}

@font-face {
  font-family: "Montserrat";
  src: url("fonts/Montserrat-var.woff2") format("woff2");
  font-style: normal;
  font-weight: 400 900;
}
```

Refer to the internal family names `Playfair Display` and `Montserrat` so a composition can't silently resolve to a copy installed on the rendering machine.
