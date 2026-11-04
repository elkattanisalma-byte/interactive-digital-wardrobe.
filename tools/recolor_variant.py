#!/usr/bin/env python3
"""Make a colour variant of an item photo by recolouring it (keeps folds and texture).

    python3 tools/recolor_variant.py images/capi/white-tshirt.webp "#2c3650" images/capi/navy-tshirt.webp

Works best on plain fabrics; for white from a coloured photo, generate a new photo instead."""
import sys, numpy as np
from PIL import Image
def recolor(src, hexc, out):
    im = Image.open(src).convert('RGBA'); a = np.array(im).astype(float)
    rgb = a[..., :3] / 255; alpha = a[..., 3]
    L = 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]
    from PIL import ImageFilter
    C0 = np.array([int(hexc[i:i + 2], 16) for i in (1, 3, 5)]) / 255
    light = (0.2126 * C0[0] + 0.7152 * C0[1] + 0.0722 * C0[2]) > 0.8
    if light:   # smooth the source texture so white fabric does not look grainy
        L = np.array(Image.fromarray((L * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.6))).astype(float) / 255
    m = alpha > 128
    hi = np.percentile(L[m], 92); lo = np.percentile(L[m], 3)
    s = np.clip((L - lo) / max(hi - lo, 1e-3), 0, 1.15)          # fabric shading 0..1 (folds, seams)
    C = np.array([int(hexc[i:i + 2], 16) for i in (1, 3, 5)]) / 255
    lum = 0.2126 * C[0] + 0.7152 * C[1] + 0.0722 * C[2]
    depth = 0.22 if lum > 0.8 else 0.45 if lum > 0.6 else 0.6 if lum > 0.3 else 0.75      # how much the folds darken the colour
    shade = (1 - depth) + depth * s
    res = C[None, None, :] * shade[..., None]
    res += np.clip(s - 1, 0, None)[..., None] * 0.35                # keep soft highlights
    o = np.dstack([np.clip(res, 0, 1) * 255, alpha]).astype(np.uint8)
    Image.fromarray(o, 'RGBA').save(out, 'WEBP', quality=86, method=6)
if __name__ == '__main__':
    recolor(*sys.argv[1:4])
