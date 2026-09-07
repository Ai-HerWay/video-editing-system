#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const args = process.argv.slice(2);
const rootArg = args.find((arg) => !arg.startsWith("--"));

if (!rootArg) {
  console.error("Usage: node validate-package.mjs <skill-dir> [--forbid <term>]...");
  process.exit(2);
}

const root = path.resolve(rootArg);
const forbidden = [];
for (let i = 0; i < args.length; i += 1) {
  if (args[i] === "--forbid" && args[i + 1]) forbidden.push(args[i + 1].toLowerCase());
}

const required = [
  "SKILL.md",
  "agents/openai.yaml",
  "assets/frame.md",
  "assets/components/quiet-editorial-caption.html",
  "assets/components/quiet-editorial-safe-zones.html",
  "assets/examples/golden-frames.html",
  "assets/fonts/Inter-400-latin.woff2",
  "assets/fonts/Inter-700-latin.woff2",
  "assets/fonts/OFL-Inter.txt",
  "references/font-setup.md",
  "scripts/preflight.mjs",
];
const missing = required.filter((relative) => !fs.existsSync(path.join(root, relative)));

function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const absolute = path.join(dir, entry.name);
    return entry.isDirectory() ? walk(absolute) : [absolute];
  });
}

const textExtensions = new Set([".md", ".html", ".mjs", ".yaml", ".yml", ".json", ".txt"]);
const violations = [];
for (const file of walk(root)) {
  const relative = path.relative(root, file).toLowerCase();
  const content = textExtensions.has(path.extname(file))
    ? fs.readFileSync(file, "utf8").toLowerCase()
    : "";
  for (const term of forbidden) {
    if (relative.includes(term) || content.includes(term)) violations.push(`${term}: ${relative}`);
  }
}

if (missing.length || violations.length) {
  if (missing.length) {
    console.error("Missing required package files:");
    missing.forEach((file) => console.error(`- ${file}`));
  }
  if (violations.length) {
    console.error("Forbidden identifiers found:");
    [...new Set(violations)].forEach((item) => console.error(`- ${item}`));
  }
  process.exit(1);
}

console.log(`Quiet Editorial UI package valid: ${root}`);
