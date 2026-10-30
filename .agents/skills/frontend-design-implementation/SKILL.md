---
name: frontend-design-implementation
description: Design-to-code translation skill. Guides frontend engineers in translating approved wireframes, design tokens, and component guidelines into production Laravel Blade and Tailwind/CSS code.
---

# Frontend Design Implementation

## Purpose
Guide frontend engineers in translating approved design tokens, component guidelines, and wireframes into clean, accessible, production-grade Laravel Blade templates, Tailwind CSS utilities, and Vanilla CSS components.

## When to Use
- During Phase 3: Concurrent Worker Dispatch (Gate 5).
- Whenever writing or updating Blade views (`resources/views/`) and assets (`public/assets/`).

## Step-by-Step Workflow

### Step 1: Ingest Approved Design Specs & Tokens
Before writing any HTML:
1. Read `DESIGN_TOKENS.md` and `design-tokens.css` for the current module or feature.
2. Read `WIREFRAMES.md` and `COMPONENT_GUIDELINES.md`.
3. Check existing production reference views:
   - `resources/views/frontend/academic/classes.blade.php`
   - `resources/views/frontend/about/index.blade.php`
   - `resources/views/frontend/academic/routine.blade.php`
   - `resources/views/frontend/teachers/index.blade.php`
4. Confirm color constants:
   - Institutional Green: `#005030` / `#004027`
   - Primary CTA: `amber-400` / `#f59e0b`
   - Notice/Bulletin: `sky-600` / `#0284c7`
   - Base Border: `border-slate-200/90`

### Step 2: Implement Semantic HTML & Layout Structure
1. Build the asymmetric layout specified in the wireframe:
   `<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">`.
2. Allocate columns according to the 60/40 or 65/35 split.
3. Ensure every image has width/height attributes or aspect-ratio classes (`aspect-video`, `aspect-square`) to prevent layout shifts (CLS).

### Step 3: Apply the 7 Master UI Recipes (`ui-refactor.md`)
1. **Sharpen the Message**: One focal accent span `<span class="text-[#005030] font-bold">`.
2. **Break the Symmetry**: Asymmetric editorial layout with floating anchor badge.
3. **Build the Argument**: Uniform `.section-header-block` and `.home-section-divider`.
4. **Pick the Winner**: Flagship card elevated with 60% visual weight.
5. **Scale the Type**: Enforce 4-tier typographic scale.
6. **Give Color Meaning**: Respect semantic color roles.
7. **Add a Signature**: Pulsing section kicker dot (`.section-kicker-dot`).

### Step 4: Validate UI-Mandatory Rules
- Zero placeholder buttons: all buttons must trigger real actions or valid routes.
- Full responsive reflow down to 375px without horizontal scroll.
- Visible keyboard focus rings on all interactive elements.

## Quality Checklist
- [ ] Views consume CSS variables from `design-tokens.css` or matching Tailwind tokens.
- [ ] 7 Master UI Recipes applied and verified.
- [ ] No dead buttons or `#` placeholder links.
- [ ] Mobile responsive layout tested and verified without horizontal scroll.
- [ ] Ready for Visual QA screenshot capture and audit.

