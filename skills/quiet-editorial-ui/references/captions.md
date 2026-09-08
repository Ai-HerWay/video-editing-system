# Captions

Start from `assets/components/quiet-editorial-caption.html`. Copy it into the project's `public/compositions/` folder, then copy the required font files into `public/fonts/`.

## Preparing the transcript

1. Work from word-level timestamps.
2. Read the transcript through and correct it before you author anything.
3. Strip music markers, junk tokens, and any hallucinated filler.
4. Keep each word as `{ id, text, start, end }`.
5. Drop the cleaned transcript into the component's `TRANSCRIPT` array, replacing the placeholder words.
6. List a few genuinely meaningful words in `ACCENT_WORDS`. Do not accent every cue.
7. Set the component's `data-duration`, and the host's, to the exact caption window.

The component groups the words for you as it runs. It closes a group at punctuation, at any pause of 150ms or more, or once a group reaches its word cap. Displayed text has punctuation stripped and always stays on one line.

## How it should look

- The whole caption is Montserrat 700.
- Playfair Display italic appears only on the words you listed in `ACCENT_WORDS`.
- The success green appears only when the word itself means completion or confirmation (list those in `CONFIRM_WORDS`).
- Set `GROUND = "clean"` for a quiet, high-contrast background.
- Set `GROUND = "framed"` for busy, bright, or moving footage.
- One group is visible at a time.
- Every group is fitted to its safe width via `fitTextFontSize`.
- Proportional type stays at 96px or larger at 1080px portrait width. If a phrase will not fit, shorten the group or change lanes — never let it wrap to a second line.

## Wiring the host

Use one composition id across the host, the template root, and the timeline key:

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

Keep the caption above the footage and graphic tracks but below the optional safe-zone debug overlay. Check every cue end — the component hard-hides each group at its end timestamp.

## Placement

Use the preferred lane from `safe-zones.md`. If a face, mouth, logo, source UI, or load-bearing text crosses that lane, move to the nearest alternate lane that stays safe for the entire cue. A cue must never change lanes while it is on screen.
