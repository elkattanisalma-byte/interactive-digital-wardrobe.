#!/usr/bin/env python3
"""Write docs/photo-prompts.md and docs/photo-sheets.json for the items that still use a drawing.

The descriptions live in docs/photo-descriptions.json (one line per item id); edit them there.
Run again after adding photos: items that already have one in images/capi/ are left out.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / 'index.html').read_text(encoding='utf-8')
data = json.loads(re.search(r'<script type="application/json" id="idw-data">([\s\S]*?)</script>', html).group(1))
DESC = json.loads((ROOT / 'docs' / 'photo-descriptions.json').read_text(encoding='utf-8'))
CATS = data['schema']['categories']
done = {p.stem for p in (ROOT / 'images' / 'capi').iterdir()} if (ROOT / 'images' / 'capi').exists() else set()
todo = [i for c in CATS for i in data['items'] if i['category'] == c and i['id'] not in done]

STYLE = ('Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. '
         'True-to-life colours and realistic fabric texture, fine stitching, natural folds. '
         'No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. '
         'Photorealistic e-commerce product photography, high detail.')
QUARTERS = ['Top-left', 'Top-right', 'Bottom-left', 'Bottom-right']

# Sheet numbers never change once written, so an uploaded sheet-NN always maps to the same items.
SHEETS = ROOT / 'docs' / 'photo-sheets.json'
sheets = json.loads(SHEETS.read_text()) if SHEETS.exists() else {}
covered = {i for ids in sheets.values() for i in ids if i}
fresh = [i for i in todo if i['id'] not in covered]
n = max((int(k.split('-')[1]) for k in sheets), default=0)
for k in range(0, len(fresh), 4):
    n += 1; ids = [i['id'] for i in fresh[k:k + 4]]; sheets[f'sheet-{n:02d}'] = ids + [None] * (4 - len(ids))
open_sheets = {k: v for k, v in sheets.items() if any(i and i not in done for i in v)}


def one(i):
    return (f'Professional e-commerce product photo, flat lay shot from directly above. {DESC[i["id"]]}. '
            f'Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. {STYLE} Square 1:1 format.')


def sheet(ids):
    parts = ' '.join(f'{QUARTERS[p]}: {DESC[i][0].lower() + DESC[i][1:]}.' for p, i in enumerate(ids) if i)
    count = sum(1 for i in ids if i)
    return (f'Professional e-commerce product photo, flat lay shot from directly above, showing {count} separate items arranged in a neat 2x2 grid, '
            f'each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. {parts} '
            f'Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. {STYLE} Square 1:1 format.')


name = {i['id']: i['name'] for i in data['items']}
md = [f'''# Photo prompts for The Interactive Digital Wardrobe

{len(todo)} of {len(data["items"])} items still use a drawing. There are two ways to make their photos — use either, or mix them.

**A. Sheets (faster: {len(open_sheets)} images).** Each prompt below asks for 4 items in one picture (a sheet whose items partly have photos already just replaces them). Save the result as `sheet-NN.png` (the name in the heading). The preparation script cuts out the 4 items and assigns each to the right item from its position in the grid.

**B. One item per image (best detail).** The prompts at the end make one item each. Save as `<item-id>.png`. Recommended for coats, dresses and anything with fine detail.

Then upload the images to `images/upload/` in the repository (GitHub → *Add file → Upload files*) and run `python3 tools/prepare_photos.py` (or ask Claude to do it). The script removes the grey background with a local AI cut-out, crops, optimizes (WebP, 900 px) and links every photo in `index.html`; wardrobe, item panels, outfit flat-lays and printables all use it automatically.

**Check every image:** colours and details as described · each item complete, not cut off by the edge · items not touching (sheets) · nothing extra in the picture (no hangers, hands, text). JPG, PNG or WebP are all fine; the background does not need to be transparent.

## A. Sheets of four''']
for sid, ids in open_sheets.items():
    md.append(f'### `{sid}.png`\n\n' + '\n'.join(f'- {QUARTERS[p]}: **{name[i]}** (`{i}`)' for p, i in enumerate(ids) if i) + f'\n\n```\n{sheet(ids)}\n```')
md.append('## B. One item per image')
for c, cat in CATS.items():
    its = [i for i in todo if i['category'] == c]
    if not its: continue
    md.append(f'### {cat["label"]}')
    md += [f'#### `{i["id"]}.png` — {i["name"]}\n\n```\n{one(i)}\n```' for i in its]
(ROOT / 'docs' / 'photo-prompts.md').write_text('\n\n'.join(md) + '\n', encoding='utf-8')
SHEETS.write_text(json.dumps(sheets, indent=1) + '\n', encoding='utf-8')
print(f'{len(todo)} items without a photo · {len(open_sheets)} sheets to make · docs/photo-prompts.md and docs/photo-sheets.json written')
