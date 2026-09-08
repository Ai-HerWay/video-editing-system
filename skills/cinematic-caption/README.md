# Cinematic Caption

AI Her Way's cinematic caption system for HyperFrames videos — a way to treat captions as part of the picture instead of subtitles stapled to the bottom of the frame.

Rather than dropping every line into a fixed strip, the skill turns speech into a short run of designed editorial moments. It scores the words that actually carry the claim, builds each sentence in the order it is spoken, holds related fragments together in one spatial group, and dresses them with mixed-case support copy, heavy display heroes, translucent glass fills, real subject depth, and restrained sound accents — all pinned to AI Her Way's locked Social/Reels brand system.

## What you need

- A local [HyperFrames](https://github.com/heygen-com/hyperframes) project
- An AI coding agent that supports installable `SKILL.md` skills
- Source footage or an existing HyperFrames composition to caption

## Install

This skill is distributed to AI Her Way Pro Hub members. Copy the `cinematic-caption` folder into your agent's skills directory, then restart the agent so it discovers the skill.

- **Claude Code:** copy it into `~/.claude/skills/cinematic-caption`
- **Other compatible agents:** copy it into that agent's skills directory (commonly `~/.agents/skills/cinematic-caption`)

## Use

Invoke it directly:

```text
$cinematic-caption
```

Or just ask:

- "Apply the cinematic caption skill to this video."
- "Add cinematic spatial captions to this HyperFrames project."
- "Make the important words large, translucent, and animated."
- "Give these captions a premium real-estate editorial style."

The skill reads word timing, scores hero candidates for meaning and proof value, edits speech into ordered semantic groups, maps how the speaker moves across each cue, plans controlled layout changes around that motion, implements progressive mixed-depth overlays, and verifies both representative frames and the whole visual sequence before rendering.

Designed passages avoid both template repetition and random movement. Each sentence gets one reading direction, consistent internal spacing, and a subject-relative anchor. Parallel hero lists can hold a single placement instead of moving on every word, while unrelated beats change only one or two design properties at a time. The default translucent treatment is neutral silver-white glass: the source footage stays visible through a 32–55% fill, a fine rim preserves readability, and lower strokes can tuck behind the subject when a clean matte exists.

## What it produces

- A `caption-design-plan.json` timing and design plan
- Caption markup or a reusable caption sub-composition
- Seek-safe motion metadata
- Local media and optional sound-effect references
- Verification snapshots and a passing HyperFrames check
- A chronological contact sheet for reviewing layout variety
- A local preview for approval

## License

Proprietary to AI Her Way. See [LICENSE](LICENSE). Provided to Pro Hub members for their own use; not for redistribution or resale.
