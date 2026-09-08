# Safe zones

Every coordinate below is in output-resolution space. Background media and non-essential texture may bleed past the critical area; load-bearing content may not.

| Format | Critical area | Preferred caption lane | Caption max width |
|---|---|---|---|
| 1080×1920 portrait | `x=90–990`, `y=240–1520` | centred `y=1220–1320` | 840px |
| 1920×1080 landscape | `x=96–1824`, `y=54–972` | `y=820–960` | 1640px |
| 1080×1080 square | `x=72–1008`, `y=72–1008` | `y=760–920` | 900px |

For any other resolution, scale these rectangles proportionally from the matching aspect-ratio family.

## Who gives way to whom

When two things want the same space, protect them in this order:

1. Face and mouth.
2. Required source UI and load-bearing source text.
3. Logos and identity marks.
4. Captions.
5. Editorial overlay graphics.
6. Decorative or background elements.

Always move the lower-priority element. Never hide required source information to keep a preferred layout.

## Alternate lanes

- **Portrait** — try centred `y=1000–1120`, then `y=1360–1480`, as long as both stay inside the critical area.
- **Landscape** — try `y=680–800`, then a left- or right-aligned lower third clear of the subject.
- **Square** — try `y=620–740`, then an upper-middle lane if the lower half is taken.

Hold the chosen lane for the whole cue, entrance and exit included. Leave room for italic ascenders, scale emphasis, shadows, and cursor overshoot.

## Debugging placement

Mount `assets/components/quiet-editorial-safe-zones.html` on the highest track while you lay out. Set its root dimensions to the target output size, and add temporary exclusion rectangles for the real face and source UI when you need them. Remove the host, or set `data-hidden`, before the final render.
