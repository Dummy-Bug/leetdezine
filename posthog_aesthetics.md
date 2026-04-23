# PostHog Aesthetics — LeetDezine Redesign Plan

What we're going for: warm sandy texture, app-window card style, bold typography,
personality. No desktop OS icons for now. All changes are CSS + index.md only —
no framework rebuild, ships in one push to master.

---

## Step 1 — Palette swap (extra.css)

Replace the cold white surfaces with warm cream/sand tones.

Current `--surface-0` is `#ffffff`. PostHog's background is closer to `#f3efe3`
(warm parchment). Every surface gets a warm shift.

Token changes for `[data-md-color-scheme="default"]`:

```
--surface-0:          #f3efe3   (was #ffffff — main page bg, parchment)
--surface-1:          #ede9da   (was #fafafa — slightly darker sand)
--surface-2:          #e6e1d0   (was #f5f5f5)
--surface-raised:     #faf7f0   (was #ffffff — cards sit slightly lighter than bg)
--surface-sidebar:    #ece8d8   (was #f7f8fa)
--surface-sidebar-hover: #e0dbc9 (was #eef2f6)
```

Text stays dark (`#1a1208` — very dark warm brown instead of pure black `#0a0a0a`).
Borders shift warm too — `#c8c0a8` instead of `#d4d4d4`.

Brand stays emerald — it pops beautifully on sand.

Keep the dark scheme (`slate`) mostly as-is. PostHog's interior is light;
dark mode is a bonus feature, not the hero.

---

## Step 2 — Grain texture overlay (extra.css)

PostHog's background has a subtle paper grain. Pure CSS, zero images needed.

Add a `::before` pseudo-element on `body` using an SVG-based noise filter:

```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.035;
  background-image: url("data:image/svg+xml,...");  /* SVG turbulence noise */
}
```

The SVG uses `feTurbulence` with `baseFrequency="0.65"` — that's the fine grain
PostHog uses, not the coarse noise you see on cheap sites. Opacity stays at 0.03–0.04
so it's subliminal: you feel it, you don't see it.

---

## Step 3 — Typography overhaul (extra.css)

PostHog headings are heavy, confident, and have optical tightness.

Changes:
- `h1` font-weight: `800` (currently likely `700`)
- `h1` letter-spacing: `-0.03em` (tight, magazine-style)
- `h2` font-weight: `700`, letter-spacing: `-0.02em`
- Line height on body text: `1.7` (PostHog reads airy despite density)
- Hero title on landing: bump to `clamp(2.4rem, 5vw, 3.8rem)` — should feel big

The font stays Inter — it handles weight 800 well and PostHog actually uses a
similar grotesque. No font swap needed.

---

## Step 4 — App-window card on the landing hero (index.md + extra.css)

This is the signature PostHog move. The hero content renders inside a bordered
"application window" — complete with the three traffic-light dots (close/minimize/maximize).

HTML structure to wrap around the existing `.cs-hero` section:

```html
<div class="ph-window">
  <div class="ph-window-bar">
    <span class="ph-dot ph-dot-red"></span>
    <span class="ph-dot ph-dot-yellow"></span>
    <span class="ph-dot ph-dot-green"></span>
    <span class="ph-window-title">leetdezine.com</span>
  </div>
  <div class="ph-window-body">
    <!-- existing cs-hero content goes here -->
  </div>
</div>
```

CSS for `.ph-window`:
- Background: `--surface-raised` (slightly lighter than page bg)
- Border: `1.5px solid` warm border color
- Border-radius: `12px`
- Box-shadow: layered warm shadow (not blue-tinted, warm brown shadow)
- The `.ph-window-bar` is `40px` tall, sand-colored, flex row with the dots
- Dots are `12px` circles: red `#ff5f57`, yellow `#ffbd2e`, green `#28c840`
- Window title in the bar is centered, small, muted — `font-size: 0.75rem`

This single element elevates the whole page immediately.

---

## Step 5 — Concept cards redesign (extra.css)

Current cards are flat with subtle borders. PostHog cards have:
- Visible border (not subtle)
- Warm background slightly offset from page bg
- A colored left-accent bar or top border per card
- Hover: card lifts with warm shadow + slight Y translate (-2px)

Changes to `.cs-concept-card`:
- Background: `var(--surface-raised)`
- Border: `1.5px solid var(--border-strong)`
- On hover: `box-shadow: 0 8px 24px rgba(139, 115, 75, 0.15)` — warm amber shadow
- `transform: translateY(-2px)` on hover
- `transition: all 0.15s ease`
- Remove current muted palette, let the warm bg do the work

---

## Step 6 — Journey steps (case study cards) redesign (extra.css)

The current journey rail is clean but forgettable. PostHog makes you feel
like you're leveling up through a game.

Changes to `.cs-journey-step`:
- Add a visible warm-bordered card style (same as concept cards above)
- The step number marker gets bigger: `2.5rem`, bold, warm amber color `#b45309`
- The difficulty dots get replaced with a cleaner pill: `●●○○○` stays but styled
  as a small rounded badge with amber background on filled dots
- Step tag (Foundation, Ascent, etc.) gets a distinct color per tier:
  - Foundation: amber `#d97706`
  - Ascent: emerald `#059669`
  - Expedition: blue `#2563eb`
  - Summit: violet `#7c3aed`
  - Battleground: rose `#e11d48`
- Each tier tag becomes a colored pill badge, not just plain text

---

## Step 7 — Navbar personality (mkdocs.yml + extra.css)

PostHog's nav has colored icons per product. We can't do SVG icons in MkDocs nav
without a custom override, but we can add emoji icons to the nav titles in mkdocs.yml:

```yaml
nav:
  - "🧠 Concepts": 01-Concepts/...
  - "📐 Estimation": 02-Back-of-Envelope-Estimation/...
  - "⚔️ Case Studies": 03-Case-Studies/...
```

This is low-effort but adds that "each section has a visual identity" feel that
PostHog nails in their mega-menu.

Also: make the active nav tab have a warm amber underline instead of the current
brand-colored underline — closer to PostHog's tab style.

---

## Step 8 — Section dividers (index.md + extra.css)

PostHog uses horizontal rules that feel like section breaks in a document —
not just lines, but lines with a label centered on them.

Current `.cs-section-divider` is already close. Enhancement:
- Make the line a warm dashed border (`border-top: 1.5px dashed var(--border-strong)`)
- The label pill gets a warm background (`--surface-raised`) with the sand color
- Add a small icon/emoji before the label text in the HTML

---

## Step 9 — Footer note (index.md + extra.css)

Add a small "made by an engineer, for engineers" footer personality line at the
bottom of the landing — PostHog's footer has character, not just links.

Replace the current generic `.cs-footer-note` copy with something opinionated:

```
Built by one engineer. No VC money, no paywalls.
Just the internals you actually need to pass the interview — and survive the job.
```

Style it like a sticky note or a terminal prompt line for personality.

---

## Execution order

Do these in sequence — each step is independently shippable:

1. Step 1 + 3 — palette + typography (biggest immediate impact, 1 file change)
2. Step 2 — grain overlay (subtle but makes the warmth feel real)
3. Step 4 — app-window card on hero (the wow moment)
4. Step 5 + 6 — card redesigns
5. Step 7 — nav emoji
6. Step 8 + 9 — dividers + footer polish

Total estimated CSS lines added/changed: ~300–400
Files touched: `extra.css`, `index.md`
Files untouched: `mkdocs.yml` (except nav labels), all docs content

No build tool changes. No new dependencies. One `git push` to deploy.
