# Design

## Theme

Light mode only. White body (`#fff`) with a warm near-neutral surface (`#f5f5f3`). Primary brand color is CPA green — authoritative without being flashy. Typography pairs Playfair Display (serif, display) with Open Sans (sans-serif, body) — a classic contrast-axis pairing that signals professional credibility.

## Colors

| Token | Value | Role |
|---|---|---|
| `--g` | `#3A9E49` | Brand green — primary CTA, links, accents |
| `--gd` | `#2C7A38` | Dark green — hover states, pressed buttons |
| `--gl` | `#E8F7EA` | Light green tint — card backgrounds, badges, highlights |
| `--gm` | `#d4efda` | Mid green tint — borders on green-tinted elements |
| `--blk` | `#111` | Near-black — headings, strong emphasis |
| `--ink` | `#1a1a1a` | Body text default |
| `--body` | `#444` | Secondary body text, prose paragraphs |
| `--muted` | `#777` | Captions, metadata, placeholder labels |
| `--light` | `#f5f5f3` | Section backgrounds (alternating), stats bar |
| `--bdr` | `#e0e0db` | Borders, dividers, card outlines |
| `--wht` | `#fff` | Card fills, page background, button text on dark |

**Dark surfaces:** Footer and topbar use `#111312` (near-black) and `#2C7A38` respectively. CTA band uses `--g` as full-bleed background.

**Note:** All tokens are hex. A future pass should migrate to OKLCH for perceptual consistency and easier tint derivation.

## Typography

### Typefaces

| Role | Family | Fallback |
|---|---|---|
| Display / Headings (`--fh`) | Playfair Display | Georgia, serif |
| Body / UI (`--fb`) | Open Sans | system-ui, sans-serif |

Loaded via Google Fonts: `Playfair Display` at 400, 600, 700, 800, italic 700; `Open Sans` at 400, 500, 600, 700.

### Scale

| Element | Family | Size | Weight | Notes |
|---|---|---|---|---|
| Hero h1 | `--fh` | `clamp(34px, 5vw, 62px)` | 800 | `letter-spacing: -.025em`, `line-height: 1.05` |
| Section h2 (`.sh2`) | `--fh` | `clamp(26px, 3.4vw, 40px)` | 700 | `letter-spacing: -.02em`, `line-height: 1.15` |
| Page hero h1 | `--fh` | `clamp(28px, 4vw, 48px)` | 700 | Dark-bg hero variant |
| Article h2 | `--fh` | 27px | 700 | `.art-body h2` |
| Article h3 | `--fh` | 22px | 700 | `.art-body h3` |
| FAQ question | `--fh` | 17px | 700 | Accordion trigger |
| Card heading (service) | `--fh` | 19px | 700 | White on dark photo overlay |
| Blog card h3 | `--fh` | 18px | 700 | `line-height: 1.25` |
| Section lead (`.sec-lead`) | `--fb` | 16.5px | 400 | `max-width: 620px`, `line-height: 1.72` |
| Hero sub | `--fb` | 17px | 400 | `max-width: 500px`, `line-height: 1.72` |
| Body prose | `--fb` | 15.5px | 400 | `line-height: 1.78` |
| Review quote | `--fb` | 14.5px | 400 (italic) | `line-height: 1.65` |
| Eyebrow (`.eyebrow`) | `--fb` | 11.5px | 700 | `letter-spacing: .16em`, uppercase, green |
| Nav links | `--fb` | 12.5px | 600 | |
| Buttons | `--fb` | 13px | 700 | `letter-spacing: .07em`, uppercase |
| Topbar | `--fb` | 12.5px | 500 | |

### Body defaults

```css
body { line-height: 1.7; -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; }
```

## Spacing & Layout

**Container:** `max-width: 1240px; margin: 0 auto; padding: 0 32px`

**Section padding:** `72px 0` desktop → `52px 0` at ≤800px

**Section alternation:** White sections alternate with `--light` (`#f5f5f3`) backgrounds. CTA band uses `--g` (green).

**Grid patterns:**
- Hero: `grid-template-columns: 1fr 1fr; gap: 52px`
- Services: `grid-template-columns: repeat(3, 1fr); gap: 22px`
- Pain points: `grid-template-columns: repeat(3, 1fr); gap: 28px`
- Industries: `grid-template-columns: repeat(4, 1fr); gap: 22px`
- Reviews: `grid-template-columns: repeat(3, 1fr); gap: 20px`
- Footer: `grid-template-columns: 1.9fr 1fr 1fr 1.15fr; gap: 48px`

**Mobile breakpoint:** 1140px (hamburger nav). Grids collapse to 1 column at ≤800px for most layouts.

## Border Radius

| Token | Value | Usage |
|---|---|---|
| `--r` | `5px` | Buttons, form inputs, small elements |
| `--rl` | `12px` | Cards, modals, image containers |

## Shadows

| Token | Value | Usage |
|---|---|---|
| `--sh` | `0 1px 8px rgba(0,0,0,.06)` | Cards at rest (subtle lift) |
| `--shm` | `0 4px 24px rgba(0,0,0,.1)` | Hover states, dropdown menus |
| `--shl` | `0 8px 48px rgba(0,0,0,.14)` | Heavy hover, hero photo |

## Components

### Buttons

| Class | Background | Text | Usage |
|---|---|---|---|
| `.btn-gp` | `--g` | white | Primary CTA (hero, sections) |
| `.btn-dk` | `#111` | white | Secondary dark button |
| `.btn-ol` | transparent | `--g` | Outline — tertiary actions |
| `.btn-p` | `--g` | white `!important` | General page CTA |
| `.btn-gp-sm` | `--g` | white | Compact CTA |
| `.btn-gh` | transparent | `--ink` | Ghost button |
| `.btn-w` | white | `--gd` | CTA on green band |
| `.btn-wg` | transparent | white | Ghost on green band |
| `.nav-cta-btn` | `--g` | white | Nav "Contact Us" |
| `.fsub` | `--g` | white | Form submit button |

All buttons: `font-size: 13px; font-weight: 700; letter-spacing: .07em; text-transform: uppercase; border-radius: var(--r)`

Hover: `background: --gd; transform: translateY(-1px to -2px)`

### Service Card (`.svc-card`)

Full-bleed photo card with dark gradient overlay from bottom. Label + link sit in absolute-positioned overlay at bottom. Hover: `translateY(-5px)` + photo `scale(1.06)`.

### Review Card (`.rc`)

White card, `1.5px solid --bdr`, `border-radius: --rl`. Contains: star string (✦), italic quote, avatar initial circle (green tint), reviewer name + source.

### FAQ Accordion (`.faq-it`)

Border-bottom divider. Toggle triggered by click. `+` / `−` indicator in brand green. Heading in `--fh`, answer in `--fb`.

### Blog Card (`.bc`)

White card with overflow:hidden. Top image area (168px, green tint bg). Body with category tag (green uppercase), heading, excerpt, read link. Full flex column.

### Team Card (`.tc`)

White card with hover lift. Avatar: 64px circle, green tint bg, initials in `--fh`. Name, title (green uppercase), bio text.

### Photo Split (`.photo-split`)

Two-column layout: content left (headline, bullets, CTA) + Unsplash photo right. Rounded image. Used on service pages.

### Image Band (`.svc-imgband`)

Full-bleed dark section with `rgba` overlay on a background image. 2×2 stats grid (`istat` items). Used mid-page on service pages.

### Form Card (`.form-card`)

White card, `1.5px solid --bdr`, `border-radius: --rl`, `box-shadow: --sh`. Label: 12px bold uppercase. Input: 14.5px, focus ring in `--g`. Textarea: `min-height: 108px`.

### Article CTA Box (`.art-cta`)

Light green background (`--gl`), green border. Heading in `--fh`, body, centered `btn-p` button. Used mid-article for in-content lead capture.

## Header & Navigation

**Topbar:** `--gd` background. Address left, phone + email right. 12.5px Open Sans.

**Site header:** White background, `3px solid --g` bottom border. Logo (42px height) left. Nav links + dropdown + `.nav-cta-btn` right. Sticky on scroll (`.scrolled` class adds shadow).

**Hamburger breakpoint:** 1140px. Mobile nav slides in from right, `border-top: 2px solid --g`.

## Footer

**Background:** `#111312` (near-black). **Top border:** `3px solid --g`.

**Brand lockup:** Green tile `IH` (50×50px rounded square, `--g` bg) + white wordmark in Playfair Display.

**Grid:** 4-column (brand desc / quick links / services / contact). Collapses to 2-col at 800px, 1-col at 500px.

**Bottom bar:** `1px solid rgba(255,255,255,.09)`. Copyright left, Privacy Policy + Terms links right. 13px Open Sans.

## Page Sections (Recurring Patterns)

| Section | Background | Top Pattern |
|---|---|---|
| Hero | `--wht` | Split grid: content left, photo right |
| Stats bar | `--light` | 4-column stat grid |
| Services | `--wht` | `eyebrow` + `.sh2` + 3-col photo cards |
| Pain points | `--light` | `eyebrow` + `.sh2` + 3-col text cards |
| Process | `--wht` | `eyebrow` + `.sh2` + 3-col numbered steps |
| Image band | Unsplash photo + dark overlay | Full-bleed |
| Local | `--wht` | Split: content left, photo right |
| Industries | `--light` | 4-col text cards |
| Reviews | `--wht` | 3-col review cards |
| FAQ | `--light` | Accordion |
| CTA | `--g` (green) | Centered headline + dual buttons |
| Footer | `#111312` | 4-col grid |

## Known Issues & Improvement Targets

- **Eyebrow overuse:** `.eyebrow` appears before nearly every section heading — a pattern the SKILL.md flags as a saturated AI tell. Future work should reduce cadence to 1–2 deliberate placements per page.
- **Color system in hex:** Tokens should migrate to OKLCH for contrast-safe tint derivation.
- **Body color contrast:** `--body: #444` on `--wht: #fff` yields ~9.7:1 (fine). `--muted: #777` on white is ~4.48:1 — borderline AA. Check on tinted section backgrounds.
- **No motion system:** Zero scroll animations, reduced-motion not declared. Future animate pass has a clean slate.
- **Card-grid dominance:** Pain points, industries, and reviews are all uniform card grids — reduces visual variety across the scroll.
