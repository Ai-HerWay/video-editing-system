"""Create the editable 9.6-second signature sequence from local licensed inputs."""
from pathlib import Path
import argparse, html, json, math, re, shutil

SKILL = Path(__file__).resolve().parents[1]
DURATION = 9.6
REQUIRED = {
    'source': 'source.mp4', 'advercase_regular': 'AdvercaseFont-Regular.ttf',
    'advercase_italic': 'Advercase-Font-Italic.ttf', 'montserrat': 'Montserrat.woff2',
    'gsap': 'gsap.min.js', 'pop': 'pop.mp3', 'whoosh': 'whoosh-short.mp3',
    'ping': 'chime.mp3',
}

def create(config_path, captions_path, output, source_start=0):
    config_path = Path(config_path).resolve()
    config = json.loads(config_path.read_text(encoding='utf-8-sig'))
    if not math.isfinite(source_start) or source_start < 0:
        raise ValueError('source_start must be finite and nonnegative')
    inputs = {}
    for key in REQUIRED:
        value = config.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f'Missing local asset path: {key}')
        path = Path(value)
        if not path.is_absolute(): path = config_path.parent / path
        if not path.is_file(): raise ValueError(f'Asset not found: {key}: {path}')
        inputs[key] = path.resolve()
    captions = json.loads(Path(captions_path).read_text(encoding='utf-8-sig'))
    if not isinstance(captions, list) or not captions:
        raise ValueError('Supply an array of timed caption words for this source range')
    tags = []; last = -1
    for i, word in enumerate(captions):
        start, end = float(word['start']), float(word['end'])
        if not (math.isfinite(start) and math.isfinite(end) and 0 <= start < end <= DURATION + .000001 and start >= last):
            raise ValueError(f'Caption {i} is unordered or outside 0–9.6 seconds')
        if not isinstance(word['text'], str) or not word['text'].strip():
            raise ValueError(f'Caption {i} has no text')
        last = start
        tags.append(f'<div id="cw{i}" class="clip caption" data-start="{start:.3f}" data-duration="{end-start:.3f}" data-track-index="8"><span>{html.escape(word["text"])}</span></div>')
    template = (SKILL/'assets/starter/index.html').read_text(encoding='utf-8')
    assert template.count('<!-- SIGNATURE_CAPTIONS -->') == 1
    template = template.replace('<!-- SIGNATURE_CAPTIONS -->', ''.join(tags))
    template = template.replace('data-media-start="28.2"', f'data-media-start="{source_start:.6f}"')
    # Copy exact bytes with truthful extensions, including alternate video/font formats.
    names = {key: key + inputs[key].suffix.lower() for key in REQUIRED}
    for key, old in REQUIRED.items(): template = template.replace('assets/'+old, 'assets/'+names[key])
    out = Path(output).resolve()
    if out.exists() and any(out.iterdir()):
        raise ValueError('Output must be a new or empty directory; existing edits are never overwritten')
    out.mkdir(parents=True, exist_ok=True); assets = out/'assets'; assets.mkdir(exist_ok=True)
    for key, path in inputs.items(): shutil.copy2(path, assets/names[key])
    for path in (SKILL/'assets/pencil').glob('*.wav'): shutil.copy2(path, assets/path.name)
    (out/'index.html').write_text(template, encoding='utf-8')
    (out/'caption-words.json').write_text(json.dumps(captions, indent=2), encoding='utf-8')
    (out/'package.json').write_text(json.dumps({'name':'signature-reel-starter','private':True,'scripts':{'check':'npx --yes hyperframes@0.8.90 check','render':'npx --yes hyperframes@0.8.90 render'}},indent=2),encoding='utf-8')
    (out/'hyperframes.json').write_text(json.dumps({'paths':{'assets':'assets','blocks':'compositions','components':'compositions/components'},'authoringSkill':'general-video'},indent=2),encoding='utf-8')
    manifest = {'style_version':'1.2.0','source_start':source_start,'duration':DURATION,'inputs':{k:str(v) for k,v in inputs.items()},'status':'starter; new content requires editorial and render review'}
    (out/'input-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    (out/'BRIEF.md').write_text('# Signature reel starter\n\nApproved V7 mechanics, new project. This 9.6-second connected-system scene is a starting sequence, not an automatic full reel. Replace headings, diagram meaning and assets for the actual subject, then adapt the timeline for longer edits. Verify the source contains the requested range. Read the signature skill visual and sound specifications.\n',encoding='utf-8')
    return out

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets', required=True, type=Path, help='JSON mapping local input paths')
    parser.add_argument('--captions', required=True, type=Path, help='JSON words timed relative to the chosen range')
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--source-start', default=0, type=float)
    args = parser.parse_args()
    try: print(create(args.assets, args.captions, args.out, args.source_start))
    except (ValueError, KeyError, TypeError, OSError) as error: parser.exit(1, f'{error}\n')
