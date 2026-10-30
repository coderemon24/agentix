---
name: typography-and-color-theory
description: Deep typography and color theory skill. Establishes mathematical type scales, optical adjustments, semantic color roles, 60-30-10 distribution, and WCAG accessibility standards.
---

# Typography & Color Theory

## Purpose
Apply mathematical precision and cognitive science to typography and color palettes. Ensure exceptional legibility, balanced visual weight, harmonious emotional resonance, and full WCAG 2.1 AA/AAA compliance across all user interfaces.

## When to Use
- When defining design tokens and CSS variables (Gate 3).
- When pairing fonts or tuning line-height, letter-spacing, and text hierarchy.
- When resolving poor contrast, unreadable data tables, or chaotic accent colors.

## 1. Typography Principles & System

### 4-Tier Typographic Scale
Every interface must adhere to a strict 4-tier typographic hierarchy:
1. **Tier 1: Display & Page Headlines**:
   - Desktop: `36px – 48px` (`text-3xl` to `text-5xl`), Line-height: `1.15 – 1.25`, Font-weight: `700` or `800`.
   - Purpose: Establish immediate context and authority. Include exactly ONE focal accent span.
2. **Tier 2: Section & Card Titles**:
   - Desktop: `18px – 24px` (`text-lg` to `text-2xl`), Line-height: `1.3 – 1.4`, Font-weight: `600` or `700`.
   - Purpose: Chunk content logically; clear scannability for fast reading.
3. **Tier 3: Body & Content Text**:
   - Desktop: `14px – 16px` (`text-sm` to `text-base`), Line-height: `1.6 – 1.7` (`leading-relaxed`), Font-weight: `400` or `500`.
   - Line length rule: Maintain `45 – 75` characters per line (`max-w-prose`) for optimal reading speed.
4. **Tier 4: Kickers, Badges & Meta Text**:
   - Desktop: `11px – 13px` (`text-xs`), Line-height: `1.4`, Letter-spacing: `0.05em` (`tracking-wider`), Font-weight: `600` or `700`.
   - Purpose: Categorical signaling, status pills, timestamps.

### Font Pairing Rules
- Pair a display face with personality (e.g., Editorial Serif or Sturdy Grotesque) with a workhorse geometric or humanist sans-serif body (e.g., Inter, Plus Jakarta Sans, SF Pro, or Noto Sans for Bengali/multilingual).
- Ensure script harmony: when rendering non-Latin scripts (e.g., Bengali, Arabic), increase line-height by `+0.15` and adjust base font size by `+1px` to prevent glyph collision.

---

## 2. Color Theory & Semantic Distribution

### The 60-30-10 Rule
Distribute interface colors with disciplined intent:
- **60% Dominant Canvas / Neutral**: Clean surfaces, calm backgrounds (`bg-slate-50`, `bg-white`, `border-slate-200/90`). Prevents cognitive exhaustion.
- **30% Structural / Secondary Neutral**: Deep institutional slate/gray for text, headers, and container framing (`text-slate-900`, `text-slate-600`, subtle panel fills).
- **10% Intentional Accent**: High-contrast, semantic colors strictly reserved for conversion, status, and focal points.

### Semantic Color Roles (EduCore Standard)
1. **Brand Primary Accent (Institutional Green `#005030` / `#004027`)**:
   - Used for: Primary navigation active states, focal headline spans, institutional badges.
2. **Primary Conversion Action (Warm Amber `amber-500` / `#f59e0b`)**:
   - Strictly reserved for: Admission, Registration, Checkout, Primary Submit actions. Never used for non-actionable decor.
3. **Information & Notice (Sky Blue `sky-600` / `#0284c7`)**:
   - Strictly reserved for: Bulletins, routine notices, informational callouts.
4. **Success (Emerald `emerald-600` / `#059669`)**:
   - Strictly reserved for: Completed transactions, verified attendance, passing grades.
5. **Warning & Danger (Rose `rose-600` / `#e11d48`)**:
   - Strictly reserved for: Overdue fees, disciplinary alerts, destructive delete actions.

### Contrast Standards (WCAG 2.1)
- **Normal Text (< 18px)**: Minimum `4.5:1` contrast ratio against surface.
- **Large Text (>= 18px bold or >= 24px regular)**: Minimum `3.0:1` contrast ratio.
- **UI Components & Icons**: Minimum `3.0:1` contrast ratio against adjacent surfaces.

## Deliverables
- Color and typography definitions integrated into `DESIGN_SYSTEM.md`, `DESIGN_TOKENS.md`, and `design-tokens.css`.
- WCAG contrast verification matrix.

## Quality Checklist
- [ ] Are all text elements meeting minimum 4.5:1 contrast?
- [ ] Is body copy line-height set to leading-relaxed (1.6+)?
- [ ] Is line length capped at 75 characters max?
- [ ] Is warm amber strictly isolated to primary conversion actions?
- [ ] Are all font families loaded with specified weights and display swap?

