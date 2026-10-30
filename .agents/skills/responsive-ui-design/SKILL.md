---
name: responsive-ui-design
description: Mobile-first and multi-device responsive design skill. Enforces fluid grids, container breakpoints, touch ergonomics, and zero horizontal scrolling.
---

# Responsive UI Design & Multi-Device Ergonomics

## Purpose
Ensure all interfaces function flawlessly across smartphones, tablets, laptops, and ultra-wide desktop monitors. Eliminates broken layouts, accidental text clipping, touch target frustration, and horizontal scrollbars.

## When to Use
- During layout wireframing and frontend Blade implementation (Gates 4 & 5).
- When conducting visual QA across mobile (375px), tablet (768px), and desktop (1440px).

## 1. Breakpoint System
- **Mobile (`< 640px`)**: Single column vertical flow (`grid-cols-1`). Full-width inputs, touch targets >= 44px, sticky bottom action bar where appropriate.
- **Tablet (`640px – 1023px`)**: 2-column balanced grid (`md:grid-cols-2`). Collapsible filters into bottom drawers or slide-overs.
- **Desktop (`1024px – 1439px`)**: Asymmetric editorial layout (`lg:grid-cols-12`). Full sidebars, multi-column tables with fixed headers.
- **Widescreen (`>= 1440px`)**: Centered container constraint (`max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`). Content never stretches into unreadable ultra-wide bands.

## 2. Responsive Rules of Thumb
1. **Zero Horizontal Overflow**:
   - Never allow root or container horizontal scrollbars.
   - Use `overflow-x-auto` strictly inside dedicated data table wrappers:
     `<div class="w-full overflow-x-auto border border-slate-200 rounded-lg"><table>...</table></div>`.
2. **Fluid Typography & Spacing**:
   - Use responsive utility modifiers: `text-2xl sm:text-3xl lg:text-5xl` for primary headlines.
   - Scale padding proportionally: `p-4 sm:p-6 lg:p-8` for container cards.
3. **Touch Target Ergonomics**:
   - All interactive controls on mobile must measure at least `44 × 44 px` with adequate finger spacing (`gap-3` minimum).
   - Ensure dropdown selects and date pickers use native mobile pickers (`<input type="date">`, `<select>`) on mobile viewports for optimal OS ergonomics.

## Quality Checklist
- [ ] Tested and verified at 375px (iPhone SE), 768px (iPad Mini), and 1440px (Desktop).
- [ ] No horizontal scrolling on the root page across any viewport.
- [ ] Tables are wrapped in scrollable containers with clear visual swipe affordance.
- [ ] Form submit buttons are easily reachable with one thumb on mobile.
- [ ] Navigation menus collapse into a clean, keyboard-accessible mobile drawer.

