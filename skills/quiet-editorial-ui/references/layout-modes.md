# Layout modes

Choose layout from the actual frame, not from the media category.

## Mode selection

| Mode | Choose when | Treatment |
|---|---|---|
| `available-area` | A stable negative-space region can hold the complete idea | Anchor a deliberate editorial stage to that region; keep footage and source UI untouched |
| `direct-overlay` | Footage fills the frame or negative space changes too much | Use a bounded surface, local scrim, or strong type contrast; avoid faces and load-bearing source content |
| `full-frame` | No footage exists or a beat intentionally hands ownership to graphics | Use the warm canvas, one hero idea, and a secondary UI object or structural path |

Do not switch modes inside a beat. A composition may use different modes across beats when the source and story justify it.

## Inspection pass

1. Capture or inspect at least three representative frames: early, middle, and late.
2. Mark face and mouth regions, logos, source UI, source text, captions, and moving objects.
3. Find regions that remain clear across all sampled frames.
4. Reserve the caption lane before placing other graphics.
5. Prefer `available-area` only when the full motion envelope fits, including overshoot and cursor travel.
6. Use `direct-overlay` when the free region is intermittent or too small for the complete idea.

## Existing design specifications

- Treat the style as presentation authority when the user explicitly invokes it.
- Preserve approved identity assets, exact user copy, and semantic brand information.
- Preserve an existing `frame.md` once as `frame.pre-quiet-editorial-ui.md` before replacing it.
- Do not recursively back up a previous backup.
- Record retained brand exceptions under `Approved Entities` in the effective `frame.md`.

## Composition behavior

- Portrait: favor a strong vertical stack or a bounded stage; do not assume top graphics and bottom footage.
- Landscape: favor an asymmetric editorial split when a stable subject occupies one side; otherwise use a low, wide overlay or full-frame treatment.
- Square: use a compact vertical hierarchy and reduce simultaneous UI objects.
- Busy or bright footage: introduce a warm-white surface or localized contrast layer behind load-bearing text.
- Clean footage: allow unboxed ink text when contrast and motion remain readable.
