#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const args = process.argv.slice(2);
const projectArg = args.find((arg) => !arg.startsWith("--"));
const publicIndex = args.indexOf("--public-dir");

if (!projectArg) {
  console.error("Usage: node preflight.mjs <composition-dir> [--public-dir <path>]");
  process.exit(2);
}

const projectDir = path.resolve(projectArg);
const publicDir = publicIndex >= 0
  ? path.resolve(args[publicIndex + 1])
  : path.join(projectDir, "public");
const fontDir = path.join(publicDir, "fonts");
const required = [
  "Georgia-Regular.woff2",
  "Georgia-Italic.woff2",
  "Inter-400-latin.woff2",
  "Inter-700-latin.woff2",
];

function isWoff2(filePath) {
  if (!fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) return false;
  const handle = fs.openSync(filePath, "r");
  const signature = Buffer.alloc(4);
  fs.readSync(handle, signature, 0, 4, 0);
  fs.closeSync(handle);
  return signature.toString("ascii") === "wOF2";
}

if (!fs.existsSync(projectDir) || !fs.statSync(projectDir).isDirectory()) {
  console.error(`Quiet Editorial UI preflight failed: composition directory not found: ${projectDir}`);
  process.exit(2);
}

const invalid = required.filter((name) => !isWoff2(path.join(fontDir, name)));
const specs = ["frame.md", "design.md", "DESIGN.md"].filter((name) =>
  fs.existsSync(path.join(projectDir, name)),
);

if (invalid.length) {
  console.error("Quiet Editorial UI preflight failed.");
  console.error(`Required WOFF2 files missing or invalid in ${fontDir}:`);
  invalid.forEach((name) => console.error(`- ${name}`));
  console.error("Supply licensed Georgia files and copy the bundled Inter files before rendering.");
  process.exit(2);
}

console.log("Quiet Editorial UI font preflight passed.");
console.log(`Composition: ${projectDir}`);
console.log(`Design specs found: ${specs.length ? specs.join(", ") : "none"}`);
