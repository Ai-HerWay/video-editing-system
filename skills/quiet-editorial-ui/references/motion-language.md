# Motion language

Motion should explain selection, grouping, progress, or completion.

## Timing

- Primary entrances: 0.35–0.62s.
- Small labels and rules: 0.25–0.4s.
- Cursor travel: 0.55–0.9s, scaled to distance.
- Selection response: 0.18–0.42s.
- Scene exits: 0.12–0.22s.
- Typical entrance travel: 12–42px at 1080px short-edge resolution.

## Choreography

- Reveal the label, then the hero, then the operational object.
- Make cursor motion causal: travel, select, then show the state change.
- Use `power3.out` for precise entrances, `expo.out` for display type, and restrained `back.out(1.2–1.4)` only for compact selection feedback.
- Preserve spatial continuity when one object becomes another state.
- Use opacity to support translation, scale, or a masked reveal; do not build sequences from floaty fades alone.
- Keep all render-critical motion on a synchronous paused timeline.

## Constraints

- Animate transforms, opacity, color, background color, border color, or radius only.
- Do not animate layout properties.
- Do not use infinite loops, runtime clocks, unseeded randomness, or input events.
- Do not animate a cursor unless it causes an observable change.
- Do not use more than one success signal at a time.
