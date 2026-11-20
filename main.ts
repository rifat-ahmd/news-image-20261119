// Entry for make.fun news-image-20261119: world news of Thursday 19 November 2026 in one image.
// The image is pre-rendered (page.html -> render.py -> entry.png); this program only copies it,
// so both runs write identical bytes. Node 22, standard library only, no network.
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const MAX_BYTES = 1024 * 1024;
const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

const image = readFileSync(new URL('./entry.png', import.meta.url));
if (!image.subarray(0, 8).equals(PNG_SIGNATURE)) throw new Error('entry.png is not a PNG');
if (image.length > MAX_BYTES) throw new Error(`entry.png is ${image.length} bytes, over 1 MiB`);
// IHDR width and height (big-endian) sit at bytes 16-23.
const width = image.readUInt32BE(16);
const height = image.readUInt32BE(20);
if (width > 1024 || height > 1024) throw new Error(`entry.png is ${width}x${height}, over 1024x1024`);

const outDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, 'entry.png'), image);
