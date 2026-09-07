# Captions

Use `assets/components/quiet-editorial-caption.html` as the starting sub-composition. Copy it into the project's `public/compositions/` folder, then copy the four required font files into `public/fonts/`.

## Transcript preparation

1. Use word-level timestamps.
2. Read and correct the transcript before authoring.
3. Remove music markers, invalid tokens, and hallucinated filler.
4. Preserve the word objects as `{ id, text, start, end }`.
5. Replace the neutral `WORDS` array in the component with the cleaned project transcript.
6. Set `EMPHASIS_WORDS` only for a few editorially meaningful words. Do not emphasize every cue.
7. Set the component and host `data-duration` to the exact caption window.

The component groups words synchronously. It breaks at punctuation, pauses of at least 150ms, or four words. It removes punctuation from displayed text and keeps one line.

## Visual behavior

- Use Montserrat 700 for the full caption.
- Use Playfair Display italic only for explicitly listed emphasis words.
- Use the success green only when the word itself means completion or confirmation.
- Use `SURFACE_MODE = "clean"` for a quiet, high-contrast ground.
- Use `SURFACE_MODE = "card"` for busy, bright, or moving footage.
- Keep one group visible at a time.
- Fit every group to its safe width with `fitTextFontSize`.
- Keep proportional type at 96px or larger at 1080px portrait width. If a phrase cannot fit, shorten the group or move lanes; do not force a second line.

## Host wiring

Use the same composition id on the host, template root, and timeline key:

```html
<div
  id="quiet-editorial-caption-host"
  data-composition-id="quiet-editorial-caption"
  data-composition-src="compositions/quiet-editorial-caption.html"
  data-start="0"
  data-duration="8"
  data-track-index="8"
  data-width="1080"
  data-height="1920"
></div>
```

Keep the caption above footage and graphic tracks, but below the optional safe-zone debug overlay. Verify every cue end; the component hard-kills each group at its end timestamp.

## Placement

Use the preferred lane from `safe-zones.md`. If a face, mouth, logo, source UI, or load-bearing text intersects that lane, choose the nearest alternate lane that remains safe for the entire cue. Never allow a cue to jump lanes while visible.
