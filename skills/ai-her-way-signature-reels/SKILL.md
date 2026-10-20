---
name: ai-her-way-signature-reels
description: Apply Signature Sketch, the approved AI Her Way illustrated editorial reel style, with Advercase captions, hand-drawn stickers, diagrams and matched sound. Use when asked for Signature Sketch or the default branded reel treatment; preserve source edits unless restructuring is requested.
---

# Signature Sketch — AI Her Way

**Style name: Signature Sketch.** Requests such as "Edit this in Signature Sketch" select this complete visual, motion and sound treatment, including the iMessage variation. "The Illustrated Editorial Edit" and "AI Her Way signature style" are legacy aliases for the same style. Keep the technical skill ID `ai-her-way-signature-reels` stable. This naming update changes no approved visual or audio rules.

Keep future styles separate: each needs its own name, specification and reference example. An explicit request for another style overrides this default; do not blend styles unless asked.

Produce sophisticated, warm reels in the style Nici approved on 29 September 2026. This is the default visual and sound treatment for new AI Her Way reels. A current user request overrides these defaults. Older Playfair, frosted-glass, mandatory sound-cadence and caption rules in other skills do not override this style.

Read [the visual specification](references/visual-style.md) and [sound direction](references/sound-direction.md) before composing. Consult [the approved example](references/approved-example.md) when matching movement, layout or sound density. These resources are packaged with this skill; they do not depend on the original editor's computer.

For repeatable implementation, use the [portable starter and bundled approved pencil cues](references/starter.md). The starter contains the actual approved animation code; supply the new source and its real caption timings.

## Apply the style

1. Establish the reel's purpose and exact retained speech. For source selection and restructuring, use the repository's `edit-videos-my-way` skill when available; this style also works with an already edited video. Preserve meaning, negations, numbers and the speaker's natural voice. Do not turn a style revision into a fresh cut.
2. Use Advercase for titles and speech captions, supported by Montserrat. Read the font requirements in the visual specification; do not silently substitute a legacy font.
3. Map each important idea to a purposeful visual: hand-drawn sticker, connected diagram, question, quote, real evidence or presenter beat. Give the sequence room to be read. Rich animation does not require constant movement or a fixed event cadence.
4. Build around the approved ingredients: warm paper surfaces, irregular ivory sticker rims, restrained shadows, soft spring arrivals, connected line drawings and expressive editorial type. Use the brand palette in [tokens.json](references/tokens.json). Preserve the visual identity across transitions; adapt the actual diagram to the spoken idea.
Use gentle push-ins and modest crop changes roughly every 2–3 seconds during presenter passages. Keep readable holds for diagrams and evidence. This latest direction supersedes the earlier selective 1–2-second suggestion for new reels.

For messages beside a presenter, read [the iMessage treatment and portable builder](references/imessage-treatment.md): privacy redaction, speech-matched sticker landings, typed titles, handwritten CTAs and the optional lead-magnet handoff.

5. Protect the face, hands, evidence and Instagram interface areas. Start from the approved caption placement and review representative moving frames with an interface overlay. Margins are review guides, not a guarantee across devices or expanded post captions.
6. Choose sound by the visible action. Write a cue list with visual target, sound family, start and end; every cue should have an identifiable purpose. Keep the voice intelligible. In particular, a continuous arrow gets one draw, not a repeated scribble loop.
7. Render a reviewable sample when the brief needs a new treatment, or continue an already approved treatment without repeating an approval interview. Use the available editor/compositor; when using HyperFrames, follow its installed composition/render instructions. No dependency on a particular user's absolute paths.

## Delivery checks

- Inspect the exported video, including transitions and frames containing the longest captions. Check face/hand clearance and right/bottom interface clearance.
- Verify the export's duration, dimensions, frame rate, included audio and absence of clipping. Listen for sound-to-action timing and masked speech; state any listening limitation instead of claiming an unheard mix was auditioned.
- Compare the result to the approved example for typography, sticker character, diagram clarity and restraint. Confirm that typed text stops making sound when typing stops.
- Deliver the actual preview, editable project, source range/cut map, font and asset provenance, cue list and relevant checks. Report actual user feedback separately from editorial inference; only mark a result approved when the user approves it.

Style version: **1.3.0** (20 October 2026). Includes October's scene pings, featured typing, handwritten CTA sounds, 2–3-second presenter reframes and portable iMessage treatment. V7 remains the packaged visual/pencil reference; the iMessage rules are later user-requested refinements, endorsed for sharing on 20 October. Examples establish a shared target, not a promise of identical outputs from every editor or renderer.
