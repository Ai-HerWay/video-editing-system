# Motion language

Motion here has one job: to explain a selection, a grouping, progress, or a completion. If a move explains none of those, it does not belong.

## Timing

| Move | Duration |
|---|---|
| Primary entrance | 0.35–0.62s |
| Small label or rule | 0.25–0.4s |
| Cursor travel | 0.55–0.9s, scaled to distance |
| Selection response | 0.18–0.42s |
| Scene exit | 0.12–0.22s |

Typical entrance travel is 12–42px at 1080px short-edge resolution.

## Choreography

- Reveal in order: label, then hero, then operational object.
- Make cursor motion causal — it travels, it selects, and then the state changes.
- Ease with `power3.out` for precise entrances, `expo.out` for display type, and a restrained `back.out(1.2–1.4)` only for compact selection feedback.
- Keep spatial continuity when one object turns into another state.
- Let opacity ride alongside translation, scale, or a masked reveal — never build a sequence from floaty fades alone.
- Keep every render-critical move on a single paused, synchronous timeline.

## Limits

- Animate transforms, opacity, colour, background colour, border colour, or radius — nothing else.
- Never animate layout properties.
- No infinite loops, runtime clocks, unseeded randomness, or input events.
- Never animate a cursor that causes no observable change.
- Never run two success signals at once.
