# Agentix Engineering & Architecture Conventions

## 1. Operating Model
- Multi-agent Git worktree architecture managed via the `agx` CLI tool.
- Zero file collisions: backend agents work in `agent/backend`, frontend agents work in `agent/frontend`, lead integration in `main`.

## 2. Command Reference
- `agx init`: Setup worktrees & branches.
- `agx st`: Check status.
- `agx run -b "<backend prompt>" -f "<frontend prompt>"`: Parallel execution.
- `agx diff`: Review PR diffs.
- `agx vqa -u <URL>`: Playwright visual audit across 375px, 768px, 1440px.
- `agx merge -f <Filter>`: Integrate into main.
- `agx p -m "<Message>"`: Push to GitHub.

## 3. Staged Approval Gates
- Gate 1: Discovery (`PROJECT_BRIEF.md`, `UX_RESEARCH.md`, `USER_PERSONAS.md`)
- Gate 2: Visual Direction (`DESIGN_DIRECTION.md`, `DESIGN_REFERENCES.md`, `VISUAL_MOODBOARD.md`)
- Gate 3: Design Tokens & System (`DESIGN_SYSTEM.md`, `DESIGN_TOKENS.md`, `design-tokens.css`)
- Gate 4: Wireframes (`WIREFRAMES.md` with 60/40 asymmetry)
- Gate 5: Parallel Worker PRs
- Gate 6: Playwright Visual QA (`DESIGN_REVIEW.md`, `VISUAL_QA_REPORT.md`)

