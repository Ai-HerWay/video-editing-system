# Font setup

The skill bundles Inter but does not distribute Georgia. Obtain licensed webfont files through the user's own font license and place them in the composition's `public/fonts/` directory with these exact names:

```text
Georgia-Regular.woff2
Georgia-Italic.woff2
Inter-400-latin.woff2
Inter-700-latin.woff2
```

Copy the Inter files from this skill's `assets/fonts/` directory. Do not rename another serif to Georgia.

Run:

```bash
node <skill-dir>/scripts/preflight.mjs <composition-dir>
```

The preflight checks for valid WOFF2 signatures and exits nonzero when a required face is unavailable. Treat failure as render-blocking. Do not use a system-font fallback because HyperFrames renders in a clean browser environment that may not have desktop fonts installed.

Use these declarations in project compositions:

```css
@font-face {
  font-family: "Georgia QEUI";
  src: url("fonts/Georgia-Regular.woff2") format("woff2");
  font-style: normal;
  font-weight: 400;
}

@font-face {
  font-family: "Georgia QEUI";
  src: url("fonts/Georgia-Italic.woff2") format("woff2");
  font-style: italic;
  font-weight: 400;
}
```

Reference the internal family name `Georgia QEUI` so the composition cannot silently resolve to a machine-installed copy.
