# Safe zones

All coordinates below are output-resolution coordinates. Background media and nonessential texture may bleed beyond the critical area.

| Format | Critical area | Preferred caption lane | Caption max width |
|---|---|---|---|
| 1080×1920 portrait | `x=90–990`, `y=240–1520` | center `y=1220–1320` | 840px |
| 1920×1080 landscape | `x=96–1824`, `y=54–972` | `y=820–960` | 1640px |
| 1080×1080 square | `x=72–1008`, `y=72–1008` | `y=760–920` | 900px |

For other resolutions, scale these rectangles proportionally from the matching aspect-ratio family.

## Collision hierarchy

Protect in this order:

1. Face and mouth.
2. Required source UI and load-bearing source text.
3. Logos and identity marks.
4. Captions.
5. Editorial overlay graphics.
6. Decorative or background elements.

Move lower-priority elements before higher-priority elements. Do not hide required source information to preserve the preferred layout.

## Alternate lanes

- Portrait: try centered `y=1000–1120`, then `y=1360–1480` if both remain inside the critical area.
- Landscape: try `y=680–800`, then a left- or right-aligned lower third clear of the subject.
- Square: try `y=620–740`, then an upper-middle lane if the lower half is occupied.

Reserve the chosen lane for the entire cue, including entrance and exit motion. Account for italic ascenders, scale emphasis, shadows, and cursor overshoot.

## Debugging

Mount `assets/components/quiet-editorial-safe-zones.html` on the highest track during layout work. Set its root dimensions to the target output size. Add temporary exclusion rectangles for the actual face and source UI when necessary. Remove the host or set `data-hidden` before final render.
