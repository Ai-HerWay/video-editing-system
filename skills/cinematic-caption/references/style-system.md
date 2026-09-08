# Style System

This reference turns spoken words into a repeatable AI Her Way caption design system. The craft draws on editorial social-video conventions; the specific choices below are ours.

## AI Her Way brand pins

The general method leaves several choices deliberately open — which display face, which single accent hue, which colour for a rule line. AI Her Way fills those blanks with its locked Social/Reels system. Apply the brand value wherever the general text names a role or an option; the method itself does not change.

- **Type, without exception.** `hero` = Playfair Display Black / 900. `editorial accent` = Playfair Display Italic. `support` = Montserrat, regular or medium.
- **One accent word per group.** Exactly one italic word in a group may carry a colour accent — Walnut `#7B5A49` over light footage, Dusty Blue `#C4D6DA` over dark footage. This single italic-accent word is the brand's most recognisable caption signature. Never give more than one word per group the accent, and never reach for an arbitrary hue.
- **Gold hairline.** The `rule-draw` device renders in Gold `#B08A62`, matching the ~2px gold rule the brand draws under headlines.

Full palette, for the rare moment a concrete hex is genuinely needed: Espresso `#35241F`, Ink `#2B1E19`, Linen Cream `#F2EBDD`, Ivory `#FAF6EF`, Dusty Blue `#C4D6DA`, Stone `#C0CACE`, Sage `#AAB6A0`, Deep Olive `#46513D`, Walnut `#7B5A49`, Gold `#B08A62`.

## Step 1 — Cut speech into cues

Aim for 2–5 displayed words and roughly 0.65–1.8 seconds per cue. Break on meaning, contrast, breath, and rhetorical turns — not on a fixed word count. Drop filler and trailing punctuation unless the punctuation *is* the idea. Hold important phrases a little longer, and accept that not every spoken word needs to appear. Keep a cue to one line where you can; use two lines only for a deliberate hero lockup. Keep support copy in natural mixed case, saving all caps for acronyms, tight proof labels, or one forceful CTA keyword.

Give every displayed fragment a role:

| Role | What it is |
| --- | --- |
| `setup` | context that prepares a claim |
| `anchor` | the key noun or idea |
| `contrast` | a reversal, e.g. cheaper / not expensive |
| `proof` | a number, place, feature, or concrete example |
| `aside` | a short conversational bridge |
| `payoff` | the conclusion of the sentence |
| `cta` | the requested next action |

Group before you style. A semantic group is one clause, contrast, proof statement, payoff, or CTA. Every fragment gets a `semanticGroupId` and an `orderIndex` that follows speech order. Omit filler when it helps, but never reorder the surviving words just to fill space.

Pick one stack grammar per group:

- **support → hero** — context first, decisive word second;
- **eyebrow → hero → qualifier** — compact setup, dominant idea, then a clarifier;
- **proof label → value** — a small label ahead of a large number or place;
- **cta setup → action → keyword → tail** — the whole instruction in the order it is spoken;
- **parallel hero run** — consecutive list items that swap in and out of one anchor zone.

Treat phrases as units when they wrap. Do not split an adjective from its noun, a preposition from its object, or an action from the keyword it needs.

## Step 2 — Assign emphasis on purpose

Three levels, sized for a 1080×1920 composition:

- **support** — 52–80 px, regular or medium, mostly clean white;
- **anchor** — 76–112 px, semibold or bold, one accent colour or one weight shift;
- **hero** — 150–240 px, extra-bold or condensed display, held back for a reversal, a decisive payoff, an important number or place, or a CTA keyword. A very short number or place can reach 280 px when the frame allows.

Roughly 60–75% of cues should be support, 20–35% anchor, and no more than 5–15% hero. Do not promote a word just because it is a noun.

Score every hero candidate before you style it:

- `+3` — removing the word would weaken or change the claim;
- `+2` — it is concrete proof: a number, place, named feature, or result;
- `+2` — it carries the spoken stress, the reversal, the punchline, the payoff, or the CTA keyword;
- `+1` — it is short enough to stay powerful and readable at hero scale;
- `−3` — it is filler, connective tissue, or a generic noun with no argumentative weight;
- `−2` — a neighbouring cue already carries the same emphasis;
- `−2` — safe placement would hide identifying letters or important scene content.

Promote to `hero` at a score of 4 or higher, and normally only the single highest scorer in an argument beat. Use `anchor` when the idea matters but does not clear the bar. A genuine rhetorical parallel list may promote several consecutive items together as one `heroSequence` — record the shared reason rather than pretending each is its own payoff. A passage with no hero at all is a valid outcome.

Favour weight and scale contrast over decoration. Across a typical 8–12 second passage, run white support, one neutral glass family, and at most one accent hue unless brand or meaning clearly demands more.

The three-part type hierarchy:

- **support** — a clean, locally bundled sans in its true regular or medium weight (brand pin: Montserrat);
- **hero** — a display face whose file genuinely contains the extra-bold, black, or condensed weight you set (brand pin: Playfair Display Black / 900);
- **editorial accent** — an occasional serif or italic for a conversational action, aside, or CTA, never every cue (brand pin: Playfair Display Italic).

Do not alias a 700 file as 800 or 900, lean on browser-synthesised bold, or fake weight with a fat outline. Steer clear of heavy negative tracking, and inspect hero words at full resolution for merged strokes, false crossbars, and ambiguous letters.

Default support to white. On a bright frame, hold the white with a restrained dark stroke, drop shadow, or feathered local scrim before you flip the text itself to black. Use black support only when it is genuinely the more readable editorial choice for that exact frame.

## Step 3 — Place captions around the subject

For portrait 1080×1920, treat x=90–990 and y=240–1520 as the baseline safe zone unless the project sets tighter margins.

At the start, midpoint, and end of each designed cue:

1. find the face, mouth, hair, shoulders, hands, products, UI, and existing text;
2. fold those samples into one motion envelope, so a placement that is safe at the start stays safe throughout;
3. locate the largest calm negative-space region, or a clean outer hair/shoulder edge for real depth;
4. hold foreground support at least 40 px off the face and mouth for the whole cue;
5. stack the phrase into one to three intentional lines, with the anchor making the visual edge;
6. keep the group's anchor zone and reading path until the sentence, shot, or argument changes.

Record a `flowDirection` for each group — `upper-left-to-lower-right`, `top-to-bottom`, `left-to-right`, and so on. Later fragments may travel farther along that vector or hold aligned, but must never reverse it. Spatial variety comes from a new group choosing a justified path, not from zigzagging inside one sentence.

Valid placements: upper-left, upper-right, shoulder-left, shoulder-right, center-gap, lower-left, lower-right. Avoid the bottom platform-UI band, and avoid thin white type over bright windows or sky without a restrained shadow, scrim, or alternate colour.

Across an 8–12 second passage, use roughly three to five layout states where the footage and argument give you safe transitions. Between unrelated groups, change one or two properties — anchor zone, alignment, scale relationship, depth, fill, or motion — not all of them at once. A parallel hero run counts as one layout state even as several words swap through it.

Keep related lines tight enough to read as a unit:

- support-to-support — line-height 0.96–1.10, no arbitrary spacer;
- support-to-hero or hero-to-qualifier — about 0.15–0.45× the support font size;
- CTA action-to-keyword — visually adjacent, usually within one support line-height;
- unrelated groups — separate clearly, or replace the earlier group, rather than leaving ambiguous floating fragments.

Inside a top-to-bottom group, each later fragment's top edge sits level with or below the previous one. Inside a left-to-right group, each later fragment sits level with or to the right. No up-down-up or left-right-left order within a sentence.

For built-up speech, let semantic fragments accumulate into the final lockup at their word starts. A phrase can open as compact support, hand off to a background hero, and finish on a foreground payoff — but never show the finished lockup before its words are spoken.

Where automatic face or object detection is not available, place conservatively and confirm the start, midpoint, and end snapshots by eye.

## Step 4 — Choose the treatment

**Clean editorial** — the default for most cues: precise sans, modest tracking, no box, and a soft text shadow only where contrast needs it.

**Weight or scale shift** — mix thin or regular support with one bold anchor. Keep the phrase coherent; the anchor reads first without erasing the support words.

**Hero-scale word** — for a reversal, payoff, proof point, or CTA. Let the word briefly overshoot and settle. It may sit behind or beside the subject only while masking and contrast stay legible.

**Proof-scale number or place** — treat an important number, city, region, address fragment, percentage, or named place as evidence. Set it much larger than an ordinary anchor — often 170–280 px in portrait — and let it span a good share of the frame width, paired with a much smaller white label. Put it behind the subject only with a real depth treatment; otherwise use the largest face-safe negative space.

**Tinted-glass hero fill** — the default translucent treatment. Set glyph fill to roughly 32–55% opacity so the real room, landscape, or footage shows through the letters. Add a crisp 0.75–1.25 px rim, a restrained inner highlight, and an optional soft light sweep. Hold the letterform steady while the internal highlight travels for about 0.4–0.8 seconds. Neutral silver-white is the base look; bring in one hue per word only when brand, footage, or meaning earns it — and for AI Her Way that hue is always the single italic-accent word in Walnut `#7B5A49` on light footage or Dusty Blue `#C4D6DA` on dark footage, never more than one word per group. Repeating scan lines, striped bands, and obvious raster textures are opt-in, not part of the default glass. Reserve multicolour, flag, map, image, or video texture for speech that names that place or evidence source. For genuine video-through-type, clip a duplicated local video to the exact glyphs and drive it from composition time. If a dimensional look is explicitly requested, reuse the same local font geometry across every layer and keep bevel or extrusion shallow; glass alone needs no extrusion.

**Behind-subject depth** — real behind-person type is three layers: base footage, then the oversized hero or proof type, then a foreground subject matte or cutout above it. Keep ordinary support copy above the subject layer. With no clean matte, use a hand-verified occlusion mask only on a stable shot; otherwise do not fake the depth — set the word beside or above the person with face clearance. Hair, hands, and gestures are part of the silhouette. The foreground layer must share the base footage's exact timing and geometry: confirm start time, frame rate, duration, dimensions, crop, and object-fit before you judge the matte, and inspect at least three frames with real movement in hair, hands, or shoulders. A soft doubled contour usually means the foreground RGB was compressed separately even though timing matches — rebuild the cutout from the original source pixels plus the existing matte alpha so foreground and background colours stay identical, encode it locally with a real alpha channel, and never add a cosmetic shadow to the subject layer. Record an `occlusionBudget` per background hero: aim for 10–30% of the glyph area crossing hair, shoulders, arms, or torso, with 35% the ceiling for a short familiar word. Face and mouth coverage never counts as acceptable overlap. When a clean matte exists, prefer a 10–22% hairline or outer-head overlap for the most important heroes — a word floating over an unused gap almost always reads weaker than one whose lower strokes tuck behind the subject — while preserving the upper glyph structure so the whole word stays readable. Treat identifying internal glyphs as protected: for words with repeated or narrow letters, keep enough of the centre for instant spelling and prefer overlap on the first or last outer stroke. Confirm the displayed spelling in a midpoint snapshot rather than trusting the DOM text.

**Soft bloom** — for luminous, aspirational, technology, energy, reveal, or premium-payoff language, or when glow is explicitly requested. Bloom for 0.20–0.40 seconds at entry, then settle to a readable edge with layered text-shadow or a low-opacity blurred duplicate. Never leave a thick neon halo on routine dialogue.

**Evidence graphics** — maps, listing cards, photos, icons, numbers, or mini-panels may support a `proof` cue as evidence attached to the sentence, not decoration. Prefer one cluster with clear hierarchy. Rounded cards can carry a faint rim light or bloom but stay subordinate to the message. Keep standalone evidence native — a screenshot can use its own edge and a restrained shadow; folders and files read as objects. Add a panel only when it represents a real browser, chat, dialog, or interface surface. For sequential instructions, give related assets a `persistenceGroup` and keep completed steps on screen while the next dependent action appears and the frame has room.

**Subject transition** — a cutout, silhouette, or foreground wipe can bridge a major section change. Use it sparingly, and only when clean source separation exists. Never fabricate an inaccurate mask.

## Step 5 — Motion vocabulary

Keep entries fast and decisive, generally 0.18–0.45 seconds.

- `support-cascade` — 10–22 px rise with opacity and a 30–55 ms word stagger;
- `firm-settle` — 0.88 → 1.04 → 1 scale for an anchor or hero landing;
- `editorial-wipe` — an overflow-hidden reveal for a clean phrase or place;
- `directional-snap` — 18–36 px move in from the nearest frame edge;
- `rule-draw` — a short underline or divider drawn after the anchor arrives (brand pin: render in Gold `#B08A62`, the gold-hairline signature);
- `bloom-settle` — glow and blur peak at entry, then ease off while the glyph stays crisp;
- `fill-drift` — the glyph lands first, then the translucent internal colour or footage moves while letter geometry holds;
- `depth-reveal` — a large word enters on the middle layer and is partly occluded by a real foreground subject matte;
- `card-orbit` — evidence cards arrive from nearby vectors and settle into one organised cluster;
- `foreground-wipe` — a subject or architectural edge motivates the transition.

Use transform and opacity for the primary motion. Keep animation deterministic and seek-safe, and do not pile bounce, blur, rotation, and glow onto one routine cue.

## Step 6 — Sound design

Sound is optional. When you use it, land it on the visual moment, not the animation start:

- support caption — usually silent; an occasional soft tick is plenty;
- directional move or wipe — a short airy whoosh;
- anchor landing — a muted pop or light impact;
- hero word or payoff — a low, controlled thump with a short transient;
- bloom or luminous reveal — a subtle shimmer sitting quietly above the landing;
- evidence-card cluster — one entry whoosh plus small staggered ticks, not one hit per card;
- major section transition — a brief reverse riser into a single landing impact.

Default to no more than one audible accent per emphasis beat, and leave quiet gaps. Keep narration intelligible, avoid harsh high-frequency clicks, and duck or trim accents under consonant-heavy speech. Rotate the sound identity across adjacent hero beats — for example bass impact, one glass shimmer, a digital servo or airy sweep, a dry clockwork tick, a mechanical toggle, then a final low impact. Reserve shimmer for a single luminous reveal, keep adjacent beats off the same chime, and never overlap high-frequency accents without a specific reason. Never imply generic SFX are part of any reference creator's licensed audio.

## Step 7 — Plan schema

Write `caption-design-plan.json` in this shape:

```json
{
  "version": 1,
  "range": { "start": 0, "end": 12.4 },
  "accent": "#7B5A49",
  "_accentNote": "Walnut on light grounds; Dusty Blue #C4D6DA on dark grounds",
  "cues": [
    {
      "id": "ecap-001",
      "semanticGroupId": "claim-01",
      "orderIndex": 2,
      "start": 0.42,
      "end": 1.58,
      "text": "electricity cheaper",
      "role": "contrast",
      "emphasis": "hero",
      "heroReason": "The reversal carries the claim; score 6",
      "placement": "shoulder-right",
      "anchorZone": "subject-right-hairline",
      "layoutState": "background-hero-with-foreground-support",
      "buildMode": "foreground-background-handoff",
      "flowDirection": "upper-left-to-lower-right",
      "persistenceGroup": null,
      "foregroundText": "electricity",
      "heroText": "cheaper",
      "stackGap": "0.28em-support",
      "subjectEnvelope": {
        "sampleTimes": [0.42, 1.0, 1.58],
        "protected": ["face", "mouth", "right-hand"]
      },
      "depthStrategy": "subject-cutout",
      "treatment": "neutral-silver-tinted-glass",
      "fillSource": "transparent-silver-white-with-soft-light-sweep",
      "palette": ["rgba(255,255,255,0.52)", "rgba(196,214,218,0.30)"],
      "occlusionBudget": 0.18,
      "motion": "firm-settle-with-soft-light-sweep",
      "graphic": null,
      "audioAccent": {
        "type": "muted-bass-impact",
        "start": 1.04,
        "gain": 0.18
      },
      "notes": "Keep 60 px clear of face"
    }
  ]
}
```

Use exact seconds. Keep cue IDs stable so markup, tracks, motion metadata, snapshots, and later revisions can all point at the same moment.

## Step 8 — HyperFrames implementation

- Put each cue on a dedicated overlay track or inside a caption sub-composition.
- For behind-subject type, layer base footage lowest, hero or proof type in the middle, and the foreground subject matte higher — with support copy above all three.
- Let outer clips own `data-start`, `data-duration`, placement, and bounds.
- Animate an inner `.ecap-motion` wrapper.
- Namespace IDs, classes, variables, and timeline labels with `ecap-`.
- Build one paused timeline and drive it from the HyperFrames time source.
- Use local fonts, media, and SFX; depend on no remote asset at render time.
- Record every animated selector and its properties in the motion sidecar.
- When you adapt a registry component, keep its contract and restyle it for the active project.

## Step 9 — Verification checklist

- Every spoken idea that needs support has a readable cue.
- Timing follows the semantic delivery, not an arbitrary interval.
- Every hero has a recorded reason and clears the threshold, or belongs to one documented parallel hero run.
- Ordinary support copy is mostly white and stacked with intentional hierarchy.
- Important numbers and places get a visibly larger proof tier when present.
- Layout changes fall between argument beats; fragments in one sentence or parallel list keep a stable anchor.
- Support copy uses mixed case unless a clear reason calls for all caps.
- Built-up phrases follow real word starts and never reveal the finished phrase early.
- Unrelated adjacent heroes vary one or two properties; parallel hero runs stay visually stable.
- Behind-subject claims correspond to a real matte or occlusion mask.
- The subject layer is frame-locked with no halo, doubled edge, shadow, or colour shift at hair, hands, or shoulders.
- Background heroes stay recognisable within their recorded occlusion budgets.
- Hero spelling is unambiguous; identifying internal glyphs are not hidden.
- Heroes use real bundled display weights — no synthetic bold, merged strokes, false crossbars, or crushed tracking.
- Each group holds its declared direction with no reversals.
- Every group reads in spoken order with consistent spacing and no orphaned fragments.
- Captions stay level unless an explicit rationale justifies rotation.
- Sequential instructional assets persist while the next step depends on them, with no generic framing on native assets.
- CTA fragments form one compact cluster and reveal in reading order.
- A dimensional translucent word uses one exact-font mask across fill, rim, highlight, and extrusion, with texture visible from its first readable frame.
- Tinted-glass heroes keep visible source detail through a 32–55% neutral or justified single-hue fill and sit close enough to a clean matte for 10–22% intentional overlap.
- Glow settles to crisp readable type.
- No foreground cue enters the recorded face/mouth envelope or covers a key gesture, product, UI, or scene detail.
- Caption contrast holds on the actual midpoint frame.
- Audio transients land with the visuals and never mask narration.
- Adjacent hero beats have distinct primary sound identities; shimmer happens once and no repeated chimes overlap.
- Motion stays correct when seeking directly to any cue.
- The chronological contact sheet reads as one coherent passage, not a stack of repeated centred cards.
- HyperFrames lint, runtime, layout, motion, and contrast checks pass.
