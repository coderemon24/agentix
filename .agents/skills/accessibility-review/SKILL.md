---
name: accessibility-review
description: Accessibility and inclusive design audit skill. Enforces WCAG 2.1 AA/AAA compliance, screen reader ARIA roles, keyboard navigation, and focus state visibility.
---

# Accessibility (a11y) & Usability Standards

## Purpose
Guarantee that all interfaces are usable by everyone, including people using screen readers, keyboard-only navigation, speech input, or high-contrast display modes. Meets international legal and institutional compliance standards (WCAG 2.1 AA minimum).

## When to Use
- During component guideline authoring (Gate 3).
- During Frontend Blade implementation (Gate 5).
- During Visual QA and accessibility auditing (Gate 6).

## 1. Core WCAG 2.1 AA Requirements

### Color Contrast
- Normal body and UI text: Minimum `4.5:1` contrast ratio against the background.
- Large text (>= 24px regular or >= 18.5px bold): Minimum `3.0:1` contrast ratio.
- Active UI components, borders, and functional icons: Minimum `3.0:1` contrast ratio.

### Keyboard Navigation & Focus
- Every interactive element (links, buttons, inputs, selects, tabs, modal close triggers) must be reachable via `Tab` key in logical sequence.
- **Visible Focus Indicator**: Never use `outline: none` without a high-visibility replacement.
  Use: `focus:outline-none focus:ring-2 focus:ring-[#005030] focus:ring-offset-2`.
- Modal / Dialog Trapping: When a modal opens, keyboard focus must be trapped inside until closed. Pressing `Escape` must dismiss the dialog and return focus to the trigger.

### Semantic HTML & ARIA
- Use real HTML elements instead of clickable divs: `<button type="button">` instead of `<div onclick="...">`.
- Provide text alternatives: All `<img>` tags must have descriptive `alt="..."` attributes (or `alt=""` if strictly decorative).
- Accessible form controls: Every form `<input>` must be explicitly associated with a `<label for="id">`.
- Interactive state indicators: Use `aria-expanded="true/false"` for collapsibles/accordions, `aria-current="page"` for active navigation links, and `role="alert"` for live validation error banners.

### Motion Sensitivity
- Respect the user's OS motion preferences:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
  ```

## Quality Checklist
- [ ] All clickable elements are genuine `<button>` or `<a>` tags.
- [ ] Focus rings are clearly visible on every interactive control during keyboard tab navigation.
- [ ] All inputs have associated labels and error messages linked via `aria-describedby`.
- [ ] Contrast passes 4.5:1 on all text across light/dark surfaces.
- [ ] `prefers-reduced-motion` is implemented to disable bouncy animations.

