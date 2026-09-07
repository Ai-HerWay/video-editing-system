#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const compositionArg = process.argv.slice(2).find((arg) => !arg.startsWith("--"));
if (!compositionArg) {
  console.error("Usage: node install-fonts.mjs <composition-dir> [--assets-dir <path>]");
  process.exit(2);
}

const args = process.argv.slice(2);
const assetsIndex = args.indexOf("--assets-dir");
const compositionDir = path.resolve(compositionArg);
const configPath = path.join(compositionDir, "hyperframes.json");
const config = fs.existsSync(configPath) ? JSON.parse(fs.readFileSync(configPath, "utf8")) : {};
const configuredAssets = config.paths?.assets || "assets";
const assetsDir = assetsIndex >= 0
  ? path.resolve(args[assetsIndex + 1])
  : path.resolve(compositionDir, configuredAssets);
const fontDir = path.join(assetsDir, "fonts");
const skillDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const encodedDir = path.join(skillDir, "assets", "fonts");
const fonts = [
  ["permanent-marker-400.woff2.b64", "permanent-marker-400.woff2"],
  ["playfair-display-var.woff2.b64", "playfair-display-var.woff2"],
  ["montserrat-var.woff2.b64", "montserrat-var.woff2"]
];

if (!fs.existsSync(compositionDir) || !fs.statSync(compositionDir).isDirectory()) {
  console.error(`Composition directory not found: ${compositionDir}`);
  process.exit(2);
}

fs.mkdirSync(fontDir, { recursive: true });
for (const [encodedName, outputName] of fonts) {
  const encodedPath = path.join(encodedDir, encodedName);
  if (!fs.existsSync(encodedPath)) {
    console.error(`Bundled font is missing: ${encodedPath}`);
    process.exit(2);
  }
  const bytes = Buffer.from(fs.readFileSync(encodedPath, "utf8").replace(/\s+/g, ""), "base64");
  if (bytes.subarray(0, 4).toString("ascii") !== "wOF2") {
    console.error(`Bundled font is invalid: ${encodedName}`);
    process.exit(2);
  }
  fs.writeFileSync(path.join(fontDir, outputName), bytes);
}

console.log(`Installed ${fonts.length} Tactile Paper Collage fonts in ${fontDir}`);
