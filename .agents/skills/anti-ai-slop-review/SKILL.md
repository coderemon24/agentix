---
name: anti-ai-slop-review
description: Heuristic design criticism skill to identify, challenge, and eliminate generic AI aesthetic tropes, cookie-cutter templates, and empty decorative filler.
---

# Anti-AI-Slop Design Criticism & Review

## Purpose
Challenge and eliminate generic, algorithmic AI aesthetic clichés from frontend interfaces. Transform lazy, default-generated UI into bespoke, human-crafted, authoritative digital experiences with real product personality.

## When to Use
- When conducting Visual QA & Design Review (Gate 6).
- When critiquing proposed wireframes or initial Blade views before PR merge.
- When an interface feels like an AI template rather than a custom client product.

## 1. The 10 AI Slop Red Flags (The Banned Clichés)

| Red Flag | AI Slop Symptom | Human-Crafted Solution |
| :--- | :--- | :--- |
| **1. Cliché Gradients** | Purple-to-blue, magenta, or neon cyan gradients on text headings or card borders. | Single authoritative brand color, deep institutional neutrals, or intentional single-accent highlights. |
| **2. Floating Glassmorphism** | Translucent cards with `backdrop-filter: blur(20px)` and glowing white borders. | Crisp, solid card surfaces (`bg-white` or `bg-slate-50`) with disciplined hairline borders (`border-slate-200/90`). |
| **3. Fake Stats & Marketing Fluff** | "99.9% Excellence", "10,000+ Happy Humans", generic stock corporate claims. | Grounded, domain-specific metrics verified by real client data or honest editorial copy. |
| **4. Bento Grid Overload** | Chopping every section into 8 tiny identical rounded tiles regardless of content logic. | Asymmetric editorial layouts (60/40 or 65/35) reflecting genuine content hierarchy. |
| **5. Meaningless Sparkle Badges** | Placing `✨` or sparkle SVG icons next to headings to denote "smart" features. | High-utility badges with precise semantic descriptions (e.g., "Verified Curriculum", "New Syllabus"). |
| **6. Hyper-Rounded Corners** | `rounded-3xl` (24–32px) on inner cards, inputs, and small badges. | Disciplined radius scale: 4px for badges, 8px for inputs/buttons, 12–16px for outer cards. |
| **7. Cookie-Cutter Centered Hero** | Centered small kicker, huge centered text, centered subtext, centered dual buttons. | Asymmetric layout: left-aligned promise with focal accent span, paired with a dominant right-side proof artifact. |
| **8. Arbitrary Eyebrow Labels** | Tiny uppercase text with 0.2em letter spacing above every heading (`OVERVIEW // 01`). | Meaningful editorial kicker that actively clarifies the section category. |
| **9. Ambient Glows & Neon Orbs** | Blurry circular radial gradients floating randomly behind card corners. | Intentional whitespace and clean contrast between foreground cards and background canvas. |
| **10. Decorative Stock Icons** | Random 3D clay icons or misaligned line icons floating with zero context. | High-utility, consistent icon set (Lucide/Heroicons) sized at 16–20px inline with text. |

## 2. The Heuristic Criticism Process
When reviewing a rendered screen, ask these 4 diagnostic questions:
1. **The Swap Test**: If we changed the logo and color to a cryptocurrency or SaaS tool, would this page look identical? If yes, it is slop. Inject domain-specific institutional elements.
2. **The Flagship Test**: Is there one clear dominant element that captures 60% of the visual attention, or are 6 cards screaming with equal weight?
3. **The Utility Test**: Does every button, pill, and tag perform a real job, or is it decorative filler?
4. **The Craft Test**: Are line heights, typographic scales, and micro-spacings intentional down to the pixel?

## Deliverables
- Line-referenced criticism documented in `DESIGN_REVIEW.md`.

## Quality Checklist
- [ ] Zero gratuitous purple-cyan gradients.
- [ ] No fake sparkle icons or decorative glowing dots.
- [ ] No repetitive bento grids lacking content justification.
- [ ] All typography uses intentional weights, line-heights, and font pairings.

