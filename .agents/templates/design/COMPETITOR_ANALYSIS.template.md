# Competitor & Market Analysis: [Feature / Industry Domain]

> **Gate**: Gate 1 — Discovery Approval  
> **Prepared by**: [design-engineer]  

---

## 1. Competitive Landscape Matrix

| Competitor / Benchmark | Primary Strength | Critical UX Flaw / Weakness | Lessons for EduCore |
| :--- | :--- | :--- | :--- |
| **Competitor A (Direct)** | Comprehensive reporting suite | Clunky multi-level modal popups; non-responsive mobile tables | Use inline drawers and horizontal-scroll table containers |
| **Competitor B (Direct)** | Clean visual aesthetic | Low contrast gray text (2.1:1 ratio); slow server-side page reloads | Enforce WCAG AA (4.5:1 min) and snappy client interactions |
| **Benchmark C (Analogous)** | Flawless keyboard shortcuts and zero-latency filtering | High learning curve for non-technical users | Provide intuitive visual UI with optional power-user shortcuts |

---

## 2. Industry Conventions to Respect (Jakob's Law)
- Primary navigation along top or fixed left sidebar.
- User profile and school switcher in the top-right header corner.
- Status filters placed directly above data tables.
- Primary conversion / submission button placed at bottom-right of form cards.

---

## 3. Differentiation Opportunities for EduCore
1. **Editorial Clarity**: Replace bland template cards with high-contrast, authoritative typography.
2. **Instant Accessibility**: Guaranteed zero horizontal page scroll and full touch target ergonomics (>= 44px).
3. **Optimistic States**: Immediate visual feedback on state changes with graceful error fallback.

