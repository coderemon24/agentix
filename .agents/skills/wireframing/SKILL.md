---
name: wireframing
description: Structural wireframing and layout architecture skill. Formulates content-first page structures, asymmetric grids, responsive layout plans, and user flow blueprints.
---

# Wireframing & Layout Architecture

## Purpose
Translate UX research and information architecture into structural, content-first wireframes before writing frontend code. Wireframing ensures that page composition, visual weight, content scannability, and responsive layout behavior are locked and approved prior to Blade implementation.

## When to Use
- In Phase 2: Wireframes & Layout Architecture (Gate 4).
- When planning a new page, modal flow, dashboard widget, or institutional portal.
- Before the `frontend-engineer` begins writing HTML or CSS.

## Step-by-Step Workflow

### Step 1: Content Inventory & Hierarchy Sorting
1. List all required content blocks for the page.
2. Rank blocks by business & user value:
   - **Primary (Tier 1)**: The essential reason the user visits (e.g., Today's Timetable, Fee Breakdown, Admission Form).
   - **Secondary (Tier 2)**: Contextual trust or supporting data (e.g., Teacher Credentials, Academic Calendar link).
   - **Tertiary (Tier 3)**: Institutional footer, legal notice, secondary links.

### Step 2: Establish Layout Grids & Composition
1. Avoid flat, repetitive symmetrical grids.
2. Apply the **Asymmetric 60/40 or 65/35 Split**:
   - Primary 8 columns (`lg:col-span-8`): Holds dominant interactive tool or rich editorial narrative.
   - Secondary 4 columns (`lg:col-span-4`): Holds summary cards, contextual actions, or live status widgets.
3. Anchor Element: Integrate an anchor badge, trust pill, or credential mark that bridges boundaries.

### Step 3: High-Fidelity ASCII / Structural Wireframes
Draft unambiguous layout schemas detailing:
- Exact container max-widths (`max-w-7xl`, `max-w-5xl`, etc.).
- Column allocations across breakpoints (`grid-cols-1 md:grid-cols-2 lg:grid-cols-12`).
- Placement of section kickers, headlines, lead paragraphs, tables, and CTA buttons.
- Responsive reflow rules (how 3-column desktop layouts stack on tablet and mobile).

## Practical Example: Asymmetric Page Wireframe
```
┌────────────────────────────────────────────────────────────────────────┐
│ [Kicker: ACADEMIC ROUTINE]                                            │
│ Class Routine & Daily Schedule <span class="accent">[Spring 2026]</span>    │
│ Official institutional timetable verified by the Academic Council.     │
├──────────────────────────────────────┬─────────────────────────────────┤
│ MAIN SCHEDULE TABLE (8 Cols / 65%)   │ ACTION & METRICS (4 Cols / 35%) │
│ ┌──────────────────────────────────┐ │ ┌─────────────────────────────┐ │
│ │ Day / Period / Subject / Room    │ │ │ Floating Next Class Badge   │ │
│ │ [Monday]                         │ │ │ "Physics Lab in 25 mins"    │ │
│ │ 09:00 - Physics (Room 302)       │ │ └─────────────────────────────┘ │
│ │ 10:15 - Mathematics (Room 104)   │ │ ┌─────────────────────────────┐ │
│ │ 11:30 - English Lit (Room 201)   │ │ │ Download PDF Schedule (CTA) │ │
│ └──────────────────────────────────┘ │ │ Print Official Timetable    │ │
│                                      │ └─────────────────────────────┘ │
└──────────────────────────────────────┴─────────────────────────────────┘
```

## Deliverables
- `WIREFRAMES.md`: Complete structural wireframe document for all target views with desktop, tablet, and mobile reflow specifications.

## Quality Checklist
- [ ] Is there a clear focal point on each screen with dominant visual weight?
- [ ] Are mobile stacking reflows explicitly detailed for each section?
- [ ] Are all buttons and links assigned specific, functional routes (no dead triggers)?
- [ ] Does the wireframe respect the 4-tier typographic scale and spacing rhythm?

