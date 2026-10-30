---
name: visual-qa
description: Visual QA and automated browser audit skill. Uses Playwright to capture multi-viewport screenshots, inspect typography and spacing, verify responsive layout, and generate visual critique reports.
---

# Visual QA & Design Criticism

## Purpose
Automate and structure visual quality assurance for web interfaces. Using headless browser automation (Playwright), this skill captures multi-device screenshots, inspects typography and spacing rhythm, tests responsive reflow, and provides actionable design criticism.

## When to Use
- During Phase 4 of Orchestration (Gate 6).
- After the `frontend-engineer` has committed initial Blade views.
- Before merging frontend branches into `main` and archiving OpenSpec changes.

## Step-by-Step Workflow

### Step 1: Automated Multi-Viewport Screenshot Capture
Run the automated Playwright visual capture script:
```bash
node tests/visual-qa/capture-screenshots.js --url http://127.0.0.1:8000/<route> --output tests/visual-qa/screenshots/<feature-name>
```
Or via the Python orchestrator:
```bash
python scripts/orchestrator.py visual-qa --url http://127.0.0.1:8000/<route>
```

This captures:
1. `desktop-1440.png`: 1440 × 900 px (full-page desktop).
2. `tablet-768.png`: 768 × 1024 px (tablet portrait).
3. `mobile-375.png`: 375 × 667 px (mobile portrait).

### Step 2: Visual Inspection & Defect Detection
Inspect captured screenshots against `DESIGN_TOKENS.md` and `ui-refactor.md`:
1. **Focal Point & Hierarchy**: Does the headline focal accent span pop? Is the flagship card visibly dominant?
2. **Spacing & Alignment**: Are margins and padding multiples of 4px/8px? Are cards aligned on a clean grid line?
3. **Typography & Line Wrapping**: Does text wrap naturally? Are there awkward orphan words or broken words without hyphenation?
4. **Mobile Reflow**: Did the desktop grid collapse cleanly into a 1-column stack without horizontal overflow?
5. **Interactive States & Contrast**: Are buttons legible against card backgrounds? Are focus rings styled?

### Step 3: Anti-AI-Slop Check
Run the checklist from `anti-ai-slop-review`:
- Confirm no random floating glass cards or ambient glowing orbs.
- Confirm button styling is grounded and solid.
- Confirm all icons are crisp SVGs with matching stroke widths (1.5px or 2px).

### Step 4: Generate Actionable Visual QA Reports
Formulate specific, actionable defect feedback with exact CSS/Blade code suggestions:
- Avoid vague feedback ("Make it look cleaner").
- Provide concrete instructions: "In `routine.blade.php`, the timetable table header `.table-header` lacks horizontal padding on mobile; add `px-4 py-3 text-xs` to prevent text truncation at 375px."

## Deliverables
1. `DESIGN_REVIEW.md`: Executive design critique and visual assessment.
2. `VISUAL_QA_REPORT.md`: Granular bug and polish inventory categorized by severity (Critical, Major, Minor/Polish).
3. Multi-viewport screenshots in `tests/visual-qa/screenshots/`.

## Quality Checklist
- [ ] Screenshots captured across all 3 viewports (375px, 768px, 1440px).
- [ ] All reported issues cite specific file paths, line numbers, or CSS class selectors.
- [ ] Suggested fixes include ready-to-paste code or utility classes.
- [ ] Visual QA must pass with 0 Critical and 0 Major defects before Gate 6 approval.

