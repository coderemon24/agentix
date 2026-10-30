# Agentix (agx) — Multi-Agent Engineering & Design System

You are operating within a project governed by **Agentix** (`agx`).

## Core Architecture
Agentix coordinates 5 specialized AI agents working concurrently across isolated Git worktrees with zero file collisions:
- **`team-lead`**: Main repo / Lead worktree (`main` / `orchestration/lead`). Orchestration, OpenSpec specs, contracts, review, test gates, merge.
- **`design-engineer`**: Main repo (`main`). UX Discovery, Visual Direction, Design Tokens, and Wireframing (Gates 1–4).
- **`backend-engineer`**: Dedicated backend worktree (`../<project>-backend`, branch: `agent/backend`). Architecture, APIs, DB optimization (zero N+1, proper indexing), adversarial testing. Never touches frontend views.
- **`frontend-engineer`**: Dedicated frontend worktree (`../<project>-frontend`, branch: `agent/frontend`). Blade/HTML, Tailwind CSS, 7 Master UI Recipes (`ui-refactor.md`), token adoption. Never touches backend models or DB.
- **`visual-qa`**: Main repo (`main`). Playwright multi-device screenshots (Mobile 375px, Tablet 768px, Desktop 1440px), visual hierarchy audit, anti-AI-slop heuristics (Gate 6).

## The CLI (`agx`)
Always use the `agx` command line:
- `agx st` or `agx status`: Check agent worktree & branch statuses.
- `agx sync`: Synchronize all worktrees with `main`.
- `agx run -b "<backend>" -f "<frontend>"`: Dispatch parallel workers in isolated worktrees.
- `agx diff` or `agx review`: Inspect worker PR branch diffs against `main`.
- `agx t -f <filter>`: Run automated test suite with filter.
- `agx vqa -u <url>`: Launch Playwright headless browser and capture 375px, 768px, 1440px screenshots.
- `agx merge -f <filter>`: Merge verified branches into `main` after green tests.
- `agx p -m "<commit message>"`: Stage and push to GitHub following Conventional Commits.
- `agx auto -c <change> -p "<prompt>"`: Autonomous single-command pipeline.
- `agx d -a <agent> -p "<prompt>"`: Targeted fix dispatch.

## Staged Approval Gates
1. **Gate 1**: Discovery Approval (`PROJECT_BRIEF.md`, `UX_RESEARCH.md`, `USER_PERSONAS.md`, `INFORMATION_ARCHITECTURE.md`).
2. **Gate 2**: Visual Direction Approval (`DESIGN_DIRECTION.md`, `DESIGN_REFERENCES.md`, `VISUAL_MOODBOARD.md`).
3. **Gate 3**: Design System Approval (`DESIGN_SYSTEM.md`, `DESIGN_TOKENS.md`, `design-tokens.css`, `COMPONENT_GUIDELINES.md`).
4. **Gate 4**: Wireframe Approval (`WIREFRAMES.md` with 60/40 asymmetry and mobile reflow).
5. **Gate 5**: Implementation Review (Backend & Frontend PRs in their respective worktrees).
6. **Gate 6**: Visual QA Approval (Playwright multi-viewport audit, `DESIGN_REVIEW.md`, `VISUAL_QA_REPORT.md`).

## Anti-AI-Slop Rules
Strictly prohibit generic AI clichés:
- No cliché purple/cyan or rainbow gradients.
- No floating glassmorphism cards with heavy blur and glowing borders.
- No meaningless `✨` sparkle emojis.
- No repetitive bento grids lacking functional hierarchy.
- No placeholder buttons or dead links.
- No mobile horizontal scrolling at 375px.

