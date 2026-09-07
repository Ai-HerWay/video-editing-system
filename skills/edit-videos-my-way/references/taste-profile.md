# Taste Profile — Reference-Derived Creative Defaults

Derived from a frame-by-frame and waveform study of 12 curated high-performing reels on 2026-09-03 (source files in `C:\Users\nici\brand-design-system\ref video\`). These are not generic best practices — every rule below traces to a specific observed technique in a specific reel. Treat this file as the current creative defaults referenced in `SKILL.md` Start Here step 1. Update it when the user provides new reference videos or gives explicit current-turn preferences (those always win over this file).

## Locked Brand System (AI Her Way — Social/Reels)

Non-negotiable per the brand doc (`AI-Her-Way-Social-Design-System.md`). Every color/font choice below should resolve to these, not to invented approximations.

**Typography — no exceptions:** Playfair Display (every headline, stat, pull quote, italic accent) + Montserrat (body, small-caps eyebrows, labels, footers).

**Palette (10 colors, each with a defined role):**
| Color | Hex | Role |
|---|---|---|
| Espresso | `#35241F` | Dark tiles, anchor slides, dark grounds |
| Ink | `#2B1E19` | Body text on light grounds |
| Linen Cream | `#F2EBDD` | Cream tiles — quotes, statements |
| Ivory | `#FAF6EF` | Floated cards, lightest ground |
| Dusty Blue | `#C4D6DA` | Flat blue tiles; italic-accent/highlight color on **dark** grounds |
| Stone | `#C0CACE` | Small elements, hairline structure |
| Sage | `#AAB6A0` | Reassurance/reframe (green) |
| Deep Olive | `#46513D` | Opinion/hot-take (deep green) |
| Walnut | `#7B5A49` | Italic accent words on **light** grounds, small-caps eyebrows/labels |
| Gold | `#B08A62` | Hairline rule under headlines; rare hand-drawn/script accent |

**Signature devices:** (1) *Italic accent* — exactly one Playfair-italic word per headline, in Walnut (light bg) or Dusty Blue (dark bg). Described as "the single most recognisable element of the brand" — never skip it, never use on more than one word. (2) *Gold hairline* — a ~2px Gold rule directly under a headline. (3) *Highlight marker* — a word sitting on a color block (Dusty Blue, Espresso, Sage, or Walnut). (4) *Torn-paper + washi tape* — rationed, not maximalist.

Three of the style anchors below now exist as actual installed, brand-tuned HyperFrames skills rather than hand-built CSS: `/quiet-editorial-ui`, `/hyperframes-tactile-collage`, `/cinematic-caption`. Prefer invoking those over re-deriving their mechanics from this file's prose.

## Primary Aesthetic Anchors

Default to these three when no other direction is given — they are the closest match to the AI Her Way editorial/elegant brand, confirmed either by explicit user pick or by already being on-brand:

1. **Quiet Editorial UI** ("I turned my fav editing styles into Skills," 0:40) — now the installed `/quiet-editorial-ui` skill (brand-tuned to Playfair Display + Montserrat, the palette above). Calm, well-lit talking head; clean captions with no pill/box; restrained palette; section cards rendered as elegant serif objects floating on **frosted-glass panels**; signature move is **background rack-focus blur** — the speaker blurs out of focus as a UI panel slides in, re-sharpens when it exits. No memes, no torn-paper, no red arrows. The reel demonstrates the aesthetic it's describing — the edit style IS the pitch.
2. **Cinematic Narrative B-roll** ("this is like watching TV," the user's explicit reference pick, 92s) — opens with **no talking head at all**: a staged narrative action (walking into a room, reaching for a prop, sitting) shot with shallow depth of field, cuts on the action (a match/whip beat), before revealing the speaker. Uses a **second caption register**: alongside plain white word-by-word captions, a **handwritten red-marker/script-font layer** in the margins carries editorial asides ("Netflix is shaking in their boots," "camera angles"). Borrows a real audience comment as the on-screen hook. Cuts land on audio transients (genuine sound design, not just voice).
3. **Radical-Transparency Screen-Record** (existing AI Her Way footage, "how I use AI to add motion graphics," 94s) — talking-head intercut with full-frame screen-recording every 5-10s; the actual prompt typed into Claude is shown streaming on screen; a persistent top title caption; karaoke bottom captions; near-silent audio bed (voice does all the work). Authenticity over polish; the "b-roll" is real software UI, not stock footage or generated graphics.

When the user gives no visual-style steer, default to anchor 1 or 2 for short/punchy pieces and anchor 3 for build-along tutorials, then apply the universal structural patterns below regardless of chosen skin.

## Universal Structural Patterns (apply to any skin)

- **Persistent visual spine.** Every reel studied keeps one recurring on-screen element alive for the whole runtime while the face stays relatively static: a held prop card, a locked numbered-chip HUD, a floating title, frosted-glass panels, a magazine-cover wall. The talking head alone is never the whole visual — build the reel around what overlays the face, not just what cuts the face.
- **Text-first hook that previews the payoff inside 3 seconds.** Every winning hook front-loads either the full value contract (a chip grid showing all 9 questions at once; "5 STEPS" stamped; the whole numbered list glimpsed early) or a sharp curiosity gap (a versus framing, a borrowed comment, a cold open with no face). Never open on a slow verbal windup.
- **Two caption registers, not one.** (1) A plain, undesigned "meta" layer — the persistent title card or karaoke word-by-word captions, centred or top, small, no heavy styling. (2) A styled "content" layer that carries the brand skin — torn-paper stickers, serif editorial cards, frosted-glass panels, or a handwritten annotation layer. Never let the styled layer do the captioning job or the plain layer do the branding job.
- **Progressive/numbered structure with a visible remaining-count.** "5 Steps," "9 Questions," "4 Repos," "7 Modes" — stated as a number in the hook, then paid off one item at a time with a visual checklist, chip highlight, or finger-count that shows how much is left. This is the single strongest completion-loop mechanic across the set.
- **Proof beats promise.** Every high performer substitutes a claim with visible evidence: real UI screen-recordings, an actual typed prompt, a split-screen "original vs AI," real follower-growth numbers, an annotated screenshot with red arrows/boxes. Never describe a result the edit can show.
- **CTA = one short keyword to comment, not a sentence.** "Skill," "Repo," "+", "Jarvis," "Intake," "Toolkit," "Department." Shown as a styled sticker/card held for the final 2-3 seconds. Shorter keyword = lower friction = more comments = more reach. Reserve a softer/implicit CTA (the payoff itself seeds the next piece of content) for save-worthy long-form build-alongs.
- **Sound is voice-led with a near-silent bed by default.** 10 of 12 studied reels are VO-forward with a flat waveform — pacing comes from visual/caption cuts, not music beats. Reserve hard beat-synced cuts and audible transient "whoosh" hits for (a) pure motion-graphic/no-VO pieces (the AE-vs-Claude poster loop) and (b) cinematic narrative-B-roll pieces where a cut lands on a physical action (remote-point → Netflix reveal).
- **One recurring accent colour, often worn on-body.** A lime top matched to a lime UI highlight; an orange Claude-brand accent; a teal accent chip. For AI Her Way, this is the locked italic-accent rule: Walnut on light grounds, Dusty Blue on dark — repeat it in graphics + the CTA text colour, and in wardrobe where possible.
- **Length maps to intent.** 10-15s = punchy proof/versus loops built to rewatch. 40-60s = a single named technique or short list. 60-110s = a save-worthy numbered build-along or listicle. Match length to how many numbered beats the content actually has — don't pad.

## Hook Pattern Library (pick one deliberately, don't default to plain talking-head)

- **Versus/comparison** — two labelled panels or pill-tabs racing side by side ("Original vs AI Remake," "Claude vs Claude×BYQ").
- **Cold-open narrative, no face** — a staged physical action shot cinematically before the speaker appears or speaks to camera.
- **Borrowed comment** — a real screenshot of someone else's comment/DM used as the literal opening hook text.
- **Full-payload preview** — the entire content map (all N items) appears as a HUD/grid in the first 2 seconds, so the viewer sees exactly what they're signing up for.
- **Contrarian claim, word-by-word** — "most people tell AI what to do, but the people who…" — sets up a reversal before revealing it.
- **Prop-driven** — physically holding up a card, phone, or object that becomes a recurring cutaway surface for the rest of the reel.

## Caption System Spec

For the full hero-word scoring, placement, and motion framework, use the installed `/cinematic-caption` skill (brand-pinned: Montserrat support, Playfair Display Black hero, Playfair Display Italic editorial-accent in Walnut/Dusty Blue, Gold rule-draw). Quick reference:

- Base layer: white or off-white, bold, sentence-case or single-word pop-on, centred, mid-lower third, no background pill for the editorial-anchor look (anchors 1-2) — a soft dark pill/shadow is acceptable for the transparency-anchor look (anchor 3).
- Word-reveal cadence: one to two words at a time for dense/fast content (listicles, contrarian hooks); full short phrases (2-7 words) for slower build-alongs.
- Styled layer only when it reinforces the brand skin: serif "editorial" cards on frosted glass (anchor 1), handwritten red-marker asides (anchor 2), or torn-paper stickers via `/hyperframes-tactile-collage` (secondary — use selectively, see below).
- Never let captions sit in a fixed bottom safe-zone band that the rest of the composition has to avoid — they're an overlay on top of the frame, composited over whatever is there.

## CTA Mechanics

- Default: single keyword comment → implied auto-DM delivery of a named asset (a prompt, a guide, a template). State the keyword once as spoken audio and once as a held on-screen sticker for the last 2-3 seconds.
- Cross-platform stack (seen once, worth reusing): a pinned "long-form version on YouTube" card plus a comment-keyword CTA in the same close — captures both the warm long-form lead and the impulse comment.
- Soft/implicit CTA: end on the payoff itself (a finished reel-within-the-reel, a magazine-cover wall of past work) when the goal is authority/follow rather than an immediate lead-capture ask.

## Visual/Animation Device Library

- Background rack-focus blur when a UI/graphic panel slides over the speaker (anchor 1's signature move — calm, continuous, no hard cut needed).
- Floating proof-cards / screenshots swapped every 2-3 seconds over the speaker's shoulder to keep the frame busy during long-form talking segments.
- Numbered chip/HUD grid locked to the top of frame, with the active item highlighted as it's discussed.
- Kinetic kinetic-type kinetic assembly (brutalist poster style) for a no-face, pure-craft flex piece — acid-accent colour, torn-paper/newsprint texture, continuous looped motion rather than hard cuts.
- Match/whip cuts motivated by a physical action (a remote-point, a door-open) rather than an arbitrary hard cut.
- Annotated real screenshots (red arrows, circles, boxes) as the primary credibility device for any technical/build-along content.

## Secondary Devices (borrow selectively, don't default to)

- Torn-paper/ransom-note headline stickers and meme reaction PIPs — high-energy and effective for younger/louder AI-education content, but off-brand for AI Her Way's editorial register as a *default*; use only if the user explicitly asks for a punchier/meme-adjacent tone. When used, invoke the installed `/hyperframes-tactile-collage` skill (brand-tuned: Linen Cream/Ivory paper tones, Ink linework, Playfair Display statements, Montserrat captions, Gold hand-drawn marks) rather than hand-building torn-paper CSS.
- Hand-count finger gestures synced to a numbered list — fine for casual creator pieces, skip for the quiet-editorial anchor.

## Applying This to New WhatsApp Raw Footage — Default Recipe

1. Pick a hook pattern (Hook Pattern Library) that fits the actual footage — don't force a versus/cold-open if the raw clip doesn't support it.
2. Choose one of the three Primary Aesthetic Anchors as the skin; don't mix frosted-glass panels with torn-paper stickers in the same reel.
3. Build the persistent visual spine first (what overlays the face for the whole runtime), then place cuts/punch-ins around it.
4. Write captions in two registers per the Caption System Spec.
5. If the content is a list or has a countable structure, state the count in the hook and pay it off progressively with a visible remaining-count device.
6. Replace every claim with visible proof (screen-recording, screenshot, real number) wherever the footage allows it.
7. End on one short keyword CTA, held 2-3 seconds, unless the piece is authority/portfolio-building — then end on the payoff itself.
8. Keep the audio bed near-silent under voice unless the piece is a no-VO motion/B-roll piece, in which case sync cuts to audio transients.
