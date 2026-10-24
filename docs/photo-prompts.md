# Photo prompts for The Interactive Digital Wardrobe

144 of 147 items still use a drawing. There are two ways to make their photos — use either, or mix them.

**A. Sheets (faster: 36 images).** Each prompt below asks for 4 items in one picture (a sheet whose items partly have photos already just replaces them). Save the result as `sheet-NN.png` (the name in the heading). The preparation script cuts out the 4 items and assigns each to the right item from its position in the grid.

**B. One item per image (best detail).** The prompts at the end make one item each. Save as `<item-id>.png`. Recommended for coats, dresses and anything with fine detail.

Then upload the images to `images/upload/` in the repository (GitHub → *Add file → Upload files*) and run `python3 tools/prepare_photos.py` (or ask Claude to do it). The script removes the grey background with a local AI cut-out, crops, optimizes (WebP, 900 px) and links every photo in `index.html`; wardrobe, item panels, outfit flat-lays and printables all use it automatically.

**Check every image:** colours and details as described · each item complete, not cut off by the edge · items not touching (sheets) · nothing extra in the picture (no hangers, hands, text). JPG, PNG or WebP are all fine; the background does not need to be transparent.

## A. Sheets of four

### `sheet-01.png`

- Top-left: **Black T-shirt** (`black-tshirt`)
- Top-right: **Grey Oversized T-shirt** (`grey-oversized-tshirt`)
- Bottom-left: **Striped T-shirt** (`striped-tshirt`)
- Bottom-right: **Pink Baby Tee** (`pink-baby-tee`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a black t-shirt — short sleeves, crew neck, black. Top-right: a grey oversized t-shirt — short sleeves, crew neck, grey, oversized fit. Bottom-left: a striped t-shirt — short sleeves, crew neck, navy, stripe pattern. Bottom-right: a pink baby tee — small fitted baby tee, short cap sleeves, cropped at the waist, pink, cropped fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-02.png`

- Top-left: **White Tank Top** (`white-tank-top`)
- Top-right: **Black Fitted Top** (`black-fitted-top`)
- Bottom-left: **Ivory Lace Cami** (`ivory-lace-cami`)
- Bottom-right: **Champagne Satin Cami** (`champagne-satin-cami`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a white tank top — ribbed jersey, wide straps, white, fitted fit. Top-right: a black fitted top — ribbed jersey, wide straps, black, fitted fit. Bottom-left: a ivory lace cami — thin spaghetti straps, ivory, lace pattern, fitted fit. Bottom-right: a champagne satin cami — thin spaghetti straps, champagne, fitted fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-03.png`

- Top-left: **Pink Corset Top** (`pink-corset-top`)
- Top-right: **White Crop Top** (`white-crop-top`)
- Bottom-left: **Lilac Halter Top** (`lilac-halter-top`)
- Bottom-right: **Black Long-Sleeve Top** (`black-long-sleeve-top`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a pink corset top — sweetheart neckline, visible boning, lace-up front, pink, fitted fit. Top-right: a white crop top — boxy cropped fit, short sleeves, white, cropped fit. Bottom-left: a lilac halter top — halter neck tie, lilac, fitted fit. Bottom-right: a black long-sleeve top — fitted long sleeves, crew neck, black, fitted fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-04.png`

- Top-left: **White Off-Shoulder Top** (`white-off-shoulder-top`)
- Top-right: **White Polo Shirt** (`white-polo-shirt`)
- Bottom-left: **Grey Hoodie** (`grey-hoodie`)
- Bottom-right: **White Shirt** (`white-shirt`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a white off-shoulder top — ruffled off-the-shoulder neckline, white, relaxed fit. Top-right: a white polo shirt — piqué cotton, ribbed collar, two-button placket, white. Bottom-left: a grey hoodie — kangaroo pocket, drawstring hood, ribbed cuffs, grey, oversized fit. Bottom-right: a white shirt — button-down shirt with collar, white. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-05.png`

- Top-left: **Light Blue Shirt** (`light-blue-shirt`)
- Top-right: **Blue Pinstripe Shirt** (`blue-pinstripe-shirt`)
- Bottom-left: **Cream Silk Blouse** (`cream-silk-blouse`)
- Bottom-right: **White Ruffle Blouse** (`white-ruffle-blouse`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a light blue shirt — button-down shirt with collar, light blue, relaxed fit. Top-right: a blue pinstripe shirt — button-down shirt with collar, light blue, pinstripe pattern, oversized fit. Bottom-left: a cream silk blouse — fluid silk, soft V neckline, long sleeves, cream, relaxed fit. Bottom-right: a white ruffle blouse — ruffled placket and collar, long sleeves, white. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-06.png`

- Top-left: **Pink Puff-Sleeve Blouse** (`pink-puff-sleeve-blouse`)
- Top-right: **Cream Peter Pan Blouse** (`cream-peter-pan-blouse`)
- Bottom-left: **Red Plaid Shirt** (`red-plaid-shirt`)
- Bottom-right: **Denim Shirt** (`denim-shirt`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a pink puff-sleeve blouse — puffed short sleeves, buttoned front, pink, fitted fit. Top-right: a cream peter pan blouse — rounded Peter Pan collar, buttoned front, cream. Bottom-left: a red plaid shirt — button-down shirt with collar, red, plaid pattern, oversized fit. Bottom-right: a denim shirt — button-down shirt with collar, denim, relaxed fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-07.png`

- Top-left: **Black Satin Shirt** (`black-satin-shirt`)
- Top-right: **Cream Knit Sweater** (`cream-knit-sweater`)
- Bottom-left: **Grey Sweater** (`grey-sweater`)
- Bottom-right: **Burgundy Sweater** (`burgundy-sweater`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a black satin shirt — button-down shirt with collar, black, relaxed fit. Top-right: a cream knit sweater — knit crew-neck sweater, ribbed cuffs and hem, cream, cable pattern, relaxed fit. Bottom-left: a grey sweater — knit crew-neck sweater, ribbed cuffs and hem, grey, oversized fit. Bottom-right: a burgundy sweater — knit crew-neck sweater, ribbed cuffs and hem, burgundy. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-08.png`

- Top-left: **Pink Knit** (`pink-knit`)
- Top-right: **Cream Cardigan** (`cream-cardigan`)
- Bottom-left: **Pink Cropped Cardigan** (`pink-cropped-cardigan`)
- Bottom-right: **Mustard Cardigan** (`mustard-cardigan`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a pink knit — knit crew-neck sweater, ribbed cuffs and hem, pink. Top-right: a cream cardigan — button-front knit cardigan, V neck, cream, relaxed fit. Bottom-left: a pink cropped cardigan — cropped button-front knit cardigan, pink, cropped fit. Bottom-right: a mustard cardigan — button-front knit cardigan, V neck, mustard. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-09.png`

- Top-left: **Navy Cable Sweater** (`navy-cable-sweater`)
- Top-right: **Camel Turtleneck** (`camel-turtleneck`)
- Bottom-left: **Black Turtleneck** (`black-turtleneck`)
- Bottom-right: **Brown Argyle Vest** (`brown-argyle-vest`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a navy cable sweater — knit crew-neck sweater, ribbed cuffs and hem, navy, cable pattern. Top-right: a camel turtleneck — fine-knit turtleneck, camel, fitted fit. Bottom-left: a black turtleneck — fine-knit turtleneck, black, fitted fit. Bottom-right: a brown argyle vest — sleeveless V-neck sweater vest, brown, argyle pattern. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-10.png`

- Top-left: **Cream Cable Vest** (`cream-cable-vest`)
- Top-right: **Beige Blazer** (`beige-blazer`)
- Bottom-left: **Black Blazer** (`black-blazer`)
- Bottom-right: **Navy Blazer** (`navy-blazer`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a cream cable vest — sleeveless V-neck sweater vest, cream, cable pattern. Top-right: a beige blazer — single-breasted tailored blazer, notch lapels, beige. Bottom-left: a black blazer — single-breasted tailored blazer, notch lapels, black. Bottom-right: a navy blazer — single-breasted tailored blazer, notch lapels, navy. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-11.png`

- Top-left: **Brown Tweed Blazer** (`brown-tweed-blazer`)
- Top-right: **Grey Oversized Blazer** (`grey-oversized-blazer`)
- Bottom-left: **Denim Jacket** (`denim-jacket`)
- Bottom-right: **Black Leather Jacket** (`black-leather-jacket`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a brown tweed blazer — single-breasted tailored blazer, notch lapels, brown, tweed pattern. Top-right: a grey oversized blazer — single-breasted tailored blazer, notch lapels, grey, oversized fit. Bottom-left: a denim jacket — classic trucker jacket, chest pockets, metal buttons, denim. Bottom-right: a black leather jacket — leather biker jacket, asymmetric zip, belted hem, black, fitted fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-12.png`

- Top-left: **Olive Bomber Jacket** (`olive-bomber-jacket`)
- Top-right: **Cream Tweed Jacket** (`cream-tweed-jacket`)
- Bottom-left: **White Track Jacket** (`white-track-jacket`)
- Bottom-right: **Brown Suede Jacket** (`brown-suede-jacket`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a olive bomber jacket — bomber jacket, ribbed collar, cuffs and hem, zip front, olive, oversized fit. Top-right: a cream tweed jacket — cropped collarless tweed jacket, contrast trim, gold buttons, cream, tweed pattern, cropped fit. Bottom-left: a white track jacket — zip-up track jacket with contrast stripes along the sleeves, white. Bottom-right: a brown suede jacket — suede jacket with fringe across the chest, brown. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-13.png`

- Top-left: **Black Puffer Jacket** (`black-puffer-jacket`)
- Top-right: **Navy Coat** (`navy-coat`)
- Bottom-left: **Beige Trench Coat** (`beige-trench-coat`)
- Bottom-right: **Black Wool Coat** (`black-wool-coat`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a black puffer jacket — oversized quilted puffer jacket, high collar, black, oversized fit. Top-right: a navy coat — long double-breasted coat, navy. Bottom-left: a beige trench coat — double-breasted trench coat with belt and epaulettes, beige. Bottom-right: a black wool coat — long single-breasted wool coat, black. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-14.png`

- Top-left: **Cream Teddy Coat** (`cream-teddy-coat`)
- Top-right: **Little Black Dress** (`little-black-dress`)
- Bottom-left: **Burgundy Dress** (`burgundy-dress`)
- Bottom-right: **Sage Midi Dress** (`sage-midi-dress`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a cream teddy coat — oversized fluffy teddy coat, wide collar, cream, oversized fit. Top-right: a little black dress — sleeveless fitted sheath dress, knee length, black, fitted fit. Bottom-left: a burgundy dress — wrap midi dress, short sleeves, tie waist, burgundy. Bottom-right: a sage midi dress — bias-cut slip dress, thin straps, sage, relaxed fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-15.png`

- Top-left: **White Sundress** (`white-sundress`)
- Top-right: **Pink Floral Mini Dress** (`pink-floral-mini-dress`)
- Bottom-left: **Cream Lace Maxi Dress** (`cream-lace-maxi-dress`)
- Bottom-right: **Red Gingham Dress** (`red-gingham-dress`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a white sundress — sundress with thin straps, fitted bodice, flared skirt, white, eyelet pattern, relaxed fit. Top-right: a pink floral mini dress — mini dress with puff sleeves and a flared skirt, pink, floral pattern, fitted fit. Bottom-left: a cream lace maxi dress — flowing maxi dress with flutter sleeves, cream, lace pattern, relaxed fit. Bottom-right: a red gingham dress — tea dress, short sleeves, fitted waist, flared midi skirt, red, gingham pattern. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-16.png`

- Top-left: **Red Satin Slip Dress** (`red-satin-slip-dress`)
- Top-right: **Navy Polka Dot Dress** (`navy-polka-dot-dress`)
- Bottom-left: **Black Knit Midi Dress** (`black-knit-midi-dress`)
- Bottom-right: **White Tennis Dress** (`white-tennis-dress`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a red satin slip dress — bias-cut slip dress, thin straps, red, fitted fit. Top-right: a navy polka dot dress — tea dress, short sleeves, fitted waist, flared midi skirt, navy, polka pattern. Bottom-left: a black knit midi dress — long-sleeve knit midi dress, black, fitted fit. Bottom-right: a white tennis dress — sleeveless tennis dress, pleated skirt, polo collar, white, fitted fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-17.png`

- Top-left: **Brown Shirt Dress** (`brown-shirt-dress`)
- Top-right: **Black Wide-Leg Jumpsuit** (`black-wide-leg-jumpsuit`)
- Bottom-left: **Olive Utility Jumpsuit** (`olive-utility-jumpsuit`)
- Bottom-right: **White Linen Jumpsuit** (`white-linen-jumpsuit`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a brown shirt dress — collared midi shirt dress with belt, brown. Top-right: a black wide-leg jumpsuit — jumpsuit with wide legs, black. Bottom-left: a olive utility jumpsuit — utility jumpsuit, short sleeves, chest pockets, belt, olive, relaxed fit. Bottom-right: a white linen jumpsuit — jumpsuit with wide legs, white, relaxed fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-18.png`

- Top-left: **Straight Jeans** (`straight-jeans`)
- Top-right: **Mom Jeans** (`mom-jeans`)
- Bottom-left: **Dark Flared Jeans** (`dark-flared-jeans`)
- Bottom-right: **Baggy Jeans** (`baggy-jeans`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a straight jeans — five-pocket straight-leg jeans, denim. Top-right: a mom jeans — high-waisted tapered mom jeans with rolled hems, denim, relaxed fit. Bottom-left: a dark flared jeans — flared jeans, denim. Bottom-right: a baggy jeans — baggy relaxed jeans, denim, oversized fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-19.png`

- Top-left: **Black Skinny Jeans** (`black-skinny-jeans`)
- Top-right: **White Straight Jeans** (`white-straight-jeans`)
- Bottom-left: **Low-Rise Flare Jeans** (`low-rise-flare-jeans`)
- Bottom-right: **Black Tailored Trousers** (`black-tailored-trousers`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a black skinny jeans — skinny jeans, black, fitted fit. Top-right: a white straight jeans — five-pocket straight-leg jeans, white. Bottom-left: a low-rise flare jeans — low-rise flared jeans, denim, fitted fit. Bottom-right: a black tailored trousers — tailored straight trousers with pressed creases, black. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-20.png`

- Top-left: **Beige Wide Trousers** (`beige-wide-trousers`)
- Top-right: **Olive Trousers** (`olive-trousers`)
- Bottom-left: **Grey Wool Trousers** (`grey-wool-trousers`)
- Bottom-right: **Cream Linen Trousers** (`cream-linen-trousers`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a beige wide trousers — high-waisted wide-leg trousers, beige, relaxed fit. Top-right: a olive trousers — relaxed trousers, olive, relaxed fit. Bottom-left: a grey wool trousers — tailored straight trousers with pressed creases, charcoal. Bottom-right: a cream linen trousers — high-waisted wide-leg trousers, cream, relaxed fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-21.png`

- Top-left: **Navy Sailor Trousers** (`navy-sailor-trousers`)
- Top-right: **Khaki Cargo Pants** (`khaki-cargo-pants`)
- Bottom-left: **Brown Check Trousers** (`brown-check-trousers`)
- Bottom-right: **Black Flare Leggings** (`black-flare-leggings`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a navy sailor trousers — wide sailor trousers with a buttoned front panel, navy. Top-right: a khaki cargo pants — cargo pants with side pockets, khaki, oversized fit. Bottom-left: a brown check trousers — tailored straight trousers with pressed creases, brown, check pattern. Bottom-right: a black flare leggings — flared leggings, black, fitted fit. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-22.png`

- Top-left: **Grey Joggers** (`grey-joggers`)
- Top-right: **Beige Midi Skirt** (`beige-midi-skirt`)
- Bottom-left: **Black Midi Skirt** (`black-midi-skirt`)
- Bottom-right: **Brown Corduroy Skirt** (`brown-corduroy-skirt`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a grey joggers — joggers with elastic cuffs and drawstring, grey, relaxed fit. Top-right: a beige midi skirt — pleated midi skirt, beige. Bottom-left: a black midi skirt — satin slip midi skirt, black. Bottom-right: a brown corduroy skirt — buttoned A-line midi skirt, brown. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-23.png`

- Top-left: **Denim Mini Skirt** (`denim-mini-skirt`)
- Top-right: **Pink Ruffle Mini Skirt** (`pink-ruffle-mini-skirt`)
- Bottom-left: **Navy Pleated Mini Skirt** (`navy-pleated-mini-skirt`)
- Bottom-right: **Brown Plaid Midi Skirt** (`brown-plaid-midi-skirt`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a denim mini skirt — five-pocket mini skirt, denim, fitted fit. Top-right: a pink ruffle mini skirt — tiered ruffle mini skirt, pink. Bottom-left: a navy pleated mini skirt — pleated mini skirt, navy. Bottom-right: a brown plaid midi skirt — pleated midi skirt, brown, plaid pattern. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-24.png`

- Top-left: **White Tennis Skirt** (`white-tennis-skirt`)
- Top-right: **Rust Tiered Maxi Skirt** (`rust-tiered-maxi-skirt`)
- Bottom-left: **Champagne Satin Skirt** (`champagne-satin-skirt`)
- Bottom-right: **Denim Shorts** (`denim-shorts`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a white tennis skirt — pleated tennis skirt, white. Top-right: a rust tiered maxi skirt — tiered maxi skirt, rust, relaxed fit. Bottom-left: a champagne satin skirt — satin slip midi skirt, champagne. Bottom-right: a denim shorts — frayed denim shorts, denim. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-25.png`

- Top-left: **White Linen Shorts** (`white-linen-shorts`)
- Top-right: **Black Tailored Shorts** (`black-tailored-shorts`)
- Bottom-left: **Black Bike Shorts** (`black-bike-shorts`)
- Bottom-right: **Khaki Bermuda Shorts** (`khaki-bermuda-shorts`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a white linen shorts — drawstring linen shorts, white, relaxed fit. Top-right: a black tailored shorts — tailored shorts with pressed creases, black. Bottom-left: a black bike shorts — fitted bike shorts, black, fitted fit. Bottom-right: a khaki bermuda shorts — knee-length Bermuda shorts, khaki. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-26.png`

- Top-left: **White Sneakers** (`white-sneakers`)
- Top-right: **Black Loafers** (`black-loafers`)
- Bottom-left: **Brown Loafers** (`brown-loafers`)
- Bottom-right: **Brown Ankle Boots** (`brown-ankle-boots`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a white sneakers — pair of low-top leather sneakers, white. Top-right: a black loafers — pair of leather penny loafers, black. Bottom-left: a brown loafers — pair of leather penny loafers, brown. Bottom-right: a brown ankle boots — pair of leather ankle boots with block heel, brown. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-27.png`

- Top-left: **Black Ankle Boots** (`black-ankle-boots`)
- Top-right: **Black Heels** (`black-heels`)
- Bottom-left: **Beige Ballet Flats** (`beige-ballet-flats`)
- Bottom-right: **Pink Ballet Flats** (`pink-ballet-flats`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a black ankle boots — pair of leather ankle boots with block heel, black. Top-right: a black heels — pair of pointed-toe pumps, black. Bottom-left: a beige ballet flats — pair of ballet flats, beige. Bottom-right: a pink ballet flats — pair of ballet flats, pink. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-28.png`

- Top-left: **Black Mary Janes** (`black-mary-janes`)
- Top-right: **Cream Slingbacks** (`cream-slingbacks`)
- Bottom-left: **Gold Strappy Sandals** (`gold-strappy-sandals`)
- Bottom-right: **Tan Flat Sandals** (`tan-flat-sandals`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a black mary janes — pair of Mary Jane flats with buckle strap, black. Top-right: a cream slingbacks — pair of slingback kitten heels, cream. Bottom-left: a gold strappy sandals — pair of strappy heeled sandals, gold. Bottom-right: a tan flat sandals — pair of flat leather sandals, tan. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-29.png`

- Top-left: **Brown Knee Boots** (`brown-knee-boots`)
- Top-right: **Black Combat Boots** (`black-combat-boots`)
- Bottom-left: **Retro Running Sneakers** (`retro-running-sneakers`)
- Bottom-right: **White Platform Sneakers** (`white-platform-sneakers`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a brown knee boots — pair of knee-high leather boots, brown. Top-right: a black combat boots — pair of lace-up combat boots with chunky sole, black. Bottom-left: a retro running sneakers — pair of retro running sneakers, grey. Bottom-right: a white platform sneakers — pair of platform sneakers, white. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-30.png`

- Top-left: **Black Shoulder Bag** (`black-shoulder-bag`)
- Top-right: **Tan Shoulder Bag** (`tan-shoulder-bag`)
- Bottom-left: **Camel Tote** (`camel-tote`)
- Bottom-right: **Black Tote** (`black-tote`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a black shoulder bag — structured shoulder bag with flap, black. Top-right: a tan shoulder bag — structured shoulder bag with flap, tan. Bottom-left: a camel tote — leather tote bag, camel. Bottom-right: a black tote — leather tote bag, black. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-31.png`

- Top-left: **Pink Baguette Bag** (`pink-baguette-bag`)
- Top-right: **Straw Basket Bag** (`straw-basket-bag`)
- Bottom-left: **Black Crossbody Bag** (`black-crossbody-bag`)
- Bottom-right: **Brown Satchel** (`brown-satchel`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a pink baguette bag — small baguette bag, pink. Top-right: a straw basket bag — woven straw basket bag with leather handles, tan, woven pattern. Bottom-left: a black crossbody bag — small crossbody bag with long strap, black. Bottom-right: a brown satchel — leather satchel with buckled flap, brown. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-32.png`

- Top-left: **Black Quilted Bag** (`black-quilted-bag`)
- Top-right: **Gold Clutch** (`gold-clutch`)
- Bottom-left: **Black Sunglasses** (`black-sunglasses`)
- Bottom-right: **Pink Tinted Sunglasses** (`pink-tinted-sunglasses`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a black quilted bag — quilted leather bag with chain strap, black, quilted pattern. Top-right: a gold clutch — envelope clutch, gold. Bottom-left: a black sunglasses — pair of glasses, black. Bottom-right: a pink tinted sunglasses — pair of glasses, pink. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-33.png`

- Top-left: **Cat-Eye Sunglasses** (`cat-eye-sunglasses`)
- Top-right: **Tortoiseshell Glasses** (`tortoiseshell-glasses`)
- Bottom-left: **Gold Hoops** (`gold-hoops`)
- Bottom-right: **Pearl Earrings** (`pearl-earrings`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a cat-eye sunglasses — pair of glasses, black. Top-right: a tortoiseshell glasses — pair of glasses, brown, tortoiseshell pattern. Bottom-left: a gold hoops — pair of earrings, gold. Bottom-right: a pearl earrings — pair of earrings, ivory. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-34.png`

- Top-left: **Pearl Necklace** (`pearl-necklace`)
- Top-right: **Gold Chain Necklace** (`gold-chain-necklace`)
- Bottom-left: **Gold Watch** (`gold-watch`)
- Bottom-right: **Burgundy Scarf** (`burgundy-scarf`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a pearl necklace — necklace, ivory. Top-right: a gold chain necklace — necklace, gold. Bottom-left: a gold watch — wristwatch, gold. Bottom-right: a burgundy scarf — long knitted wool scarf, burgundy. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-35.png`

- Top-left: **Red Silk Neck Scarf** (`red-silk-neck-scarf`)
- Top-right: **Silk Headscarf** (`silk-headscarf`)
- Bottom-left: **Pink Hair Bow** (`pink-hair-bow`)
- Bottom-right: **Black Hair Bow** (`black-hair-bow`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a red silk neck scarf — small silk neck scarf, knotted, red. Top-right: a silk headscarf — square printed silk scarf, folded, cream, print pattern. Bottom-left: a pink hair bow — satin hair bow, pink. Bottom-right: a black hair bow — satin hair bow, black. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### `sheet-36.png`

- Top-left: **Black Baseball Cap** (`black-baseball-cap`)
- Top-right: **Straw Sun Hat** (`straw-sun-hat`)
- Bottom-left: **Brown Belt** (`brown-belt`)
- Bottom-right: **Black Belt** (`black-belt`)

```
Professional e-commerce product photo, flat lay shot from directly above, showing 4 separate items arranged in a neat 2x2 grid, each item centred in its own quarter of the image with wide empty space around it — the items never touch or overlap. Top-left: a black baseball cap — cotton baseball cap, black. Top-right: a straw sun hat — wide-brim straw sun hat, tan, woven pattern. Bottom-left: a brown belt — leather belt with buckle, brown. Bottom-right: a black belt — leather belt with buckle, black. Every item complete and fully visible, laid flat, front side up, shown at a natural relative scale. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

## B. One item per image

### Tops

#### `black-tshirt.png` — Black T-shirt

```
Professional e-commerce product photo, flat lay shot from directly above. A black t-shirt — short sleeves, crew neck, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `grey-oversized-tshirt.png` — Grey Oversized T-shirt

```
Professional e-commerce product photo, flat lay shot from directly above. A grey oversized t-shirt — short sleeves, crew neck, grey, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `striped-tshirt.png` — Striped T-shirt

```
Professional e-commerce product photo, flat lay shot from directly above. A striped t-shirt — short sleeves, crew neck, navy, stripe pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-baby-tee.png` — Pink Baby Tee

```
Professional e-commerce product photo, flat lay shot from directly above. A pink baby tee — small fitted baby tee, short cap sleeves, cropped at the waist, pink, cropped fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-tank-top.png` — White Tank Top

```
Professional e-commerce product photo, flat lay shot from directly above. A white tank top — ribbed jersey, wide straps, white, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-fitted-top.png` — Black Fitted Top

```
Professional e-commerce product photo, flat lay shot from directly above. A black fitted top — ribbed jersey, wide straps, black, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `ivory-lace-cami.png` — Ivory Lace Cami

```
Professional e-commerce product photo, flat lay shot from directly above. A ivory lace cami — thin spaghetti straps, ivory, lace pattern, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `champagne-satin-cami.png` — Champagne Satin Cami

```
Professional e-commerce product photo, flat lay shot from directly above. A champagne satin cami — thin spaghetti straps, champagne, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-corset-top.png` — Pink Corset Top

```
Professional e-commerce product photo, flat lay shot from directly above. A pink corset top — sweetheart neckline, visible boning, lace-up front, pink, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-crop-top.png` — White Crop Top

```
Professional e-commerce product photo, flat lay shot from directly above. A white crop top — boxy cropped fit, short sleeves, white, cropped fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `lilac-halter-top.png` — Lilac Halter Top

```
Professional e-commerce product photo, flat lay shot from directly above. A lilac halter top — halter neck tie, lilac, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-long-sleeve-top.png` — Black Long-Sleeve Top

```
Professional e-commerce product photo, flat lay shot from directly above. A black long-sleeve top — fitted long sleeves, crew neck, black, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-off-shoulder-top.png` — White Off-Shoulder Top

```
Professional e-commerce product photo, flat lay shot from directly above. A white off-shoulder top — ruffled off-the-shoulder neckline, white, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-polo-shirt.png` — White Polo Shirt

```
Professional e-commerce product photo, flat lay shot from directly above. A white polo shirt — piqué cotton, ribbed collar, two-button placket, white. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `grey-hoodie.png` — Grey Hoodie

```
Professional e-commerce product photo, flat lay shot from directly above. A grey hoodie — kangaroo pocket, drawstring hood, ribbed cuffs, grey, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Shirts

#### `white-shirt.png` — White Shirt

```
Professional e-commerce product photo, flat lay shot from directly above. A white shirt — button-down shirt with collar, white. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `light-blue-shirt.png` — Light Blue Shirt

```
Professional e-commerce product photo, flat lay shot from directly above. A light blue shirt — button-down shirt with collar, light blue, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `blue-pinstripe-shirt.png` — Blue Pinstripe Shirt

```
Professional e-commerce product photo, flat lay shot from directly above. A blue pinstripe shirt — button-down shirt with collar, light blue, pinstripe pattern, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `cream-silk-blouse.png` — Cream Silk Blouse

```
Professional e-commerce product photo, flat lay shot from directly above. A cream silk blouse — fluid silk, soft V neckline, long sleeves, cream, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-ruffle-blouse.png` — White Ruffle Blouse

```
Professional e-commerce product photo, flat lay shot from directly above. A white ruffle blouse — ruffled placket and collar, long sleeves, white. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-puff-sleeve-blouse.png` — Pink Puff-Sleeve Blouse

```
Professional e-commerce product photo, flat lay shot from directly above. A pink puff-sleeve blouse — puffed short sleeves, buttoned front, pink, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `cream-peter-pan-blouse.png` — Cream Peter Pan Blouse

```
Professional e-commerce product photo, flat lay shot from directly above. A cream peter pan blouse — rounded Peter Pan collar, buttoned front, cream. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `red-plaid-shirt.png` — Red Plaid Shirt

```
Professional e-commerce product photo, flat lay shot from directly above. A red plaid shirt — button-down shirt with collar, red, plaid pattern, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `denim-shirt.png` — Denim Shirt

```
Professional e-commerce product photo, flat lay shot from directly above. A denim shirt — button-down shirt with collar, denim, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-satin-shirt.png` — Black Satin Shirt

```
Professional e-commerce product photo, flat lay shot from directly above. A black satin shirt — button-down shirt with collar, black, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Knitwear

#### `cream-knit-sweater.png` — Cream Knit Sweater

```
Professional e-commerce product photo, flat lay shot from directly above. A cream knit sweater — knit crew-neck sweater, ribbed cuffs and hem, cream, cable pattern, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `grey-sweater.png` — Grey Sweater

```
Professional e-commerce product photo, flat lay shot from directly above. A grey sweater — knit crew-neck sweater, ribbed cuffs and hem, grey, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `burgundy-sweater.png` — Burgundy Sweater

```
Professional e-commerce product photo, flat lay shot from directly above. A burgundy sweater — knit crew-neck sweater, ribbed cuffs and hem, burgundy. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-knit.png` — Pink Knit

```
Professional e-commerce product photo, flat lay shot from directly above. A pink knit — knit crew-neck sweater, ribbed cuffs and hem, pink. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `cream-cardigan.png` — Cream Cardigan

```
Professional e-commerce product photo, flat lay shot from directly above. A cream cardigan — button-front knit cardigan, V neck, cream, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-cropped-cardigan.png` — Pink Cropped Cardigan

```
Professional e-commerce product photo, flat lay shot from directly above. A pink cropped cardigan — cropped button-front knit cardigan, pink, cropped fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `mustard-cardigan.png` — Mustard Cardigan

```
Professional e-commerce product photo, flat lay shot from directly above. A mustard cardigan — button-front knit cardigan, V neck, mustard. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `navy-cable-sweater.png` — Navy Cable Sweater

```
Professional e-commerce product photo, flat lay shot from directly above. A navy cable sweater — knit crew-neck sweater, ribbed cuffs and hem, navy, cable pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `camel-turtleneck.png` — Camel Turtleneck

```
Professional e-commerce product photo, flat lay shot from directly above. A camel turtleneck — fine-knit turtleneck, camel, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-turtleneck.png` — Black Turtleneck

```
Professional e-commerce product photo, flat lay shot from directly above. A black turtleneck — fine-knit turtleneck, black, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-argyle-vest.png` — Brown Argyle Vest

```
Professional e-commerce product photo, flat lay shot from directly above. A brown argyle vest — sleeveless V-neck sweater vest, brown, argyle pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `cream-cable-vest.png` — Cream Cable Vest

```
Professional e-commerce product photo, flat lay shot from directly above. A cream cable vest — sleeveless V-neck sweater vest, cream, cable pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Blazers

#### `beige-blazer.png` — Beige Blazer

```
Professional e-commerce product photo, flat lay shot from directly above. A beige blazer — single-breasted tailored blazer, notch lapels, beige. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-blazer.png` — Black Blazer

```
Professional e-commerce product photo, flat lay shot from directly above. A black blazer — single-breasted tailored blazer, notch lapels, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `navy-blazer.png` — Navy Blazer

```
Professional e-commerce product photo, flat lay shot from directly above. A navy blazer — single-breasted tailored blazer, notch lapels, navy. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-tweed-blazer.png` — Brown Tweed Blazer

```
Professional e-commerce product photo, flat lay shot from directly above. A brown tweed blazer — single-breasted tailored blazer, notch lapels, brown, tweed pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `grey-oversized-blazer.png` — Grey Oversized Blazer

```
Professional e-commerce product photo, flat lay shot from directly above. A grey oversized blazer — single-breasted tailored blazer, notch lapels, grey, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Jackets

#### `denim-jacket.png` — Denim Jacket

```
Professional e-commerce product photo, flat lay shot from directly above. A denim jacket — classic trucker jacket, chest pockets, metal buttons, denim. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-leather-jacket.png` — Black Leather Jacket

```
Professional e-commerce product photo, flat lay shot from directly above. A black leather jacket — leather biker jacket, asymmetric zip, belted hem, black, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `olive-bomber-jacket.png` — Olive Bomber Jacket

```
Professional e-commerce product photo, flat lay shot from directly above. A olive bomber jacket — bomber jacket, ribbed collar, cuffs and hem, zip front, olive, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `cream-tweed-jacket.png` — Cream Tweed Jacket

```
Professional e-commerce product photo, flat lay shot from directly above. A cream tweed jacket — cropped collarless tweed jacket, contrast trim, gold buttons, cream, tweed pattern, cropped fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-track-jacket.png` — White Track Jacket

```
Professional e-commerce product photo, flat lay shot from directly above. A white track jacket — zip-up track jacket with contrast stripes along the sleeves, white. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-suede-jacket.png` — Brown Suede Jacket

```
Professional e-commerce product photo, flat lay shot from directly above. A brown suede jacket — suede jacket with fringe across the chest, brown. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-puffer-jacket.png` — Black Puffer Jacket

```
Professional e-commerce product photo, flat lay shot from directly above. A black puffer jacket — oversized quilted puffer jacket, high collar, black, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Coats

#### `navy-coat.png` — Navy Coat

```
Professional e-commerce product photo, flat lay shot from directly above. A navy coat — long double-breasted coat, navy. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `beige-trench-coat.png` — Beige Trench Coat

```
Professional e-commerce product photo, flat lay shot from directly above. A beige trench coat — double-breasted trench coat with belt and epaulettes, beige. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-wool-coat.png` — Black Wool Coat

```
Professional e-commerce product photo, flat lay shot from directly above. A black wool coat — long single-breasted wool coat, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `cream-teddy-coat.png` — Cream Teddy Coat

```
Professional e-commerce product photo, flat lay shot from directly above. A cream teddy coat — oversized fluffy teddy coat, wide collar, cream, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Dresses

#### `little-black-dress.png` — Little Black Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A little black dress — sleeveless fitted sheath dress, knee length, black, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `burgundy-dress.png` — Burgundy Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A burgundy dress — wrap midi dress, short sleeves, tie waist, burgundy. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `sage-midi-dress.png` — Sage Midi Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A sage midi dress — bias-cut slip dress, thin straps, sage, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-sundress.png` — White Sundress

```
Professional e-commerce product photo, flat lay shot from directly above. A white sundress — sundress with thin straps, fitted bodice, flared skirt, white, eyelet pattern, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-floral-mini-dress.png` — Pink Floral Mini Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A pink floral mini dress — mini dress with puff sleeves and a flared skirt, pink, floral pattern, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `cream-lace-maxi-dress.png` — Cream Lace Maxi Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A cream lace maxi dress — flowing maxi dress with flutter sleeves, cream, lace pattern, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `red-gingham-dress.png` — Red Gingham Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A red gingham dress — tea dress, short sleeves, fitted waist, flared midi skirt, red, gingham pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `red-satin-slip-dress.png` — Red Satin Slip Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A red satin slip dress — bias-cut slip dress, thin straps, red, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `navy-polka-dot-dress.png` — Navy Polka Dot Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A navy polka dot dress — tea dress, short sleeves, fitted waist, flared midi skirt, navy, polka pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-knit-midi-dress.png` — Black Knit Midi Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A black knit midi dress — long-sleeve knit midi dress, black, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-tennis-dress.png` — White Tennis Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A white tennis dress — sleeveless tennis dress, pleated skirt, polo collar, white, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-shirt-dress.png` — Brown Shirt Dress

```
Professional e-commerce product photo, flat lay shot from directly above. A brown shirt dress — collared midi shirt dress with belt, brown. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Jumpsuits

#### `black-wide-leg-jumpsuit.png` — Black Wide-Leg Jumpsuit

```
Professional e-commerce product photo, flat lay shot from directly above. A black wide-leg jumpsuit — jumpsuit with wide legs, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `olive-utility-jumpsuit.png` — Olive Utility Jumpsuit

```
Professional e-commerce product photo, flat lay shot from directly above. A olive utility jumpsuit — utility jumpsuit, short sleeves, chest pockets, belt, olive, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-linen-jumpsuit.png` — White Linen Jumpsuit

```
Professional e-commerce product photo, flat lay shot from directly above. A white linen jumpsuit — jumpsuit with wide legs, white, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Jeans

#### `straight-jeans.png` — Straight Jeans

```
Professional e-commerce product photo, flat lay shot from directly above. A straight jeans — five-pocket straight-leg jeans, denim. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `mom-jeans.png` — Mom Jeans

```
Professional e-commerce product photo, flat lay shot from directly above. A mom jeans — high-waisted tapered mom jeans with rolled hems, denim, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `dark-flared-jeans.png` — Dark Flared Jeans

```
Professional e-commerce product photo, flat lay shot from directly above. A dark flared jeans — flared jeans, denim. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `baggy-jeans.png` — Baggy Jeans

```
Professional e-commerce product photo, flat lay shot from directly above. A baggy jeans — baggy relaxed jeans, denim, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-skinny-jeans.png` — Black Skinny Jeans

```
Professional e-commerce product photo, flat lay shot from directly above. A black skinny jeans — skinny jeans, black, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-straight-jeans.png` — White Straight Jeans

```
Professional e-commerce product photo, flat lay shot from directly above. A white straight jeans — five-pocket straight-leg jeans, white. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `low-rise-flare-jeans.png` — Low-Rise Flare Jeans

```
Professional e-commerce product photo, flat lay shot from directly above. A low-rise flare jeans — low-rise flared jeans, denim, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Trousers

#### `black-tailored-trousers.png` — Black Tailored Trousers

```
Professional e-commerce product photo, flat lay shot from directly above. A black tailored trousers — tailored straight trousers with pressed creases, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `beige-wide-trousers.png` — Beige Wide Trousers

```
Professional e-commerce product photo, flat lay shot from directly above. A beige wide trousers — high-waisted wide-leg trousers, beige, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `olive-trousers.png` — Olive Trousers

```
Professional e-commerce product photo, flat lay shot from directly above. A olive trousers — relaxed trousers, olive, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `grey-wool-trousers.png` — Grey Wool Trousers

```
Professional e-commerce product photo, flat lay shot from directly above. A grey wool trousers — tailored straight trousers with pressed creases, charcoal. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `cream-linen-trousers.png` — Cream Linen Trousers

```
Professional e-commerce product photo, flat lay shot from directly above. A cream linen trousers — high-waisted wide-leg trousers, cream, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `navy-sailor-trousers.png` — Navy Sailor Trousers

```
Professional e-commerce product photo, flat lay shot from directly above. A navy sailor trousers — wide sailor trousers with a buttoned front panel, navy. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `khaki-cargo-pants.png` — Khaki Cargo Pants

```
Professional e-commerce product photo, flat lay shot from directly above. A khaki cargo pants — cargo pants with side pockets, khaki, oversized fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-check-trousers.png` — Brown Check Trousers

```
Professional e-commerce product photo, flat lay shot from directly above. A brown check trousers — tailored straight trousers with pressed creases, brown, check pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-flare-leggings.png` — Black Flare Leggings

```
Professional e-commerce product photo, flat lay shot from directly above. A black flare leggings — flared leggings, black, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `grey-joggers.png` — Grey Joggers

```
Professional e-commerce product photo, flat lay shot from directly above. A grey joggers — joggers with elastic cuffs and drawstring, grey, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Skirts

#### `beige-midi-skirt.png` — Beige Midi Skirt

```
Professional e-commerce product photo, flat lay shot from directly above. A beige midi skirt — pleated midi skirt, beige. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-midi-skirt.png` — Black Midi Skirt

```
Professional e-commerce product photo, flat lay shot from directly above. A black midi skirt — satin slip midi skirt, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-corduroy-skirt.png` — Brown Corduroy Skirt

```
Professional e-commerce product photo, flat lay shot from directly above. A brown corduroy skirt — buttoned A-line midi skirt, brown. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `denim-mini-skirt.png` — Denim Mini Skirt

```
Professional e-commerce product photo, flat lay shot from directly above. A denim mini skirt — five-pocket mini skirt, denim, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-ruffle-mini-skirt.png` — Pink Ruffle Mini Skirt

```
Professional e-commerce product photo, flat lay shot from directly above. A pink ruffle mini skirt — tiered ruffle mini skirt, pink. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `navy-pleated-mini-skirt.png` — Navy Pleated Mini Skirt

```
Professional e-commerce product photo, flat lay shot from directly above. A navy pleated mini skirt — pleated mini skirt, navy. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-plaid-midi-skirt.png` — Brown Plaid Midi Skirt

```
Professional e-commerce product photo, flat lay shot from directly above. A brown plaid midi skirt — pleated midi skirt, brown, plaid pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-tennis-skirt.png` — White Tennis Skirt

```
Professional e-commerce product photo, flat lay shot from directly above. A white tennis skirt — pleated tennis skirt, white. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `rust-tiered-maxi-skirt.png` — Rust Tiered Maxi Skirt

```
Professional e-commerce product photo, flat lay shot from directly above. A rust tiered maxi skirt — tiered maxi skirt, rust, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `champagne-satin-skirt.png` — Champagne Satin Skirt

```
Professional e-commerce product photo, flat lay shot from directly above. A champagne satin skirt — satin slip midi skirt, champagne. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Shorts

#### `denim-shorts.png` — Denim Shorts

```
Professional e-commerce product photo, flat lay shot from directly above. A denim shorts — frayed denim shorts, denim. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-linen-shorts.png` — White Linen Shorts

```
Professional e-commerce product photo, flat lay shot from directly above. A white linen shorts — drawstring linen shorts, white, relaxed fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-tailored-shorts.png` — Black Tailored Shorts

```
Professional e-commerce product photo, flat lay shot from directly above. A black tailored shorts — tailored shorts with pressed creases, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-bike-shorts.png` — Black Bike Shorts

```
Professional e-commerce product photo, flat lay shot from directly above. A black bike shorts — fitted bike shorts, black, fitted fit. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `khaki-bermuda-shorts.png` — Khaki Bermuda Shorts

```
Professional e-commerce product photo, flat lay shot from directly above. A khaki bermuda shorts — knee-length Bermuda shorts, khaki. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Shoes

#### `white-sneakers.png` — White Sneakers

```
Professional e-commerce product photo, flat lay shot from directly above. A white sneakers — pair of low-top leather sneakers, white. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-loafers.png` — Black Loafers

```
Professional e-commerce product photo, flat lay shot from directly above. A black loafers — pair of leather penny loafers, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-loafers.png` — Brown Loafers

```
Professional e-commerce product photo, flat lay shot from directly above. A brown loafers — pair of leather penny loafers, brown. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-ankle-boots.png` — Brown Ankle Boots

```
Professional e-commerce product photo, flat lay shot from directly above. A brown ankle boots — pair of leather ankle boots with block heel, brown. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-ankle-boots.png` — Black Ankle Boots

```
Professional e-commerce product photo, flat lay shot from directly above. A black ankle boots — pair of leather ankle boots with block heel, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-heels.png` — Black Heels

```
Professional e-commerce product photo, flat lay shot from directly above. A black heels — pair of pointed-toe pumps, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `beige-ballet-flats.png` — Beige Ballet Flats

```
Professional e-commerce product photo, flat lay shot from directly above. A beige ballet flats — pair of ballet flats, beige. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-ballet-flats.png` — Pink Ballet Flats

```
Professional e-commerce product photo, flat lay shot from directly above. A pink ballet flats — pair of ballet flats, pink. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-mary-janes.png` — Black Mary Janes

```
Professional e-commerce product photo, flat lay shot from directly above. A black mary janes — pair of Mary Jane flats with buckle strap, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `cream-slingbacks.png` — Cream Slingbacks

```
Professional e-commerce product photo, flat lay shot from directly above. A cream slingbacks — pair of slingback kitten heels, cream. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `gold-strappy-sandals.png` — Gold Strappy Sandals

```
Professional e-commerce product photo, flat lay shot from directly above. A gold strappy sandals — pair of strappy heeled sandals, gold. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `tan-flat-sandals.png` — Tan Flat Sandals

```
Professional e-commerce product photo, flat lay shot from directly above. A tan flat sandals — pair of flat leather sandals, tan. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-knee-boots.png` — Brown Knee Boots

```
Professional e-commerce product photo, flat lay shot from directly above. A brown knee boots — pair of knee-high leather boots, brown. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-combat-boots.png` — Black Combat Boots

```
Professional e-commerce product photo, flat lay shot from directly above. A black combat boots — pair of lace-up combat boots with chunky sole, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `retro-running-sneakers.png` — Retro Running Sneakers

```
Professional e-commerce product photo, flat lay shot from directly above. A retro running sneakers — pair of retro running sneakers, grey. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `white-platform-sneakers.png` — White Platform Sneakers

```
Professional e-commerce product photo, flat lay shot from directly above. A white platform sneakers — pair of platform sneakers, white. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Bags

#### `black-shoulder-bag.png` — Black Shoulder Bag

```
Professional e-commerce product photo, flat lay shot from directly above. A black shoulder bag — structured shoulder bag with flap, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `tan-shoulder-bag.png` — Tan Shoulder Bag

```
Professional e-commerce product photo, flat lay shot from directly above. A tan shoulder bag — structured shoulder bag with flap, tan. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `camel-tote.png` — Camel Tote

```
Professional e-commerce product photo, flat lay shot from directly above. A camel tote — leather tote bag, camel. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-tote.png` — Black Tote

```
Professional e-commerce product photo, flat lay shot from directly above. A black tote — leather tote bag, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-baguette-bag.png` — Pink Baguette Bag

```
Professional e-commerce product photo, flat lay shot from directly above. A pink baguette bag — small baguette bag, pink. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `straw-basket-bag.png` — Straw Basket Bag

```
Professional e-commerce product photo, flat lay shot from directly above. A straw basket bag — woven straw basket bag with leather handles, tan, woven pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-crossbody-bag.png` — Black Crossbody Bag

```
Professional e-commerce product photo, flat lay shot from directly above. A black crossbody bag — small crossbody bag with long strap, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-satchel.png` — Brown Satchel

```
Professional e-commerce product photo, flat lay shot from directly above. A brown satchel — leather satchel with buckled flap, brown. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-quilted-bag.png` — Black Quilted Bag

```
Professional e-commerce product photo, flat lay shot from directly above. A black quilted bag — quilted leather bag with chain strap, black, quilted pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `gold-clutch.png` — Gold Clutch

```
Professional e-commerce product photo, flat lay shot from directly above. A gold clutch — envelope clutch, gold. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

### Accessories

#### `black-sunglasses.png` — Black Sunglasses

```
Professional e-commerce product photo, flat lay shot from directly above. A black sunglasses — pair of glasses, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-tinted-sunglasses.png` — Pink Tinted Sunglasses

```
Professional e-commerce product photo, flat lay shot from directly above. A pink tinted sunglasses — pair of glasses, pink. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `cat-eye-sunglasses.png` — Cat-Eye Sunglasses

```
Professional e-commerce product photo, flat lay shot from directly above. A cat-eye sunglasses — pair of glasses, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `tortoiseshell-glasses.png` — Tortoiseshell Glasses

```
Professional e-commerce product photo, flat lay shot from directly above. A tortoiseshell glasses — pair of glasses, brown, tortoiseshell pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `gold-hoops.png` — Gold Hoops

```
Professional e-commerce product photo, flat lay shot from directly above. A gold hoops — pair of earrings, gold. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pearl-earrings.png` — Pearl Earrings

```
Professional e-commerce product photo, flat lay shot from directly above. A pearl earrings — pair of earrings, ivory. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pearl-necklace.png` — Pearl Necklace

```
Professional e-commerce product photo, flat lay shot from directly above. A pearl necklace — necklace, ivory. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `gold-chain-necklace.png` — Gold Chain Necklace

```
Professional e-commerce product photo, flat lay shot from directly above. A gold chain necklace — necklace, gold. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `gold-watch.png` — Gold Watch

```
Professional e-commerce product photo, flat lay shot from directly above. A gold watch — wristwatch, gold. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `burgundy-scarf.png` — Burgundy Scarf

```
Professional e-commerce product photo, flat lay shot from directly above. A burgundy scarf — long knitted wool scarf, burgundy. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `red-silk-neck-scarf.png` — Red Silk Neck Scarf

```
Professional e-commerce product photo, flat lay shot from directly above. A red silk neck scarf — small silk neck scarf, knotted, red. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `silk-headscarf.png` — Silk Headscarf

```
Professional e-commerce product photo, flat lay shot from directly above. A silk headscarf — square printed silk scarf, folded, cream, print pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `pink-hair-bow.png` — Pink Hair Bow

```
Professional e-commerce product photo, flat lay shot from directly above. A pink hair bow — satin hair bow, pink. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-hair-bow.png` — Black Hair Bow

```
Professional e-commerce product photo, flat lay shot from directly above. A black hair bow — satin hair bow, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-baseball-cap.png` — Black Baseball Cap

```
Professional e-commerce product photo, flat lay shot from directly above. A black baseball cap — cotton baseball cap, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `straw-sun-hat.png` — Straw Sun Hat

```
Professional e-commerce product photo, flat lay shot from directly above. A straw sun hat — wide-brim straw sun hat, tan, woven pattern. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `brown-belt.png` — Brown Belt

```
Professional e-commerce product photo, flat lay shot from directly above. A brown belt — leather belt with buckle, brown. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```

#### `black-belt.png` — Black Belt

```
Professional e-commerce product photo, flat lay shot from directly above. A black belt — leather belt with buckle, black. Laid flat and neatly arranged, front side up, the whole item visible and centred with an empty margin around it. Plain, uniform light grey seamless studio background (#E4E4E4), soft even studio lighting with a very soft natural shadow. True-to-life colours and realistic fabric texture, fine stitching, natural folds. No people, no model, no hands, no mannequin, no hanger, no props, no text, no logos, no labels, no watermark. Photorealistic e-commerce product photography, high detail. Square 1:1 format.
```
