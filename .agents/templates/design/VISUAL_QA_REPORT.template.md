# Visual QA Audit Report: [Page / Route Name]

> **Gate**: Gate 6 — Visual QA Approval  
> **Test Suite**: Playwright Multi-Viewport Headless Audit  
> **Date**: [YYYY-MM-DD]  
> **Viewports Tested**: Mobile (375px), Tablet (768px), Desktop (1440px)  

---

## 1. Multi-Viewport Screenshot Inventory
- `desktop-1440.png`: `tests/visual-qa/screenshots/[feature]/desktop-1440.png`
- `tablet-768.png`: `tests/visual-qa/screenshots/[feature]/tablet-768.png`
- `mobile-375.png`: `tests/visual-qa/screenshots/[feature]/mobile-375.png`

---

## 2. Defects & Polish Items Matrix

| Issue ID | Severity | Viewport | Element / File | Defect Description | Required Actionable Fix |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **VQA-01** | Minor | Mobile (375px) | `.table-action-btn` | Touch target is 36px; violates 44px minimum. | Add `py-2.5 px-4 min-h-[44px]` to button class. |
| **VQA-02** | Polish | Desktop (1440px) | `.kicker-dot` | Pulsing animation does not respect `prefers-reduced-motion`. | Wrap `@keyframes pulse` in `@media (prefers-reduced-motion: no-preference)`. |
| **VQA-03** | Minor | All | Card body | Text color `#94a3b8` has 3.8:1 contrast on white. | Change text color to `#64748b` (4.6:1 contrast ratio, WCAG AA compliant). |

---

## 3. Approval Gate Decision
- [ ] **Gate 6 Approved**: All Critical and Major visual defects resolved.
- [ ] **Gate 6 Blocked**: Corrective prompt dispatched to `frontend-engineer`.

