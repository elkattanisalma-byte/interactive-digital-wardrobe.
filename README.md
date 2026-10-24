# The Interactive Digital Wardrobe

An interactive fashion ebook in a single web page: an animated wooden wardrobe with 147 pieces, 56 curated outfits in 14 aesthetics, an automatic outfit generator and 15 styling tools. All texts are in English. Everything runs in the browser: no server and no account are needed, and saved looks are stored on the reader's device.

## Open it

Open `index.html` in Safari, Chrome, Edge or Firefox, on a phone or a computer. Keep the `images` folder next to `index.html`, or the three photos will be replaced by their drawings. The fonts load from Google Fonts when online; offline, the page falls back to system fonts.

## Project files

| Path | What it is |
|---|---|
| `index.html` | The whole ebook: styles, page, catalog data (`#idw-data`), consistency check (`#idw-validate`) and app code |
| `images/capi/` | Clothing photos (3 so far) |
| `tools/check-data.mjs` | `node tools/check-data.mjs` — checks every item, outfit and photo link; exits with an error if something is wrong |
| `tools/prepare_photos.py` | `python3 tools/prepare_photos.py` — cleans, trims and resizes uploaded photos and prints the `PHOTOS` lines to paste |
| `docs/photo-prompts.md` | One ready-made prompt and file name for each item that still uses a drawing |

## Add a photo

1. Generate the image with the prompt in `docs/photo-prompts.md` and save it as `<item-id>.png` with a transparent background.
2. Put it in the repository root or in `images/upload/` and run `python3 tools/prepare_photos.py`.
3. Paste the printed line into the `PHOTOS` list near the top of the main script in `index.html`.
4. Run `node tools/check-data.mjs`.

The same photo is used everywhere: wardrobe, item panel, flat-lays, outfit maker and printables. If a file is missing, the drawing is shown instead.

## Edit the catalog

Items and curated outfits live in the JSON block `<script type="application/json" id="idw-data">`, one item per line. A new category, colour or aesthetic is added in `schema`. Run `node tools/check-data.mjs` after every change.

## Sell it as a digital download

Zip `index.html` together with the `images` folder (the `tools` and `docs` folders are not needed by buyers) and upload the zip as the digital file of your listing. Tell buyers to unzip it and open `index.html` in their browser.
