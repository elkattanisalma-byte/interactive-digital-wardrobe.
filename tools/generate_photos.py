#!/usr/bin/env python3
"""Generate item photos with an image API, then hand them to prepare_photos.py.

The API key is read from the environment only (OPENAI_API_KEY or GEMINI_API_KEY) and is never
written to any file. Images go to images/upload/<item-id>.png; items that already have a photo
in images/capi/ or a file in images/upload/ are skipped, so the script can be re-run safely.

  python3 tools/generate_photos.py --list-models                       # free call: checks the key, lists image models
  python3 tools/generate_photos.py --model <id> --dry-run               # prompts + cost estimate, no paid calls
  python3 tools/generate_photos.py --model <id> --ids black-tshirt,navy-blazer,brown-knee-boots
  python3 tools/generate_photos.py --model <id> --limit 30              # next 30 items without a photo

Default provider is Gemini (GEMINI_API_KEY); --provider openai uses OPENAI_API_KEY.
Afterwards run: python3 tools/prepare_photos.py --review check.jpg
"""
import argparse, base64, json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UP, CAPI = ROOT / 'images' / 'upload', ROOT / 'images' / 'capi'
DESC = json.loads((ROOT / 'docs' / 'photo-descriptions.json').read_text(encoding='utf-8'))
html = (ROOT / 'index.html').read_text(encoding='utf-8')
ITEMS = json.loads(re.search(r'<script type="application/json" id="idw-data">([\s\S]*?)</script>', html).group(1))['items']

STYLE = ('Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. '
         'True-to-life colours and realistic fabric texture, fine stitching, natural folds. '
         'No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. '
         'Photorealistic e-commerce product photography, high detail.')
PRICE = {'openai': .053, 'gemini': .05}   # USD per image used for the estimate (--price overrides); check the provider's price page


def prompt(i):
    return (f'Professional e-commerce product photo, flat lay shot from directly above. {DESC[i["id"]]}. '
            f'Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. {STYLE} Square 1:1 format.')


def post(url, body, headers):
    req = urllib.request.Request(url, json.dumps(body).encode(), {'Content-Type': 'application/json', **headers})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())


def openai(p, a):
    r = post('https://api.openai.com/v1/images/generations',
             {'model': a.model or 'gpt-image-1.5', 'prompt': p, 'size': '1024x1024', 'quality': a.quality, 'n': 1},
             {'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY']})
    return base64.b64decode(r['data'][0]['b64_json'])


GEM = 'https://generativelanguage.googleapis.com/v1beta/models'


def gemini(p, a):
    parts = [{'text': p}]
    if a.ref:   # optional style reference: an existing photo whose light and framing the new image should match
        parts = [{'inlineData': {'mimeType': 'image/png', 'data': base64.b64encode(ref_png(a.ref)).decode()}},
                 {'text': 'Use the attached photo only as a reference for photographic style, lighting, background and framing. '
                          'Do not include the item in the reference photo. ' + p}]
    cfg = {'responseModalities': ['IMAGE'], 'imageConfig': {'aspectRatio': '1:1'}}
    if a.size: cfg['imageConfig']['imageSize'] = a.size
    r = post(f'{GEM}/{a.model}:generateContent', {'contents': [{'parts': parts}], 'generationConfig': cfg},
             {'x-goog-api-key': os.environ['GEMINI_API_KEY']})
    for part in r['candidates'][0]['content']['parts']:
        if 'inlineData' in part: return base64.b64decode(part['inlineData']['data'])
    raise RuntimeError('no image in the response')


def ref_png(path):
    """The reference photo flattened onto the grey studio background, as PNG bytes."""
    from io import BytesIO
    from PIL import Image
    im = Image.open(ROOT / path).convert('RGBA'); bg = Image.new('RGBA', im.size, (228, 228, 228, 255)); bg.alpha_composite(im)
    buf = BytesIO(); bg.convert('RGB').save(buf, 'PNG'); return buf.getvalue()


def list_models():
    req = urllib.request.Request(f'{GEM}?pageSize=1000', headers={'x-goog-api-key': os.environ['GEMINI_API_KEY']})
    with urllib.request.urlopen(req, timeout=60) as r:
        ms = json.loads(r.read())['models']
    img = [m['name'].split('/')[-1] for m in ms if 'image' in m['name'].lower() or 'imagen' in m['name'].lower()]
    print(f'Key works: {len(ms)} models visible. Image models:'); print('\n'.join('  ' + m for m in img))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--provider', choices=['openai', 'gemini'], default='gemini')
    ap.add_argument('--model'); ap.add_argument('--quality', default='medium')
    ap.add_argument('--size', help='Gemini output size, e.g. 1K or 2K'); ap.add_argument('--ref', help='style reference photo, e.g. images/capi/white-tshirt.webp')
    ap.add_argument('--price', type=float, help='USD per image for the estimate')
    ap.add_argument('--list-models', action='store_true')
    ap.add_argument('--ids'); ap.add_argument('--limit', type=int)
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    if a.list_models:
        if not os.environ.get('GEMINI_API_KEY'): sys.exit('GEMINI_API_KEY is not set in the environment')
        return list_models()
    if a.provider == 'gemini' and not a.model and not a.dry_run: sys.exit('choose the model with --model (see --list-models)')
    have = {p.stem for d in (CAPI, UP) if d.exists() for p in d.iterdir()}
    todo = [i for i in ITEMS if i['id'] not in have]
    if a.ids: want = a.ids.split(','); todo = [i for i in ITEMS if i['id'] in want]
    if a.limit: todo = todo[:a.limit]
    price = a.price or PRICE[a.provider]
    print(f'{len(todo)} images · about ${len(todo) * price:.2f} with {a.provider} at ${price}/image (estimate, before retries)')
    if a.dry_run:
        for i in todo[:3]: print(f'\n{i["id"]}.png\n{prompt(i)}')
        return 0
    key = {'openai': 'OPENAI_API_KEY', 'gemini': 'GEMINI_API_KEY'}[a.provider]
    if not os.environ.get(key): sys.exit(f'{key} is not set in the environment')
    UP.mkdir(parents=True, exist_ok=True); fails = []
    for n, i in enumerate(todo, 1):
        for attempt in range(3):
            try:
                img = (openai if a.provider == 'openai' else gemini)(prompt(i), a)
                (UP / f'{i["id"]}.png').write_bytes(img); print(f'[{n}/{len(todo)}] {i["id"]} ✓'); break
            except urllib.error.HTTPError as e:
                msg = e.read().decode(errors='replace')[:300]
                if e.code in (401, 403, 400): sys.exit(f'{i["id"]}: HTTP {e.code} {msg}')   # key, verification or billing problem: stop
                time.sleep(10 * (attempt + 1))
            except Exception as e:
                msg = str(e); time.sleep(10 * (attempt + 1))
        else:
            fails.append(i['id']); print(f'[{n}/{len(todo)}] {i["id"]} ✗ {msg}')
    print(f'\nDone: {len(todo) - len(fails)} images in images/upload/. Next: python3 tools/prepare_photos.py --review check.jpg')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
