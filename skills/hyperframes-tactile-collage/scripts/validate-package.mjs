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
const required = [
  "SKILL.md",
  "agents/openai.yaml",
  "references/style-system.md",
  "references/scene-grammar.md",
  "references/layering-safe-zones.md",
  "references/motion-captions-audio.md",
  "assets/frame.md",
  "assets/components/tactile-caption.html",
  "assets/components/tactile-safe-zones.html",
  "assets/fonts/permanent-marker-400.woff2.b64",
  "assets/fonts/playfair-display-var.woff2.b64",
  "assets/fonts/montserrat-var.woff2.b64",
  "assets/fonts/courier-prime-700.woff2.b64",
  "assets/fonts/LICENSE-Permanent-Marker.txt",
  "assets/fonts/OFL-Courier-Prime.txt",
  "scripts/install-fonts.mjs",
  "scripts/validate-package.mjs"
];

const failures = [];
for (const relative of required) {
  if (!fs.existsSync(path.join(root, relative))) failures.push(`missing ${relative}`);
}

const textExtensions = new Set([".md", ".yaml", ".yml", ".html", ".mjs", ".txt", ".b64"]);
const forbidden = [
  /\/Users\//i,
  /\/home\/[A-Za-z0-9._-]+\//i,
  /~\/(Desktop|Documents|Downloads)\//i,
  /file:\/\//i,
  /[A-Z]:\\Users\\/i
];
for (let index = 0; index < args.length; index += 1) {
  if (args[index] === "--forbid" && args[index + 1]) {
    const escaped = args[index + 1].replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    forbidden.push(new RegExp(escaped, "i"));
  }
}

function walk(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const full = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(full) : [full];
  });
}

if (fs.existsSync(root)) {
  for (const file of walk(root)) {
    if (!textExtensions.has(path.extname(file))) continue;
    const relative = path.relative(root, file);
    const content = fs.readFileSync(file, "utf8");
    for (const pattern of forbidden) {
      if (pattern.test(content)) failures.push(`${relative} contains forbidden source-specific content matching ${pattern}`);
    }
  }
}

const skillPath = path.join(root, "SKILL.md");
if (fs.existsSync(skillPath)) {
  const skill = fs.readFileSync(skillPath, "utf8");
  if (skill.split(/\r?\n/).length > 500) failures.push("SKILL.md exceeds 500 lines");
  const frontmatter = skill.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!frontmatter) failures.push("SKILL.md frontmatter is missing");
  else {
    const keys = frontmatter[1].split(/\r?\n/).filter(Boolean).map((line) => line.split(":", 1)[0]);
    if (keys.join(",") !== "name,description") failures.push("SKILL.md frontmatter must contain only name and description");
  }
}

for (const font of ["permanent-marker-400.woff2.b64", "playfair-display-var.woff2.b64", "montserrat-var.woff2.b64", "courier-prime-700.woff2.b64"]) {
  const fontPath = path.join(root, "assets", "fonts", font);
  if (!fs.existsSync(fontPath)) continue;
  const bytes = Buffer.from(fs.readFileSync(fontPath, "utf8").replace(/\s+/g, ""), "base64");
  if (bytes.subarray(0, 4).toString("ascii") !== "wOF2") failures.push(`${font} is not valid encoded WOFF2 data`);
}

if (failures.length) {
  console.error("Tactile Paper Collage package validation failed:");
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exit(1);
}

console.log("Tactile Paper Collage package validation passed.");
console.log(`Validated ${required.length} required files with portability and source-isolation checks.`);
