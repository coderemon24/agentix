# Agentix (`agx`)

<p align="center">
  <strong>Universal Multi-Agent Engineering & Staged AI Design System Architecture</strong><br>
  <em>Coordinates specialized AI workers across isolated Git worktrees with zero file collisions and automated Playwright visual testing.</em>
</p>

<p align="center">
  <a href="#quick-start"><img src="https://img.shields.io/badge/CLI-agx-blue.svg?style=flat-square" alt="CLI agx" /></a>
  <a href="#compatibility"><img src="https://img.shields.io/badge/AI%20Tools-Claude%20%7C%20Cursor%20%7C%20Antigravity%20%7C%20Copilot%20%7C%20Windsurf-brightgreen.svg?style=flat-square" alt="AI Compatibility" /></a>
  <a href="#visual-qa"><img src="https://img.shields.io/badge/Visual%20QA-Playwright-orange.svg?style=flat-square" alt="Playwright" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-purple.svg?style=flat-square" alt="License MIT" /></a>
</p>

---

## 💡 Why Agentix?

When building modern web applications with AI assistants, asking a single agent to write backend databases and frontend UI simultaneously leads to **merge conflicts, broken layouts, and generic AI template slop**.

**Agentix** solves this by operating as a multi-agent engineering team:
1. **Isolated Git Worktrees**: Workers build simultaneously in dedicated branches (`agent/backend`, `agent/frontend`). **Zero file collisions.**
2. **6 Staged Design Gates**: Takes projects from UX Discovery → Visual Direction → Design Tokens → Wireframes → Code → Visual QA.
3. **Playwright Visual Testing**: Headless browser captures Mobile (375px), Tablet (768px), and Desktop (1440px) to audit real rendered interfaces.
4. **Anti-AI-Slop Review**: Banishes generic purple/cyan gradients, floating glassmorphism, and sparkle icons in favor of high-craft editorial design.
5. **Universal Compatibility**: Works out-of-the-box with **Claude Code**, **Cursor**, **Google Antigravity**, **GitHub Copilot**, **Windsurf**, and **Aider**.

---

## ⚡ 1-Minute Quick Start

### Option A: One-Line Install (Recommended)

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/coderemon24/agentix/main/install.ps1 | iex
```

**Linux / macOS / Git Bash:**
```bash
curl -fsSL https://raw.githubusercontent.com/coderemon24/agentix/main/install.sh | bash
```

### Option B: Clone into Any Project
```bash
# In your existing project root
git clone https://github.com/coderemon24/agentix.git .agentix-temp
cp -r .agentix-temp/.agents .agentix-temp/scripts .agentix-temp/tests .
cp .agentix-temp/agx* .agentix-temp/AGENTS.md .agentix-temp/USER_MANUAL.md .agentix-temp/CLAUDE.md .agentix-temp/.cursorrules .
rm -rf .agentix-temp

# Initialize worktrees & branches
agx init
```

---

## 🛠️ Fast Command Cheat Sheet (`agx` vs `opsx`)

Agentix commands are short, developer-friendly, and support 1-letter aliases:

| Command | Shorthand | What It Does |
| :--- | :--- | :--- |
| `agx init` | — | Automatically creates Git branches and worktrees in 3 seconds. |
| `agx status` | **`agx st`** | Inspects all worktrees, active branches, and git changes. |
| `agx sync` | — | Merges latest `main` into all agent worktree branches. |
| `agx run-parallel -b "..." -f "..."` | **`agx run -b "..." -f "..."`** | Launches Backend and Frontend engineers concurrently in isolated worktrees. |
| `agx review` | **`agx diff`** | Shows exact git diffs of `agent/backend` and `agent/frontend` against `main`. |
| `agx test -f <filter>` | **`agx t -f <filter>`** | Executes automated test suite with optional filter. |
| `agx visual-qa -u <URL>` | **`agx vqa -u <URL>`** | Launches Playwright and captures 375px, 768px, 1440px screenshots. |
| `agx integrate -f <filter>` | **`agx merge -f <filter>`** | Merges verified worker branches into `main` after test gates pass. |
| `agx push -m "<message>"` | **`agx p -m "<msg>"`** | Formulates Conventional Commit and pushes to `origin main`. |
| `agx pipeline -c <name> -p "..."` | **`agx auto -c <name> -p "..."`** | **Single-Command Super Flow**: sync → code → review → test → vqa → merge → push. |
| `agx dispatch -a <agent> -p "..."` | **`agx d -a <agent> -p "..."`** | Sends targeted prompt or fix to a specific worker. |

---

## 🏗️ Multi-Agent Architecture & Strict Boundaries

```
                             ┌───────────────────────────────┐
                             │    Team Lead (Main Worktree)  │
                             │   Orchestrator & Gatekeeper   │
                             └───────────────┬───────────────┘
                                             │
               ┌─────────────────────────────┼─────────────────────────────┐
               │                             │                             │
               ▼                             ▼                             ▼
  ┌──────────────────────────┐  ┌──────────────────────────┐  ┌──────────────────────────┐
  │     Design Engineer      │  │     Backend Engineer     │  │    Frontend Engineer     │
  │ UX Discovery, Tokens,    │  │ Endpoints, DB Opt,       │  │ Components, Views, CSS,  │
  │ Wireframes, Direction    │  │ Adversarial Tests        │  │ 7 Master UI Recipes      │
  │ (Root Workspace)         │  │ (../<project>-backend)   │  │ (../<project>-frontend)  │
  └────────────┬─────────────┘  └────────────┬─────────────┘  └────────────┬─────────────┘
               │                             │                             │
               │ Design Specs & Tokens       │ API Endpoints & Logic       │ Rendered Markup & Styles
               └─────────────────────────────┼─────────────────────────────┘
                                             │
                                             ▼
                                ┌──────────────────────────┐
                                │   Visual QA Specialist   │
                                │ Playwright Multi-Device  │
                                │ Screenshot & Slop Audit  │
                                └────────────┬─────────────┘
                                             │
                                             ▼
                                ┌──────────────────────────┐
                                │   Team Lead Integration  │
                                │ Merge, Archive, Git Push │
                                └──────────────────────────┘
```

| Agent | Worktree Path | Branch | File Ownership | Prohibited Edits |
| :--- | :--- | :--- | :--- | :--- |
| **`team-lead`** | Root & Lead worktree | `main` | OpenSpec specs, contracts, gates | Never writes code directly without PR review. |
| **`design-engineer`** | Root workspace | `main` | `.agents/templates/`, tokens, wireframes | Never touches backend server code or DB migrations. |
| **`backend-engineer`** | `../<project>-backend` | `agent/backend` | `app/`, `database/`, `routes/`, `tests/` | Never touches frontend views, HTML, or CSS. |
| **`frontend-engineer`** | `../<project>-frontend` | `agent/frontend` | `resources/views/`, `public/assets/` | Never touches backend models, DB, or routes. |
| **`visual-qa`** | Root workspace | `main` | `tests/visual-qa/`, screenshots, reports | Never touches application business logic. |

---

## 🚦 The 6 Staged Approval Gates

1. **Gate 1: Discovery Approval** — `PROJECT_BRIEF.md`, `UX_RESEARCH.md`, `USER_PERSONAS.md`, `INFORMATION_ARCHITECTURE.md`.
2. **Gate 2: Visual Direction Approval** — `DESIGN_DIRECTION.md`, `DESIGN_REFERENCES.md`, `VISUAL_MOODBOARD.md`.
3. **Gate 3: Design System Approval** — `DESIGN_SYSTEM.md`, `DESIGN_TOKENS.md`, `design-tokens.css`, `COMPONENT_GUIDELINES.md`.
4. **Gate 4: Wireframe Approval** — `WIREFRAMES.md` (Asymmetric 60/40 layouts & mobile reflow).
5. **Gate 5: Implementation Review** — Backend PR (Zero N+1, tests) & Frontend PR (7 UI recipes, responsive reflow).
6. **Gate 6: Visual QA Approval** — Multi-viewport screenshots (375/768/1440px), `DESIGN_REVIEW.md`, `VISUAL_QA_REPORT.md`.

---

## 🤖 Universal Compatibility with All AI Tools

Agentix includes native configuration files for all popular AI tools:

- **Claude Code**: Native `CLAUDE.md` with operating commands and worktree protocols.
- **Cursor IDE**: `.cursorrules` and `.cursor/rules/agentix.mdc` for agent awareness.
- **Google Antigravity**: `.agents/agents/` and `.agents/skills/` integration.
- **Windsurf IDE**: `.windsurfrules` configuration.
- **GitHub Copilot**: `.github/copilot-instructions.md`.
- **Aider / Codex / OpenSpec**: `CONVENTIONS.md` and OpenSpec delta integration.

---

## 📄 License & Community

Created by [coderemon24](https://github.com/coderemon24). Released under the [MIT License](LICENSE).

