# Font setup

The skill bundles both webfonts it needs — Playfair Display (display serif) and Montserrat (UI sans). Both are licensed under the SIL Open Font License and are redistributable, so no user-supplied font files are required. Copy them from this skill's `assets/fonts/` directory into the composition's `public/fonts/` directory, keeping these exact names:

```text
PlayfairDisplay-var.woff2
PlayfairDisplay-Italic-var.woff2
Montserrat-var.woff2
```

Each is a variable font covering the full 400–900 weight range; do not rename another serif or sans to these families.

Run:

```bash
node <skill-dir>/scripts/preflight.mjs <composition-dir>
```

The preflight checks for valid WOFF2 signatures and exits nonzero when a required face is unavailable. Treat failure as render-blocking. Do not use a system-font fallback because HyperFrames renders in a clean browser environment that may not have desktop fonts installed.

Use these declarations in project compositions:

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

Reference the internal family names `Playfair Display` and `Montserrat` so the composition cannot silently resolve to a machine-installed copy.
