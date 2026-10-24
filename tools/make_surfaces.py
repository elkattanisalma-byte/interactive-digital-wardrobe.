#!/usr/bin/env python3
"""Render the photographic flat-lay surfaces (one per aesthetic) into images/surfaces/.

Each surface is a real-material texture (linen, marble, oak, concrete, velvet...) with soft
window light, so the cut-out item photos sit on it like a product flat-lay shoot.
Run once; the files are committed. Needs numpy and Pillow.
"""
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

W, H = 600, 800
OUT = Path(__file__).resolve().parent.parent / 'images' / 'surfaces'
R = np.random.default_rng(7)


def noise(scale, w=W, h=H, octaves=4, rng=R):
    """Fractal value noise in [0,1]."""
    acc = np.zeros((h, w)); amp, tot = 1.0, 0.0
    for o in range(octaves):
        sw, sh = max(2, int(w / scale * 2 ** o)), max(2, int(h / scale * 2 ** o))
        n = Image.fromarray((rng.random((sh, sw)) * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
        acc += np.asarray(n, float) / 255 * amp; tot += amp; amp *= .5
    return acc / tot


def light(img, strength=.10, vign=.16):
    """Soft daylight from the top left plus a gentle vignette."""
    y, x = np.mgrid[0:H, 0:W]; x = x / W; y = y / H
    l = 1 + strength * (1 - (x * .6 + y * .8)) - vign * (((x - .5) ** 2 + (y - .45) ** 2) * 2.2)
    return np.clip(img * l[..., None], 0, 255)


def tint(v, c0, c1):
    """Map a [0,1] field to a colour ramp."""
    c0, c1 = np.array(c0, float), np.array(c1, float)
    return c0 + (c1 - c0) * v[..., None]


def weave(c0, c1, thread=3.0, rough=.5):
    """Linen / cotton: crossing threads with slub irregularities."""
    rows = R.random(H)[:, None] * np.ones((1, W)); cols = np.ones((H, 1)) * R.random(W)[None, :]
    rows = np.asarray(Image.fromarray((rows * 255).astype(np.uint8)).filter(ImageFilter.BoxBlur(thread * .3)), float) / 255
    cols = np.asarray(Image.fromarray((cols * 255).astype(np.uint8)).filter(ImageFilter.BoxBlur(thread * .3)), float) / 255
    y, x = np.mgrid[0:H, 0:W]
    grid = (np.sin(x / thread * np.pi) ** 2 * .5 + np.sin(y / thread * np.pi) ** 2 * .5)
    slub = noise(40, octaves=3)
    v = .55 + .18 * (rows - .5) + .18 * (cols - .5) + .12 * (grid - .5) + rough * .25 * (slub - .5)
    return tint(np.clip(v, 0, 1), c0, c1)


def marble(c0, c1, vein):
    t = noise(380, octaves=3) + .15 * noise(60, octaves=3)
    y, x = np.mgrid[0:H, 0:W]
    v = np.abs(np.sin((x * .9 + y * 1.4) / 160 + t * 7))
    fade = np.clip((noise(300, octaves=2) - .35) * 2.5, 0, 1)
    veins = (np.exp(-v * 18) * .9 + np.exp(-v * 4) * .25) * fade
    veins = np.asarray(Image.fromarray((np.clip(veins, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2)), float) / 255
    base = tint(.6 + .4 * noise(180, octaves=5), c0, c1)
    return base * (1 - veins[..., None] * .45) + np.array(vein, float) * veins[..., None] * .45


def wood(c0, c1, plank=150):
    y, x = np.mgrid[0:H, 0:W]
    out = np.zeros((H, W, 3))
    for i, x0 in enumerate(range(0, W, plank)):
        sl = slice(x0, x0 + plank)
        g = np.random.default_rng(i + 3); n = x[:, sl].shape[1]
        t = noise(500, octaves=2, rng=g)[:, sl]
        rings = np.sin((x[:, sl] - x0) / 2.2 + t * 6) * .5 + .5
        cols = g.random(n); streak = np.asarray(Image.fromarray((np.tile(cols, (H, 1)) * 255).astype(np.uint8)).resize((n, H)).filter(ImageFilter.GaussianBlur(.6)), float) / 255
        streak = streak * (.7 + .3 * noise(90, w=n, h=H, octaves=2, rng=g))
        v = .55 + .12 * (rings - .5) + .22 * (streak - .5) + (g.random() - .5) * .14
        out[:, sl] = tint(np.clip(v, 0, 1), c0, c1)
        out[:, x0:x0 + 2] *= .78  # seam between planks
    return out


def concrete(c0, c1, pores=2600):
    v = .5 + .5 * (noise(150, octaves=6) - .5) * 1.6
    img = tint(np.clip(v, 0, 1), c0, c1)
    im = Image.fromarray(img.astype(np.uint8)); d = ImageDraw.Draw(im)
    for _ in range(pores):
        x, y, r = R.random() * W, R.random() * H, R.random() * 1.6 + .3
        d.ellipse((x - r, y - r, x + r, y + r), fill=tuple(int(c * .72) for c in c0))
    return np.asarray(im.filter(ImageFilter.GaussianBlur(.5)), float)


def paper(c0, c1, fibres=1800, fcol=None):
    img = tint(np.clip(.5 + (noise(90, octaves=6) - .5) * 1.3, 0, 1), c0, c1)
    im = Image.fromarray(img.astype(np.uint8)); d = ImageDraw.Draw(im)
    fcol = fcol or tuple(int(c * .9) for c in c0)
    for _ in range(fibres):
        x, y, a, l = R.random() * W, R.random() * H, R.random() * np.pi, R.random() * 9 + 3
        d.line((x, y, x + np.cos(a) * l, y + np.sin(a) * l), fill=fcol, width=1)
    im = Image.blend(Image.fromarray(img.astype(np.uint8)), im, .35)
    return np.asarray(im.filter(ImageFilter.GaussianBlur(.6)), float)


def satin(c0, c1):
    t = noise(300, octaves=3)
    y, x = np.mgrid[0:H, 0:W]
    folds = np.sin((x * .5 + y) / 70 + t * 6) * .5 + .5
    v = .45 + .45 * folds ** 3 + .1 * noise(60, octaves=2)
    return tint(np.clip(v, 0, 1), c0, c1)


def velvet(c0, c1):
    v = noise(220, octaves=4) ** 1.4 * .8 + noise(3, octaves=1) * .2
    return tint(v, c0, c1)


def terrazzo(base0, base1, chips):
    img = tint(.5 + .5 * (noise(120, octaves=4) - .5), base0, base1)
    im = Image.fromarray(img.astype(np.uint8)); d = ImageDraw.Draw(im)
    for _ in range(320):
        x, y, r = R.random() * W, R.random() * H, R.random() * 4 + 1.2
        pts = [(x + np.cos(a) * r * (0.6 + R.random() * .6), y + np.sin(a) * r * (0.6 + R.random() * .6)) for a in np.linspace(0, 2 * np.pi, 6)[:-1] + R.random()]
        d.polygon(pts, fill=chips[R.integers(len(chips))])
    return np.asarray(im.filter(ImageFilter.GaussianBlur(.4)), float)


def iridescent():
    y, x = np.mgrid[0:H, 0:W]; t = noise(260, octaves=3)
    h = (x / W * .5 + y / H * .4 + t * .6) % 1
    stops = np.array([[255, 214, 240], [222, 208, 255], [204, 240, 255], [255, 241, 210], [255, 214, 240]], float)
    p = h * 4; i = p.astype(int); f = (p - i)[..., None]
    img = stops[i] * (1 - f) + stops[np.minimum(i + 1, 4)] * f
    return img * (.94 + .06 * noise(5, octaves=1)[..., None]) + 10


def jute():
    y, x = np.mgrid[0:H, 0:W]; s = 9
    over = ((x // s + y // s) % 2).astype(float)
    tx = np.sin((x % s) / s * np.pi); ty = np.sin((y % s) / s * np.pi)
    v = np.where(over > 0, tx * .6 + .25, ty * .6 + .25) + (noise(30, octaves=3) - .5) * .35 + (R.random((H, W)) - .5) * .12
    return tint(np.clip(v, 0, 1), (150, 116, 74), (222, 196, 150))


SURFACES = {
    'coquette': lambda: satin((238, 196, 205), (255, 240, 243)),
    'romantic': lambda: weave((222, 208, 196), (247, 239, 230), thread=3.2),
    'feminine-chic': lambda: marble((236, 235, 233), (252, 252, 251), (150, 150, 158)),
    'casual': lambda: wood((205, 172, 128), (236, 214, 178)),
    'streetwear': lambda: concrete((150, 149, 145), (205, 204, 199)),
    'y2k': iridescent,
    'old-money': lambda: weave((226, 218, 198), (248, 244, 233), thread=2.4, rough=.3),
    'preppy': lambda: wood((222, 226, 230), (250, 251, 252), plank=120),
    'dark-academia': lambda: paper((196, 172, 130), (234, 218, 186), fibres=900),
    'vintage': lambda: paper((206, 168, 120), (232, 204, 160), fibres=1100, fcol=(176, 140, 98)),
    'boho': jute,
    'minimalist': lambda: paper((236, 236, 233), (246, 246, 244), fibres=300),
    'sporty-chic': lambda: terrazzo((236, 238, 240), (250, 251, 252), [(206, 210, 216), (206, 210, 216), (178, 184, 192), (178, 184, 192), (150, 156, 166), (120, 132, 176), (190, 132, 132)]),
    'elegant': lambda: velvet((14, 12, 12), (58, 48, 44)),
}

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    for name, f in SURFACES.items():
        img = light(f(), strength=.06 if name == 'elegant' else .10, vign=.12 if name == 'elegant' else .16)
        p = OUT / f'{name}.webp'
        Image.fromarray(img.astype(np.uint8)).save(p, 'WEBP', quality=80, method=6)
        print(f'{name:14} {p.stat().st_size // 1024} KB')
