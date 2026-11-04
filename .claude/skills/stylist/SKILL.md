---
name: stylist
description: The owner's styling rules for The Interactive Digital Wardrobe. Use whenever you create, change or review an outfit (curated looks in index.html, the outfit generator, new catalog pieces bought to complete looks) or judge whether clothes go together.
---

# Stylist rules

These rules come from the owner's own reference outfits (tonal chocolate brown, burgundy with navy pinstripe,
red with cream polka dots, forest green with beige, butter yellow with black, blue tweed with white).
They are enforced in code — `styleWhy()` in the outfit engine and the stylist block in `#idw-validate`
(`node tools/check-data.mjs` fails on a curated look that breaks them) — but taste goes beyond code:
always look at the finished flat-lay before calling a look done.

## Colour
1. **Two, at most three colour families per outfit** (clothes, shoes and bag). Families:
   black (black, charcoal) · light (white, ivory, cream, champagne, beige) · camel (camel, tan, khaki) ·
   brown · blue (navy, denim, light blue) · grey · each accent colour on its own. Gold is a metal and never counts.
2. **Two formulas**: tonal (everything in one family, e.g. all chocolate brown, all burgundy) or
   **neutral base + one accent** (burgundy, red, forest green, butter yellow, pink, lilac, sage, olive, rust, mustard).
3. **Repeat the accent** at least twice (top + bag, bag + shoes + earrings, knit + bag + hair bow).
   A single accent is allowed only on the main piece (top, bottom, dress, jacket) with everything else neutral —
   never a lone red scarf or lone pink bag.
4. Denim and navy count as neutrals: dark denim with brown or burgundy, navy pinstripe with burgundy.

## Shoes, bag, metals
5. **Shoes and bag match**: same family, or both in the repeated accent. Exceptions: a gold clutch or gold sandals;
   sneakers (sporty/street looks) with a neutral bag.
6. **One leather tone**: chocolate brown and camel/tan leathers are never mixed in shoes, bag and belt.
7. **Gold jewellery only**, usually 2–3 pieces (hoops or drops, watch, fine chain, bangle, pearls).

## Shape
8. Fitted or waist-defined top (corset, wrap shirt, fitted knit, waistcoat, belt) over a wide or long bottom
   (wide-leg trousers or jeans, maxi or midi skirt); or a dress with a fitted bodice. Avoid oversized over oversized
   except in Streetwear.
9. **One pattern per outfit** (polka dot, pinstripe, stripe, tweed, gingham, plaid); the other pieces are plain,
   in the pattern's colours.

## By style
- Polished styles (Old Money, Feminine Chic, Elegant, Coquette, Romantic, Dark Academia, Preppy, Vintage, Minimalist):
  pointed slingbacks, pumps, mules, loafers, ballet flats, knee boots. No sneakers or combat boots.
- Casual, Streetwear, Sporty Chic, Y2K and Boho may use sneakers, platforms, sandals and boots — colour rules still apply.
- Details that fit the owner's taste: oval or cat-eye sunglasses, velvet bows and headbands, pearls.

## Workflow for a new or changed look
1. Pick the formula (tonal or neutral + accent) and the hero piece.
2. Fill the slots with pieces that keep the palette; match shoes and bag; add 2–3 gold accessories.
3. `node tools/check-data.mjs` must pass.
4. Render the flat-lay and look at it next to the others of the same style; redo anything that looks busy or flat.
5. If a look needs a piece the catalog lacks, add the piece (data + photo via the photo workflow in README) rather than
   bending the rules. Use references only as inspiration — no logos or brand designs.
