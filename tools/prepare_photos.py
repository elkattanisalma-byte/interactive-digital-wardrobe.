#!/usr/bin/env python3
"""Turn uploaded clothing photos into optimized cut-outs and link them in index.html.

Upload the generated images to images/upload/ (or the repository root), then run:

    python3 tools/prepare_photos.py

Accepted files:
  * <item-id>.png / .jpg / .webp       one item per image (e.g. black-tshirt.png)
  * sheet-NN.png / .jpg / .webp        four items in a 2x2 grid, as listed in docs/photo-sheets.json
                                       (top-left, top-right, bottom-left, bottom-right)

For every image it:
  * removes the background — keeps real transparency when there is some, otherwise uses the
    local AI cut-out (rembg, `pip install rembg onnxruntime`), otherwise a simple light-background fill,
  * for sheets, finds the four items and assigns each to its grid position,
  * trims the margins, resizes the longest side to 900 px and saves images/capi/<item-id>.webp,
  * rewrites the PHOTOS list in index.html so every photo in images/capi/ is used everywhere
    (wardrobe, item panel, outfit flat-lays, outfit maker, printables).

Options: --force (re-process files already done), --review out.jpg (contact sheet of the results).
Originals are never modified. Needs Pillow (and numpy for rembg).
"""
import json, re, sys
from collections import deque
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / 'index.html'
OUT = ROOT / 'images' / 'capi'
SHEETS = ROOT / 'docs' / 'photo-sheets.json'
EXT = ('.png', '.webp', '.jpg', '.jpeg')
LONG, QUALITY = 900, 86

html = HTML.read_text(encoding='utf-8')
data = json.loads(re.search(r'<script type="application/json" id="idw-data">([\s\S]*?)</script>', html).group(1))
IDS = {i['id'] for i in data['items']}
_session = None


def rembg_cut(im):
    global _session
    try:
        from rembg import remove, new_session
    except ImportError:
        return None
    if _session is None:
        _session = new_session('u2net')
    return remove(im.convert('RGB'), session=_session).convert('RGBA')


def flood_cut(im):
    """Fallback: remove a flat background connected to the border."""
    rgb = im.convert('RGB'); w, h = rgb.size; px = rgb.load()
    ref = px[0, 0]
    bg = lambda p: max(abs(p[0] - ref[0]), abs(p[1] - ref[1]), abs(p[2] - ref[2])) <= 22
    mask = bytearray(w * h); q = deque((x, y) for x in range(w) for y in (0, h - 1))
    q.extend((x, y) for y in range(h) for x in (0, w - 1))
    while q:
        x, y = q.popleft(); i = y * w + x
        if mask[i] or not bg(px[x, y]): continue
        mask[i] = 1
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < w and 0 <= ny < h: q.append((nx, ny))
    alpha = Image.new('L', (w, h)); alpha.putdata([0 if m else 255 for m in mask])
    out = rgb.copy(); out.putalpha(alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.8)))
    return out


def cutout(im):
    im = im.convert('RGBA')
    if im.getchannel('A').getextrema()[0] < 250:
        return im, 'kept transparency'
    cut = rembg_cut(im)
    if cut is not None:
        return cut, 'AI cut-out'
    return flood_cut(im), 'simple cut-out (install rembg for better edges)'


def finish(im, iid):
    bbox = im.getchannel('A').point(lambda v: 255 if v > 20 else 0).getbbox()
    if not bbox:
        raise ValueError('nothing left after removing the background')
    m = 10
    im = im.crop((max(0, bbox[0] - m), max(0, bbox[1] - m), min(im.width, bbox[2] + m), min(im.height, bbox[3] + m)))
    im.thumbnail((LONG, LONG), Image.LANCZOS)
    dst = OUT / f'{iid}.webp'
    im.save(dst, 'WEBP', quality=QUALITY, method=6)
    for old in OUT.glob(f'{iid}.*'):
        if old != dst: old.unlink()
    return dst


def main_region(alpha, keep):
    """Mask of the largest opaque region whose centre lies inside box `keep` (other regions removed)."""
    sc = max(1, max(alpha.size) // 300)
    small = alpha.resize((max(1, alpha.width // sc), max(1, alpha.height // sc))).point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(5))
    w, h = small.size; px = small.load(); seen = bytearray(w * h); best = None
    for sy in range(h):
        for sx in range(w):
            if seen[sy * w + sx] or not px[sx, sy]: continue
            q = deque([(sx, sy)]); seen[sy * w + sx] = 1; pts = []
            while q:
                x, y = q.popleft(); pts.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < w and 0 <= ny < h and not seen[ny * w + nx] and px[nx, ny]:
                        seen[ny * w + nx] = 1; q.append((nx, ny))
            cx = sum(x for x, _ in pts) / len(pts) * sc; cy = sum(y for _, y in pts) / len(pts) * sc
            if keep[0] <= cx < keep[2] and keep[1] <= cy < keep[3] and (best is None or len(pts) > len(best)):
                best = pts
    if not best:
        return None
    m = Image.new('L', (w, h)); mp = m.load()
    for x, y in best: mp[x, y] = 255
    return m.filter(ImageFilter.MaxFilter(3)).resize(alpha.size, Image.BILINEAR)


QUARTERS = ['top-left', 'top-right', 'bottom-left', 'bottom-right']


def split_sheet(src, ids):
    """Cut out each item of a 2x2 sheet separately, from its own quarter of the image."""
    W, H = src.size; out = []; how = ''
    for pos, iid in enumerate(ids):
        if not iid: continue
        qx, qy = (pos % 2) * W // 2, (pos // 2) * H // 2
        pad = W // 10
        box = (max(0, qx - pad), max(0, qy - pad), min(W, qx + W // 2 + pad), min(H, qy + H // 2 + pad))
        part, how = cutout(src.crop(box))
        mask = main_region(part.getchannel('A'), (qx - box[0], qy - box[1], qx - box[0] + W // 2, qy - box[1] + H // 2))
        if mask is None:
            raise ValueError(f'no item found in the {QUARTERS[pos]} quarter ({iid})')
        a = Image.composite(part.getchannel('A'), Image.new('L', part.size), mask)
        part.putalpha(a); out.append((iid, part))
    return out, how


def link_photos():
    """Rewrite the PHOTOS list in index.html from the files in images/capi/."""
    files = {p.stem: p for p in sorted(OUT.iterdir()) if p.suffix.lower() in EXT and p.stem in IDS}
    body = ''.join(f"  '{i}': 'images/capi/{p.name}',\n" for i, p in sorted(files.items()))
    src = HTML.read_text(encoding='utf-8')
    new, n = re.subn(r'(const PHOTOS = \{\n)[\s\S]*?(\};)', lambda m: m.group(1) + body + m.group(2), src, count=1)
    if n != 1:
        raise SystemExit('PHOTOS list not found in index.html')
    if new != src:
        HTML.write_text(new, encoding='utf-8')
    return len(files)


def review(paths, dst):
    cell, cols = 220, 8; rows = (len(paths) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * cell, rows * (cell + 18)), (236, 234, 230)); d = ImageDraw.Draw(sheet)
    for k, p in enumerate(paths):
        im = Image.open(p); im.thumbnail((cell - 16, cell - 16))
        x, y = (k % cols) * cell, (k // cols) * (cell + 18)
        sheet.paste(im, (x + (cell - im.width) // 2, y + (cell - im.height) // 2), im)
        d.text((x + 6, y + cell), p.stem[:34], fill=(60, 50, 40))
    sheet.save(dst, quality=85); print('Review sheet:', dst)


def main(argv):
    force = '--force' in argv
    rev = argv[argv.index('--review') + 1] if '--review' in argv else None
    OUT.mkdir(parents=True, exist_ok=True)
    sheets = json.loads(SHEETS.read_text()) if SHEETS.exists() else {}
    srcs = [p for d in (ROOT, ROOT / 'images' / 'upload') if d.exists() for p in sorted(d.iterdir())
            if p.is_file() and p.suffix.lower() in EXT and (p.stem.lower() in IDS or p.stem.lower() in sheets)]
    done, problems = [], []
    for src in srcs:
        key = src.stem.lower(); ids = [key] if key in IDS else sheets[key]
        outs = [OUT / f'{i}.webp' for i in ids if i]
        if not force and all(o.exists() and o.stat().st_mtime >= src.stat().st_mtime for o in outs):
            continue
        try:
            if key in sheets:
                parts, how = split_sheet(Image.open(src), ids)
            else:
                im, how = cutout(Image.open(src)); parts = [(key, im)]
            for iid, part in parts:
                dst = finish(part, iid); done.append(dst); w, h = Image.open(dst).size
                print(f'{iid:28} {w:>4}x{h:<4} {dst.stat().st_size // 1024:>4} KB  {how}  <- {src.name}')
        except Exception as e:
            problems.append(f'{src.name}: {e}')
    n = link_photos()
    print(f'\n{len(done)} photos prepared · {n} of {len(IDS)} items now use a photo (PHOTOS in index.html updated)')
    for p in problems: print('PROBLEM', p)
    if rev and done: review(done, rev)
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
