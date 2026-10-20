# Message stickers and the macOS guide handoff

User direction from 8 October; reaffirmed 20 October 2026. Use for a presenter pointing to message examples or a similar proof-led reel. Preserve the real recorded speech; an on-screen hook or CTA request does not authorise new spoken copy or a wholesale recut.

## Visual and editorial behaviour

- Pop real message examples beside the presenter at the exact spoken demonstratives ("like this", "and this"). Do not replace the presenter with a full-screen message page by default. Keep eyes, mouth, pointing hand and captions clear throughout the moving shot.
- Bake privacy masks into the evidence asset before compositing. Check names, avatars, numbers, email addresses, dates/countdowns, party names, venues, browser tabs, account/sidebar labels and partial adjacent messages. Blur or crop identifying content without rewriting the remaining evidence. Inspect all frames of a screen recording, not just its opening frame.
- Preserve the screenshot's proportions and readable text. Use an ivory rim, rounded sticker shape, small spring/rotation and one pop on landing. If a full message is unreadable at the available size, use a truthful cropped excerpt or a longer readable hold; do not invent a quote.
- A connector walkthrough may still use the paper stage. For this reel, keep the handwritten distinction: "iPad recording. My setup: Mac Mini at home. Requires a desktop Mac." For other creators, use their actual setup. macOS desktop setup and the device used to record a demo are different facts.
- Type the featured "My AI workout buddy" text with matched keyboard audio. The illustrative morning text is a diagram example, not a real message screenshot.
- Closing written invitation: "Comment TEXT / I’ll send you the macOS setup guide." Use handwritten styling and dry pencil audio for the visible writing and underline. Preserve the spoken follow invitation unless asked to change it. Do not add per-word sound to ordinary captions.

## Portable 45.4-second template

[create_imessage_starter.py](../scripts/create_imessage_starter.py) packages the actual editable iMessage composition and shared drawing helpers. It is a timed editorial template, **not automatic transcript analysis**. New footage requires changing text, times, message positions and camera moves in the generated `build_reel.py`, then rebuilding. The original 45.4-second source cut and private screenshots are not distributed.

Inputs are local files; paths resolve relative to your JSON manifest. Commercial fonts, runtime and non-pencil sounds require your own licensed copies. The bundled V7 CC0 pencil cues are reused. Supply 45.4 seconds of edited presenter footage and a separate aligned voice track (the video layer is muted). Message videos need to cover their slots: 3.93, 2.89 and 3.47 seconds; the connector slot is 4.65 seconds. Static message videos may hold a reviewed screenshot. The script validates file types and caption bounds; verify media durations with your editor or ffprobe.

```json
{
  "privacy_reviewed": true,
  "presenter": "inputs/presenter.mp4",
  "voice": "inputs/voice.wav",
  "message_one": "inputs/message-one-redacted.mp4",
  "message_two": "inputs/message-two-redacted.mp4",
  "message_three": "inputs/message-three-redacted.mp4",
  "connector": "inputs/connector-redacted.mp4",
  "advercase_regular": "fonts/Advercase-Regular.ttf",
  "advercase_italic": "fonts/Advercase-Italic.ttf",
  "montserrat": "fonts/Montserrat.woff2",
  "hand_font": "fonts/SegoePrint.ttf",
  "gsap": "runtime/gsap.min.js",
  "pop": "sounds/pop.mp3",
  "ping": "sounds/ping.wav",
  "typewriter": "sounds/typewriter.wav"
}
```

`privacy_reviewed` is an editor attestation, not automated redaction detection. For team demonstrations, use explicitly labelled synthetic messages with no personal content. Real delivery requires the actual reviewed examples.

```text
python scripts/create_imessage_starter.py --assets inputs.json --captions captions.json --out new-imessage-reel
```

Run from the skill directory or use absolute script paths. Captions are `{ "text": "word", "start": 0.1, "end": 0.4 }` records relative to the final edit. In the generated project, edit `build_reel.py`, run `python build_reel.py`, then `npm run check` and `npm run render`. Outputs include the HTML composition, camera cue list and sound cue list. HyperFrames 0.8.90 remains pinned to the tested renderer; no globally installed skill is required to run the Python builder.

Reference timings: first sticker starts 3.18, lands 3.52; second starts 4.22, lands 4.56. Both leave at 7.11. Connector paper stage 11.02–16.35; schedule diagram 16.35–21.4; third message 21.79–25.26. Handwritten CTA 38.5–45.4. These match the original speech only. Never reuse these timings blindly on another recording.

## Guide and caption handoff

If a lead magnet is requested, create or update its Notion page in the user's named database. Include prerequisites, exact setup steps, reusable prompts, one manual send test, one scheduled send test and troubleshooting. Verify current official product documentation before publishing setup instructions; cloud scheduling does not by itself establish availability of a local Mac connector. Do not claim a workflow was tested on the user's Mac merely because documentation was checked.

For this campaign, the comment word is TEXT and the guide ends with a linked invitation to [AI Her Way Hub](https://aiherway.com.au/hub). Caption examples should include useful delivered information, not only reminders: day-ahead summary, news headlines with sources, gratitude journal prompt, end-of-day wrap-up, a learning bite, or a dinner plan based on supplied preferences. Explain that relevant context and connected tools are needed. Do not invent achieved results or imply access to a calendar or inbox that has not been connected.

Track the guide's destination, public-sharing status and comment-to-DM automation separately. An on-screen promise or a database move does not configure delivery. Do not label an automation live until configured and tested; publication and messaging follow the user's actual authorisation.

## Review evidence

The original local v2 export was 1080×1920, 30 fps, 45.4 seconds; measured −19.1 LUFS and −3.5 dBFS true peak. Frame review covered message landings, moving-face clearance, typed text and the closing CTA. No subjective headphone/phone-speaker audition was recorded; a team editor must still listen to each new mix. Nici's 20 October message endorses the overall treatment and requests sharing it. The new portable packaging requires its own checks; approval does not mean every future edit is approved.

Run `python scripts/test_imessage_starter.py` from the skill folder to check local asset packaging, privacy attestation, caption bounds/overlap, escaping, overwrite protection, sticker timing and writing/underline sound families. Its fixtures deliberately are not playable media; it is a setup test, not a visual or listening test. Run `python scripts/test_starter.py` to check the existing V7 builder too.

Release validation on 20 October: all four iMessage setup tests and three existing starter tests passed, as did skill validation. A separate project using generated colour-video fixtures and silent voice, with locally licensed fonts/runtime/effects, rendered at 1080×1920, 30 fps, 45.4 seconds with audio. Its closing CTA frame was inspected; final builder output matched the rendered HTML byte-for-byte. This establishes packaging/renderability, not real-message readability, face clearance or a subjective audio audition for new inputs.
