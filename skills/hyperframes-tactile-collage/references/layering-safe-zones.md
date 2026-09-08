# Layering and safe zones

## The three layout modes

### Behind subject

Reach for this when a stable transparent subject layer already exists, or when
the owning media workflow has cleared you to create one.

Stack it back to front:

1. The original photographic plate, or a treated background.
2. The paper ground and any non-essential texture.
3. Load-bearing diagrams and paper objects.
4. The transparent subject.
5. Edge labels and any foreground handoff objects.
6. Captions.

Keep the face, mouth, microphone, and active gestures unobstructed. Park
important background copy above the silhouette or out in the stable side
columns. Never trust a fixed subject scale — inspect the actual alpha silhouette
across the entire beat, because the speaker moves.

### Direct overlay

Reach for this when there is no cutout, or when pulling the subject out wouldn't
improve the edit. Anchor bounded paper objects in negative space that stays
clear for the full length of the beat. If no region stays stable that long, cut
to a short full-frame scene instead of chasing the speaker with moving overlays.

### Full frame

Reach for this when the footage adds nothing, a diagram needs the whole canvas,
or the project has no face at all. Hold to one hero object and one supporting
element — a path, a label, or a piece of evidence. Don't let it thicken into a
dense scrapbook page.

## Who wins a collision

When two elements compete for the same pixels, protect them in this order:

1. Face and mouth.
2. Meaningful gestures and held objects.
3. Load-bearing source UI or text.
4. Logos and identity marks.
5. Captions.
6. Explanatory collage objects.
7. Decorative texture.

Always move or drop the lower-priority element first.

## Default critical regions

Coordinates are in output pixels; scale them proportionally for other
resolutions.

| Format | Critical region | Caption lane | Caption max width |
|---|---|---|---|
| 1080×1920 portrait | `x=90-990`, `y=240-1520` | centred near `y=1190-1340` | 840px |
| 1920×1080 landscape | `x=96-1824`, `y=54-972` | lower third near `y=810-955` | 1640px |
| 1080×1080 square | `x=72-1008`, `y=72-1008` | centred near `y=750-910` | 900px |

Background footage and non-essential texture can bleed past these edges. The
caption lane, though, is reserved for the whole cue — including any scale
emphasis and its shadow.

## Sampling the frame

Check at least the start, midpoint, and end of every beat. Add more samples
wherever the subject moves, a gesture widens, source UI changes, or a paper
object might overshoot its mark. A clean opening frame is no proof the rest of
the beat stays collision-free.
