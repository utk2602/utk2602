#!/usr/bin/env python3
"""Turn the GitHub avatar into ascii.svg — the self-typing ASCII portrait.

This is what produced the portrait at the top of the README. The avatar is a
flat, already-matted silhouette, so unlike scripts/make_portrait.py (the full
photo pipeline) it needs no background removal — just a geometric mask.

    pip install pillow numpy
    python3 scripts/avatar_portrait.py avatar.png ascii.svg
    python3 scripts/embed_portrait_font.py      # then inline the ramp font

Same ramp, same 0.600 em grid, same SMIL typing animation as the photo
pipeline, so the two are drop-in interchangeable. Swap to a real photo later
with scripts/make_portrait.py.
"""
import sys

import numpy as np
from PIL import Image

RAMP = " .`:-=+*cs#%@"
COLS = 90
ROW_RATIO = 0.48
FG_LIGHT = "#6e7681"
FG_DARK = "#c9d1d9"
CHAR_W = 7.74
FONT_SIZE = 12.9
LINE_H = 15
ROW_DELAY = 0.09
FAMILY = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"


def prep(path):
    im = Image.open(path).convert("L")
    # The avatar is a dark silhouette inside a white circle on a dark square,
    # and the silhouette touches the circle's rim — so a flood fill would leak
    # into it. Mask by geometry instead: find the white disc, blank everything
    # outside it.
    a = np.asarray(im).astype(np.float32)
    ys, xs = np.nonzero(a > 200)
    if xs.size == 0:
        sys.exit(f"{path}: no white disc to mask by — this script expects a "
                 "dark silhouette on a light circle; for a photo, use "
                 "scripts/make_portrait.py instead")
    cx, cy = (xs.min() + xs.max()) / 2.0, (ys.min() + ys.max()) / 2.0
    r = max(xs.max() - xs.min(), ys.max() - ys.min()) / 2.0
    yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
    a[(xx - cx) ** 2 + (yy - cy) ** 2 > (r - 1) ** 2] = 255
    im = Image.fromarray(a.astype(np.uint8))
    w, h = im.size
    # Crop to the dark content with a small margin.
    inverted = im.point(lambda v: 255 - v)
    bbox = inverted.getbbox()
    if bbox:
        pad = max(2, (bbox[2] - bbox[0]) // 40)
        im = im.crop((max(0, bbox[0] - pad), max(0, bbox[1] - pad),
                      min(w, bbox[2] + pad), min(h, bbox[3] + pad)))
    # Upscale so the LANCZOS downsample to the grid antialiases the edges
    # into intermediate ramp levels instead of hard @/space stairsteps.
    im = im.resize((im.width * 6, im.height * 6), Image.LANCZOS)
    return im


def to_lines(img, cols=COLS):
    w, h = img.size
    rows = max(1, int(cols * (h / w) * ROW_RATIO))
    img = img.resize((cols, rows), Image.LANCZOS)
    px = list(img.getdata())
    n = len(RAMP)
    out = []
    for r in range(rows):
        out.append("".join(
            RAMP[min(n - 1, int((1 - px[r * cols + c] / 255.0) * n))]
            for c in range(cols)
        ).rstrip())
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out


def build_svg(lines, cols=COLS):
    pad = 14
    width = int(cols * CHAR_W + pad * 2)
    height = len(lines) * LINE_H + pad * 2
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
         f'height="{height}" viewBox="0 0 {width} {height}" '
         f'font-family="{FAMILY}">',
         f'<style>.a{{fill:{FG_LIGHT}}}'
         f'@media(prefers-color-scheme:dark){{.a{{fill:{FG_DARK}}}}}</style>']
    for i, line in enumerate(lines):
        y = pad + i * LINE_H
        begin = f"{i * ROW_DELAY:.2f}s"
        end = f"{(i + 1) * ROW_DELAY:.2f}s"
        w = max(len(line), 1) * CHAR_W
        safe = (line.replace("&", "&amp;").replace("<", "&lt;")
                    .replace(">", "&gt;"))
        p.append(f'<clipPath id="c{i}"><rect x="{pad}" y="{y}" '
                 f'height="{LINE_H}" width="0">'
                 f'<animate attributeName="width" from="0" to="{w:.1f}" '
                 f'begin="{begin}" dur="{ROW_DELAY}s" fill="freeze"/>'
                 f'</rect></clipPath>')
        p.append(f'<g clip-path="url(#c{i})"><text xml:space="preserve" '
                 f'x="{pad}" y="{y + 11.2:.1f}" class="a" '
                 f'font-size="{FONT_SIZE}">{safe}</text></g>')
        # the cursor: a small block riding the wipe edge, gone once the row lands
        p.append(f'<rect y="{y + 1}" width="6" height="12" class="a" '
                 f'opacity="0">'
                 f'<animate attributeName="x" from="{pad}" to="{pad + w:.1f}" '
                 f'begin="{begin}" dur="{ROW_DELAY}s" fill="freeze"/>'
                 f'<set attributeName="opacity" to="0.8" begin="{begin}"/>'
                 f'<set attributeName="opacity" to="0" begin="{end}"/></rect>')
    p.append("</svg>")
    return "".join(p)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: avatar_portrait.py <avatar.png> [out.svg] [cols]")
    photo = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "ascii.svg"
    cols = int(sys.argv[3]) if len(sys.argv) > 3 else COLS
    lines = to_lines(prep(photo), cols=cols)
    with open(out, "w", encoding="utf-8") as f:
        f.write(build_svg(lines, cols=cols))
    print(f"wrote {out} — {len(lines)} rows, {cols} columns")
    print("next: python3 scripts/embed_portrait_font.py")


if __name__ == "__main__":
    main()
