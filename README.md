# The Interactive Digital Wardrobe

An interactive fashion ebook in a single web page: an animated wooden wardrobe with 147 pieces, 56 curated outfits in 14 aesthetics, an automatic outfit generator and 15 styling tools. All texts are in English. Everything runs in the browser: no server and no account are needed, and saved looks are stored on the reader's device.

## Open it

Open `index.html` in Safari, Chrome, Edge or Firefox, on a phone or a computer. Keep the `images` folder next to `index.html`, or the three photos will be replaced by their drawings. The fonts load from Google Fonts when online; offline, the page falls back to system fonts.

## Project files

| Path | What it is |
|---|---|
| `index.html` | The whole ebook: styles, page, catalog data (`#idw-data`), consistency check (`#idw-validate`) and app code |
| `images/capi/` | Item photos: transparent WebP cut-outs, 900 px (3 so far) |
| `images/surfaces/` | The photographic flat-lay surface of each aesthetic (made by `tools/make_surfaces.py`) |
| `tools/check-data.mjs` | `node tools/check-data.mjs` — checks every item, outfit and photo link; exits with an error if something is wrong |
| `tools/prepare_photos.py` | `python3 tools/prepare_photos.py` — cuts out, crops and optimizes uploaded photos and links them in `index.html` |
| `tools/photo_prompts.py` | Rewrites `docs/photo-prompts.md` for the items that still have no photo |
| `docs/photo-prompts.md` | Ready-made prompts: 4-item sheets (fast) or one item per image (best detail) |
| `docs/photo-sheets.json` | Which item sits in which quarter of each `sheet-NN` image |

## Add photos

1. Generate the images with the prompts in `docs/photo-prompts.md` — a sheet of four items (`sheet-NN.png`) or a single item (`<item-id>.png`). A plain light grey background is fine; it does not need to be transparent.
2. Upload them to `images/upload/`.
3. Run `python3 tools/prepare_photos.py` (`pip install pillow rembg onnxruntime` first). It removes the background with a local AI cut-out, splits sheets into their four items, saves `images/capi/<item-id>.webp` and updates the `PHOTOS` list in `index.html`. Add `--review check.jpg` to get a contact sheet of the results.
4. Run `node tools/check-data.mjs`, then `python3 tools/photo_prompts.py` to drop the finished items from the prompt list.

The same photo is used everywhere: wardrobe, item panel, outfit flat-lays (composed live on the aesthetic's surface), outfit maker and printables. If a file is missing, the drawing is shown instead.

## Edit the catalog

Items and curated outfits live in the JSON block `<script type="application/json" id="idw-data">`, one item per line. A new category, colour or aesthetic is added in `schema`. Run `node tools/check-data.mjs` after every change.

## Sell it as a digital download

Zip `index.html` together with the `images` folder (the `tools` and `docs` folders are not needed by buyers) and upload the zip as the digital file of your listing. Tell buyers to unzip it and open `index.html` in their browser.
