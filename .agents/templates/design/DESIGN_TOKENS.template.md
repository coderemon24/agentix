# Design Tokens Specification: [Project Name]

> **Gate**: Gate 3 — Design System Approval  
> **Source of Truth for**: `design-tokens.css` and Tailwind Config  

---

## 1. Color Palette Tokens

### Brand & Accents
| Token Name | CSS Custom Property | Hex Value | Usage / Role |
| :--- | :--- | :--- | :--- |
| `color.brand.primary` | `--color-brand-primary` | `#005030` | Core institutional brand green |
| `color.brand.dark` | `--color-brand-dark` | `#004027` | Deep header bar, dark badges |
| `color.brand.light` | `--color-brand-light` | `#e6f0ec` | Soft green tint for active cards |
| `color.action.cta` | `--color-action-cta` | `#f59e0b` | Warm amber strictly for primary conversions |
| `color.action.cta-hover`| `--color-action-cta-hover`| `#d97706` | Hover state for primary buttons |
| `color.notice.sky` | `--color-notice-sky` | `#0284c7` | Bulletins and routine notices |

### Neutrals & Surfaces
| Token Name | CSS Custom Property | Hex Value | Usage / Role |
| :--- | :--- | :--- | :--- |
| `surface.canvas` | `--surface-canvas` | `#ffffff` | Primary page background |
| `surface.muted` | `--surface-muted` | `#f8fafc` | Table headers, secondary panels |
| `surface.card` | `--surface-card` | `#ffffff` | Content card background |
| `border.default` | `--border-default` | `#e2e8f0` | Standard hairline card borders |
| `text.primary` | `--text-primary` | `#0f172a` | High-contrast body & headlines |
| `text.secondary` | `--text-secondary` | `#475569` | Supporting subtitles & metadata |
| `text.muted` | `--text-muted` | `#64748b` | Kickers, captions, disabled text |

---

## 2. Spacing Scale Tokens
- `--space-1`: `0.25rem` (4px)
- `--space-2`: `0.5rem` (8px)
- `--space-3`: `0.75rem` (12px)
- `--space-4`: `1rem` (16px)
- `--space-6`: `1.5rem` (24px)
- `--space-8`: `2rem` (32px)
- `--space-12`: `3rem` (48px)
- `--space-16`: `4rem` (64px)

---

## 3. Typography Tokens
- `--font-sans`: `'Plus Jakarta Sans', system-ui, -apple-system, sans-serif`
- `--font-display`: `'Newsreader', Georgia, serif`
- `--font-bengali`: `'Noto Sans Bengali', sans-serif`
- `--text-display`: `2.5rem` (40px) / Line-height `1.2`
- `--text-title`: `1.25rem` (20px) / Line-height `1.35`
- `--text-body`: `0.9375rem` (15px) / Line-height `1.65`
- `--text-kicker`: `0.75rem` (12px) / Line-height `1.4` / Letter-spacing `0.05em`

