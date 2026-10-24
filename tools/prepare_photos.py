#!/usr/bin/env python3
"""Prepare clothing photos for the ebook.

Put the generated images (PNG with a transparent background, named <item-id>.png,
e.g. black-tshirt.png) anywhere in the repository root or in images/upload/, then run:

    python3 tools/prepare_photos.py

For every file whose name matches an item id it:
  * checks it is a real image and reports whether the background is transparent,
  * removes a light "fake checkerboard" background that some generators draw instead
    of real transparency (only the light grey/white area connected to the border),
  * trims empty margins and resizes the longest side to 1000 px,
  * saves images/capi/<item-id>.png,
  * prints the lines to paste into the PHOTOS list in index.html.

Needs Pillow (pip install pillow). Originals are left untouched.
"""
import json, re, sys
from collections import deque
from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / 'index.html').read_text(encoding='utf-8')
data = json.loads(re.search(r'<script type="application/json" id="idw-data">([\s\S]*?)</script>', html).group(1))
IDS = {i['id'] for i in data['items']}
OUT = ROOT / 'images' / 'capi'
OUT.mkdir(parents=True, exist_ok=True)


def remove_checkerboard(im):
    rgb = im.convert('RGB'); w, h = rgb.size; px = rgb.load()
    bg = lambda p: max(p) - min(p) <= 14 and min(p) >= 175
    mask = bytearray(w * h); q = deque((x, y) for x in range(w) for y in (0, h - 1))
    q.extend((x, y) for y in range(h) for x in (0, w - 1))
    while q:
        x, y = q.popleft(); i = y * w + x
        if mask[i] or not bg(px[x, y]): continue
        mask[i] = 1
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < w and 0 <= ny < h: q.append((nx, ny))
    alpha = Image.new('L', (w, h)); alpha.putdata([0 if m else 255 for m in mask])
    alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.8))
    out = rgb.copy(); out.putalpha(alpha)
    return out, sum(mask) / len(mask)


def main():
    sources = [p for d in (ROOT, ROOT / 'images' / 'upload') if d.exists() for p in d.iterdir()
               if p.suffix.lower() in ('.png', '.webp', '.jpg', '.jpeg') and p.stem.lower() in IDS]
    if not sources:
        print('No photos found. Name them <item-id>.png and put them in the repository root or images/upload/.'); return
    lines = []
    for src in sorted(sources):
        iid = src.stem.lower(); im = Image.open(src)
        im = im.convert('RGBA'); a = im.getchannel('A')
        transparent = a.getextrema()[0] < 250
        note = 'transparent'
        if not transparent:
            im, share = remove_checkerboard(im)
            note = f'no transparency: removed light background ({share:.0%})' if share > .05 else 'WARNING: no transparent background found — regenerate this image'
        bbox = im.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox() or (0, 0) + im.size
        m = 12; im = im.crop((max(0, bbox[0] - m), max(0, bbox[1] - m), min(im.width, bbox[2] + m), min(im.height, bbox[3] + m)))
        im.thumbnail((1000, 1000), Image.LANCZOS)
        dst = OUT / f'{iid}.png'; im.save(dst, optimize=True)
        print(f'{iid:28} {im.size[0]}x{im.size[1]}  {dst.stat().st_size // 1024} KB  {note}')
        lines.append(f"  '{iid}': 'images/capi/{iid}.png',")
    print('\nPaste into PHOTOS in index.html:\n' + '\n'.join(lines))


if __name__ == '__main__':
    sys.exit(main())
