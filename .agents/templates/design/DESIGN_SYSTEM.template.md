# Design System Manual: [Project Name]

> **Gate**: Gate 3 — Design System Approval  
> **Prepared by**: [design-engineer]  

---

## 1. System Foundations
The design system provides a unified visual language and component architecture for EduCore. Built on systematic tokens, fluid responsive grids, accessible WCAG 2.1 AA contrast rules, and human-crafted anti-slop principles.

---

## 2. Token Architecture Overview
Tokens are exported as CSS variables in `design-tokens.css` and mapped to Tailwind configuration:
1. **Brand & Semantic Colors**: Institutional green, amber conversion, sky blue notice, emerald success, rose alert.
2. **Typography Scale**: 4 tiers (Display 36–48px, Title 18–24px, Body 14–16px, Kicker 11–13px).
3. **Spacing Scale**: 8-point base grid with 4-point micro-steps (`4px`, `8px`, `12px`, `16px`, `24px`, `32px`, `48px`, `64px`).
4. **Elevation & Borders**: Hairline `1px` borders (`#e2e8f0`), soft diffused shadows.
5. **Container & Breakpoints**: Mobile 375px, Tablet 768px, Desktop 1024px, Widescreen 1440px.

---

## 3. Reusable UI Recipes (The 7 Master Recipes)
1. **Sharpen the Message**: Grounded copy with exactly ONE focal accent span: `<span class="text-[#005030] font-bold">`.
2. **Break the Symmetry**: 60/40 or 65/35 grid (`lg:grid-cols-12`) with floating anchor badges.
3. **Build the Argument**: Uniform `.section-header-block` (kicker + title + subtitle) and hairline dividers `.home-section-divider`.
4. **Pick the Winner**: Elevate flagship item (60% weight) over identical cards.
5. **Scale the Type**: 4-tier scale with `leading-relaxed` on body text.
6. **Give Color Meaning**: Respect semantic color roles.
7. **Add a Signature**: Section kicker with pulsing dot (`.section-kicker-dot`), hairline dividers, and micro-interactions.

