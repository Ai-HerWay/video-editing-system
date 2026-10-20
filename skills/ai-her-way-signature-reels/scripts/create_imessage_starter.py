"""Build the 45.4-second iMessage editorial template from local, cleared assets."""
import argparse
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys

SKILL = Path(__file__).resolve().parents[1]
FILES = {
    'presenter': 'presenter.mp4', 'voice': 'voice.wav',
    'message_one': 'today-redacted.mp4', 'message_two': 'lifting-redacted.mp4',
    'message_three': 'protein-redacted.mp4', 'connector': 'connector-safe.mp4',
    'advercase_regular': 'AdvercaseFont-Regular.ttf',
    'advercase_italic': 'Advercase-Font-Italic.ttf',
    'montserrat': 'Montserrat.woff2', 'hand_font': 'SegoePrint.ttf',
    'gsap': 'gsap.min.js', 'pop': 'pop.mp3',
    'ping': 'scene-ping.wav', 'typewriter': 'question-typing.wav',
}

def create(config_path, captions_path, output):
    config_path = Path(config_path).resolve()
    config = json.loads(config_path.read_text(encoding='utf-8-sig'))
    if config.get('privacy_reviewed') is not True:
        raise ValueError('Review and bake privacy masks into all message and connector assets first; set privacy_reviewed to true only after review.')
    inputs = {}
    for key, name in FILES.items():
        value = config.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f'Missing local input: {key}')
        path = Path(value)
        if not path.is_absolute(): path = config_path.parent / path
        if not path.is_file(): raise ValueError(f'Missing file for {key}: {path}')
        if path.suffix.lower() != Path(name).suffix.lower():
            raise ValueError(f'{key} must be {Path(name).suffix}; convert deliberately rather than renaming media.')
        inputs[key] = path.resolve()
    captions = json.loads(Path(captions_path).read_text(encoding='utf-8-sig'))
    if not isinstance(captions, list) or not captions:
        raise ValueError('Provide actual timed caption words.')
    last_end = 0
    for word in captions:
        a, b = float(word['start']), float(word['end'])
        if not (math.isfinite(a) and math.isfinite(b) and last_end <= a < b <= 45.4):
            raise ValueError('Caption times must be finite, ordered, nonoverlapping and within 45.4 seconds.')
        if not isinstance(word['text'], str) or not word['text'].strip():
            raise ValueError('Caption text must be nonempty.')
        last_end = b
    out = Path(output).resolve()
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise ValueError('Use a new or empty output directory; existing work is never overwritten.')
    out.mkdir(parents=True, exist_ok=True)
    assets = out / 'assets'; assets.mkdir(exist_ok=True)
    for key, path in inputs.items(): shutil.copy2(path, assets / FILES[key])
    for path in (SKILL / 'assets/pencil').glob('*.wav'): shutil.copy2(path, assets / path.name)
    for name in ('build_reel.py', 'visual_helpers.py'):
        shutil.copy2(SKILL / 'assets/imessage' / name, out / name)
    (out / 'caption-words.json').write_text(json.dumps(captions, indent=2), encoding='utf-8')
    (out / 'input-manifest.json').write_text(json.dumps({'style_version':'1.3.0','inputs':{k:str(v) for k,v in inputs.items()},'privacy_reviewed':True,'status':'New project; adapt and review before delivery'}, indent=2), encoding='utf-8')
    subprocess.run([sys.executable, str(out / 'build_reel.py')], cwd=out, check=True)
    return out

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets', required=True, type=Path)
    parser.add_argument('--captions', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    try: print(create(args.assets, args.captions, args.out))
    except (ValueError, KeyError, TypeError, OSError) as error: parser.exit(1, f'{error}\n')
