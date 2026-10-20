# AI Her Way — Video Editing System

A versioned editing workflow and approved reel style for human editors and AI agents. The default is **Signature Sketch** (previously called The Illustrated Editorial Edit): warm paper, hand-drawn animated stickers and diagrams, Advercase typography, raised captions and sound matched to the visible action. Its approved September foundation includes the October refinements documented below.

Ask: **“Edit this in Signature Sketch.”** For the message variation: **“Use Signature Sketch with message stickers beside me.”** Both use `ai-her-way-signature-reels`; the existing technical skill name stays unchanged.

Future styles should have distinct names, specifications and reference examples. Select the requested style rather than blending defaults. The existing alternative styles are listed below; Signature Sketch remains the default when no style is named.

## Start here

1. Use [Edit Videos My Way](skills/edit-videos-my-way/SKILL.md) to select source material, preserve meaning and plan the cuts.
2. Apply [AI Her Way Signature Reels](skills/ai-her-way-signature-reels/SKILL.md) for the current visual and sound treatment.
3. Compare with the [approved 9.6-second sample](skills/ai-her-way-signature-reels/assets/approved-pilot-v7.mp4) and its [documented decisions](skills/ai-her-way-signature-reels/references/approved-example.md).

The style's [visual specification](skills/ai-her-way-signature-reels/references/visual-style.md), [sound direction](skills/ai-her-way-signature-reels/references/sound-direction.md) and [machine-readable tokens](skills/ai-her-way-signature-reels/references/tokens.json) travel with the skill. The sample is included so another editor can see and hear the intended result.

## Shared defaults

- Advercase titles and one-word speech captions; Montserrat support. Commercial Advercase files must be supplied under the editor's licence; they are not distributed here.
- Brand palette: Espresso, Ink, Linen, Ivory, Dusty Blue, Stone, Walnut, Sage, Olive and Gold, with exact values in the tokens file.
- Hand-drawn sticker arrivals, coherent paper explanations and deliberate movement with readable holds.
- Pop for sticker arrivals; typewriter for typed questions/quotes; scribble or continuous draw matched to actual pen movement; whoosh for transitions; alert/ping for selected emphasis. No compulsory sound cadence.
- Gentle push-ins and crop changes roughly every 2–3 seconds in presenter passages; keep longer reading holds for evidence and diagrams. This October refinement extends the approved V7 example.
- Real message screenshots pop beside the presenter on spoken cues, with identifying information already blurred. Featured typed text gets keyboard sounds; handwritten CTAs and underlines get matched dry-pencil sounds. Meaningful scene changes use soft notification pings.
- Protect faces, hands and social interface areas. The sample's raised caption placement is a review starting point, not a universal Instagram safe-zone specification.

Current user instructions take precedence. The signature style supersedes conflicting older Playfair-only, caption and cadence defaults for new AI Her Way reels. Preserve an existing project's requested style.

## Using the skills

Agents working in this checkout can follow [AGENTS.md](AGENTS.md) and read the skill files directly. For skill discovery outside the checkout, copy the two complete folders `skills/edit-videos-my-way` and `skills/ai-her-way-signature-reels` as siblings into your agent's configured skills directory. Keep their `references`, `assets` and `agents` folders together. Each skill has SKILL.md instructions and OpenAI UI metadata; a human editor can follow the same linked specification.

Example request: “Use edit-videos-my-way and ai-her-way-signature-reels to edit this raw reel in our approved style.”

The style is editor-independent. HyperFrames can implement the HTML/SVG animation; use its installed tooling and documentation when selected. The example is viewable without that runtime. Rendering new projects requires source footage, licensed fonts and suitable sound assets.

## Alternative styles

[Quiet Editorial UI](skills/quiet-editorial-ui/SKILL.md), [Tactile Collage](skills/hyperframes-tactile-collage/SKILL.md) and [Cinematic Caption](skills/cinematic-caption/SKILL.md) remain available for explicit alternative treatments and existing projects. Their historical fonts and rules are not the new signature default.

## Maintaining consistency

Style version **1.3.0** lives in the signature skill and tokens file. The 20 October update packages the iMessage treatment and the latest camera/sound directions. Keep defaults separate from campaign-specific copy. The workflow makes the shared target repeatable, but each export still needs visual and audio review.

For the latest message-sticker workflow, start with [the iMessage treatment](skills/ai-her-way-signature-reels/references/imessage-treatment.md). Its portable Python builder assembles a full editable 45.4-second template from your own local assets, with camera and sound cue records. It includes the TEXT lead-magnet handoff conventions and Hub CTA; private messages, raw footage and licensed fonts are not bundled.

Raw footage, reference creators' videos, credentials and commercial font files do not belong in ordinary skill changes. See [LICENSE](LICENSE) for repository terms.

Current approval: V7 includes the accepted camera variation and recorded-pencil sounds. Earlier procedural drawing sounds were rejected as spray-like; use the bundled V7 pencil cues.

## Reusable implementation

The [portable starter](skills/ai-her-way-signature-reels/references/starter.md) packages the actual V7 animation code, a setup script and the three approved CC0 pencil cues. Supply local source footage, accurate captions, licensed fonts and the other sound assets. The starter is an adaptable 9.6-second sequence; full reels still need an editorial plan and review.
