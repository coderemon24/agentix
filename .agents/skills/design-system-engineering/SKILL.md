---
name: design-system-engineering
description: Design system engineering skill. Produces structured tokens (JSON/CSS), CSS variable files, component inventories, interaction states, and accessibility contracts.
---

# Design System Engineering

## Purpose
Engineer scalable, maintainable, production-ready design systems. Translate abstract visual directions into unambiguous, machine-readable design tokens, CSS custom properties, and modular component guidelines that developers can implement without guessing.

## When to Use
- In Phase 2: Design System Engineering (Gate 3).
- When creating reusable UI tokens, buttons, forms, tables, cards, dialogs, or navigation components.
- When establishing brand-to-code synchrony across frontend teams.

## 1. Design Token Architecture

Design tokens are organized into 3 tiers:
1. **Global Tokens (Primitive Values)**:
   - Raw color hexes, pixel spacing, raw font stacks (e.g., `--color-green-900: #004027;`, `--space-4: 1rem;`).
2. **Semantic / Contextual Tokens**:
   - Meaning-bearing aliases (e.g., `--color-brand-primary: var(--color-green-900);`, `--surface-card: #ffffff;`, `--text-headline: var(--color-slate-900);`).
3. **Component Tokens**:
   - Component-scoped mappings (e.g., `--btn-primary-bg: var(--color-cta);`, `--card-border: var(--border-subtle);`).

## 2. Core Token Scales

### Spacing Scale (8pt Grid with 4pt Micro-steps)
- `--space-1`: 4px (tight padding, tag gaps)
- `--space-2`: 8px (icon-to-text gap, compact button padding)
- `--space-3`: 12px (form input horizontal padding)
- `--space-4`: 16px (standard card padding, element separation)
- `--space-6`: 24px (card inner padding, section rhythm)
- `--space-8`: 32px (container gap, desktop card padding)
- `--space-12`: 48px (section header gap)
- `--space-16`: 64px (major section vertical breathing room)

### Elevation & Shadow Scale
- `--shadow-sm`: `0 1px 2px 0 rgba(0, 0, 0, 0.05)` (subtle buttons, badges)
- `--shadow-md`: `0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.04)` (standard resting cards)
- `--shadow-lg`: `0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04)` (hover states, dropdown menus)
- `--shadow-modal`: `0 20px 25px -5px rgba(0, 0, 0, 0.12), 0 8px 10px -6px rgba(0, 0, 0, 0.06)` (dialog overlays)

### Border Radius Scale
- `--radius-sm`: `4px` (inner badges, checkboxes)
- `--radius-md`: `8px` (form inputs, buttons)
- `--radius-lg`: `12px` (content cards, dropdown containers)
- `--radius-xl`: `16px` (flagship showcase cards, modals)
- `--radius-full`: `9999px` (status pills, avatar frames)
*(Rule: Never apply radius > 16px to interior content cards unless explicitly creating a circular badge).*

## 3. Component Inventory & Guidelines

Every component documented in the system must define:
1. **Variants**: Primary, Secondary, Tertiary/Ghost, Destructive, Outline.
2. **Interactive States**: Default, Hover, Active, Focus-Visible, Disabled, Loading/Busy.
3. **Responsive Adaptability**: Stack vs inline behavior, touch target sizing (minimum 44 × 44 px on mobile).
4. **Accessibility Contract**: Required ARIA roles, label bindings, keyboard navigation keys (`Enter`, `Space`, `Escape`, `Arrow keys`).

## Deliverables
1. `DESIGN_SYSTEM.md`: Comprehensive design system manual.
2. `DESIGN_TOKENS.md`: Token specifications with values, roles, and usage notes.
3. `design-tokens.css`: Implementation-ready CSS custom properties for direct inclusion in the app.
4. `COMPONENT_INVENTORY.md`: Catalog of all reusable UI elements.
5. `COMPONENT_GUIDELINES.md`: Structural code snippets and interaction patterns.

## Quality Checklist
- [ ] Are all tokens defined as valid CSS variables in `design-tokens.css`?
- [ ] Are mobile touch targets at least 44x44px?
- [ ] Are all interactive states defined for every component variant?
- [ ] Do shadows use calm, tinted alpha values instead of harsh black drops?
- [ ] Can frontend developers copy component classes directly without modifying styles?

