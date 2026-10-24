#!/usr/bin/env node
// Inventory consistency check for The Interactive Digital Wardrobe.
// Reads the catalog (#idw-data) and the validator (#idw-validate) straight from index.html,
// so the page and this script always apply the same rules.
//
//   node tools/check-data.mjs                 check index.html
//   node tools/check-data.mjs --data file.json  check another catalog with the same validator
//
// Exit code 1 when there are errors.
import fs from 'fs';
import path from 'path';
import vm from 'vm';
import { fileURLToPath } from 'url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const htmlPath = path.join(root, 'index.html');
const html = fs.readFileSync(htmlPath, 'utf8');

const block = id => {
  const m = html.match(new RegExp(`<script[^>]*id="${id}"[^>]*>([\\s\\S]*?)</script>`));
  if (!m) throw new Error(`index.html has no <script id="${id}"> block`);
  return m[1];
};

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(block('idw-validate'), ctx);

const dataArg = args.indexOf('--data');
const data = JSON.parse(dataArg >= 0 ? fs.readFileSync(args[dataArg + 1], 'utf8') : block('idw-data'));

// PHOTOS map from the main script, plus each item's own "image" field
const photos = {};
const pm = html.match(/const PHOTOS = (\{[\s\S]*?\});/);
if (pm) Object.assign(photos, vm.runInNewContext(`(${pm[1]})`));
for (const it of data.items || []) if (it.image && !(it.id in photos)) photos[it.id] = it.image;

const drawable = (html.match(/const KIND_ART = \{([^}]*)\}/) || ['', ''])[1].match(/(\w+):/g)?.map(k => k.slice(0, -1));
const result = ctx.window.validateInventory(data, { photos, drawable });

const missingFiles = Object.entries(photos).filter(([, src]) => !/^data:/.test(src) && !fs.existsSync(path.join(root, src)));
for (const [id, src] of missingFiles) result.warnings.push(`photo file not found for "${id}": ${src} (the drawing will be shown)`);

const s = result.stats;
console.log(`Catalog: ${s.items} items, ${s.outfits} curated outfits, ${s.categories} categories, ${s.colors} colours, ${s.aesthetics} aesthetics, ${Object.keys(photos).length} photos`);
for (const e of result.errors) console.log(`  ERROR    ${e}`);
for (const w of result.warnings) console.log(`  warning  ${w}`);
console.log(result.errors.length ? `✗ ${result.errors.length} error(s), ${result.warnings.length} warning(s)` : `✓ 0 errors, ${result.warnings.length} warning(s)`);
process.exit(result.errors.length ? 1 : 0);
