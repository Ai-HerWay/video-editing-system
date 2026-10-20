# Repeatable code and sound assets

The [editable starter](../assets/starter/index.html) contains the approved V7 sticker SVGs, paper-stage animation, raised captions, three drawing cues, continuous long-arrow stroke, camera push-ins and crop cut. Motion is on one paused, registered GSAP timeline; footage and captions remain separate layers. It is a **9.6-second sequence to adapt**, not a full-reel generator or a universal three-sticker story.

The [starter script](../scripts/create_starter.py) creates a portable project from user-supplied local assets. It requires Python 3 and the standard library. For rendering, the generated project pins HyperFrames 0.8.90, the version used for the approved sample. Follow the installed HyperFrames workflow when checking or upgrading the renderer.

Create `inputs.json` with paths relative to that JSON file (absolute paths also work):

```json
{
  "source": "inputs/footage.mp4",
  "advercase_regular": "fonts/Advercase-Regular.ttf",
  "advercase_italic": "fonts/Advercase-Italic.ttf",
  "montserrat": "fonts/Montserrat.woff2",
  "gsap": "runtime/gsap.min.js",
  "pop": "sounds/pop.mp3",
  "whoosh": "sounds/whoosh.mp3",
  "ping": "sounds/ping.mp3"
}
```

Supply licensed fonts, runtime and these sound assets. They are not redistributed by this starter. The three approved CC0 pencil excerpts **are bundled**, along with their source/processing record in [pencil provenance](../assets/pencil/provenance.json). Treat the sample as the sound reference when choosing the other effects. Typewriter is a documented convention; this sequence does not contain typing or require a typewriter file.

Provide `captions.json` as an array of `{ "text": "word", "start": 0.1, "end": 0.4 }` records, timed relative to the selected 9.6-second range. Use the actual source transcript, not the demonstration's words.

```text
python scripts/create_starter.py --assets inputs.json --captions captions.json --source-start 28.2 --out new-reel
```

Run that command from the skill folder, or use the script's full path. Choose the appropriate source start; 28.2 is only the original pilot's offset. The source must contain the entire selected range. The script validates local inputs and caption bounds and refuses to overwrite a non-empty project.

In the output project, run `npm run check -- --snapshots`, inspect frames, then `npm run render -- --output preview.mp4`. Confirm source coverage, sound timing, dimensions and voice clarity in the actual export. All assets are copied locally; no network-dependent source URLs are embedded in the composition.

For a longer or different reel, reuse the SVG drawing approach, sticker entrances, camera-wrapper keyframes and cue structure from `index.html`. Replace the example's headings, diagram and timeline to match the actual ideas. Do not stretch the whole sequence, repeat the same three-sticker diagram regardless of topic, or reuse the original captions on new footage. Sound placements belong to their visible marks; move both together.

The approved sample is the reference for the look and mix. The starter's explicit pop/whoosh/ping inputs allow asset licensing to be respected on another machine; matching those sounds still needs listening review.

## Verified package behaviour

The setup script passed tests for caption escaping and source offsets, local asset resolution, refusal to overwrite an existing project, and rejection of out-of-range caption timing. A fresh project built from the original licensed inputs passed HyperFrames checks with 30/30 contrast samples and rendered at 1080 × 1920, 30 fps, 9.6 seconds with AAC audio. Five review snapshots matched the source project pixel-for-pixel. The decoded audio comparison had correlation 0.999696 and difference RMS −56.02 dBFS; the independently encoded audio was not byte-identical. New content still needs review.
