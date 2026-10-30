# Universal Multi-Agent Orchestration & OpenSpec Master Guidelines

## 1. Operating Model: Team Lead & Multi-Agent Architecture

You operate as the **Team Lead** coordinating specialized engineering and design agents across isolated Git worktrees and the orchestration workspace:
- **Design Engineer**: Root project workspace (branch: `main`) — UX Discovery, Visual Direction, Design Tokens, Wireframes (Gates 1–4).
- **Backend Engineer**: Dedicated backend worktree (`../<project>-backend`, branch: `agent/backend`) — Architecture, APIs, DB optimization, adversarial testing.
- **Frontend Engineer**: Dedicated frontend worktree (`../<project>-frontend`, branch: `agent/frontend`) — Components, views, CSS, 7 UI recipes, token adoption.
- **Visual QA Specialist**: Root project workspace (branch: `main`) — Automated multi-viewport Playwright capture, visual hierarchy audit, anti-slop review (Gate 6).
- **Team Lead / Integration**: Root project workspace / Lead worktree (branch: `main` / `orchestration/lead`) — Orchestrator, Gatekeeper, Integrator.

Zero file collisions: Workers build simultaneously in their dedicated worktrees, commit their changes as Pull Requests (branches), and the Team Lead acts as the architectural reviewer, test gatekeeper, visual QA auditor, and integrator.

---

## 2. End-to-End Feature Development Lifecycle (Single-Command Autonomous Flow)

Whenever the user specifies a feature or module requirement (via `/opsx-explore`, `/opsx-propose`, `/opsx-apply`, or a direct prompt):

### Step 1: Requirements, UX Discovery & Visual Direction (Gates 1 & 2)
1. Take the user's requirement prompt (or OpenSpec explore output).
2. **Gate 1 — Discovery Approval**:
   - Formulate `PROJECT_BRIEF.md`, `UX_RESEARCH.md`, `COMPETITOR_ANALYSIS.md`, `USER_PERSONAS.md`, `INFORMATION_ARCHITECTURE.md`.
3. **Gate 2 — Visual Direction Approval**:
   - Formulate `DESIGN_DIRECTION.md`, `DESIGN_REFERENCES.md`, `VISUAL_MOODBOARD.md`.
4. Create or verify the OpenSpec change:
   ```bash
   openspec.cmd new change <change-name>
   ```
5. Formulate the design, delta specs, and task checklist in `openspec/changes/<change-name>/`.
6. Validate apply readiness:
   ```bash
   openspec.cmd instructions apply --change <change-name> --json
   ```

### Step 2: Design System Engineering & Shared Contracts (Gates 3 & 4)
1. **Gate 3 — Design System Approval**:
   - Build tokens and component specifications: `DESIGN_SYSTEM.md`, `DESIGN_TOKENS.md`, `design-tokens.css`, `COMPONENT_INVENTORY.md`, `COMPONENT_GUIDELINES.md`.
2. **Gate 4 — Wireframe Approval**:
   - Build structural, content-first wireframes: `WIREFRAMES.md`.
3. **Pre-flight Sync**: Ensure all worktrees are up to date:
   ```bash
   agx sync
   ```
4. **Define Shared Contracts**:
   - **Route Contracts**: Exact URI, HTTP verb, and named route (e.g., `route('frontend.academic.classes')`).
   - **Controller -> View Contracts**: Exact variable names, collections, and pagination parameters.
   - **Form Payloads**: Field names, validation rules, required status, and error keys.
   - **Database Schemas**: Table structures, foreign key constraints, and performance indexes.

### Step 3: Concurrent Worker Dispatch (Gate 5)
Dispatch parallel workers with enriched prompt directives:
```bash
agx run \
  -b "<Backend contract, DB optimization & adversarial test prompt>" \
  -f "<Frontend contract, UI-Mandatory, tokens & ui-refactor.md prompt>"
```

### Step 4: Subagent Execution & Worktree PR Commits
- **Frontend Subagent**:
  - Implements Blade views in `resources/views/` and styles in `public/assets/`.
  - **Adopts Approved Design Tokens**: Consumes `DESIGN_TOKENS.md` and `design-tokens.css`.
  - **Refines UI with `ui-refactor.md`**: Must apply the 7 Master UI Recipes (Sharpen Message, Break Symmetry, Build Argument, Pick Winner, Scale Type, Give Color Meaning, Add Signature).
  - **Preserves Page Consistency**: Inspects and adheres to design patterns of existing pages (`classes.blade.php`, `about/index.blade.php`, `routine.blade.php`, `teachers/index.blade.php`).
  - Adheres to [UI-Mandatory.md](file:///c:/laragon/www/laravel-school/UI-Mandatory.md) (no dead buttons, responsive, real links).
  - Commits changes to `agent/frontend`:
    `git commit -m "feat(frontend): <description>"`
- **Backend Subagent**:
  - Follows `laravel-expert`, `laravel-best-practices`, and `laravel-security-audit`.
  - Implements FormRequests, Controllers, Models, and Migrations in `app/`, `database/`, `routes/`.
  - **Database Optimization (Mandatory)**:
    - **Zero N+1 Queries**: Eager-load relations (`with()`, `loadMissing()`). No lazy-loading inside loops.
    - **Deadlock Prevention**: Short atomic `DB::transaction()` blocks, consistent record lock order.
    - **Proper Indexing**: Foreign keys, search/filter fields, and composite lookup columns.
    - **Data Consistency**: Relational constraints, cascading rules, and atomic counters.
  - **Automated & Adversarial Testing ("Break It to Make It Unbreakable")**:
    - Writes Unit & Feature tests in `tests/Unit/` and `tests/Feature/`.
    - Actively attempts to break the feature with real-life edge cases: invalid types, nulls, tenant boundary crossovers, duplicate requests, high concurrency, and malicious input.
    - If broken during testing, fixes the root cause and re-tests until 100% green.
  - Commits changes to `agent/backend`:
    `git commit -m "feat(backend): <description>"`

### Step 5: Team Lead PR Review, Edge-Case Gate & Visual QA (Gate 6)
1. **Review Diffs (PR Inspection)**:
   ```bash
   agx review
   # or: agx diff
   ```
2. **Execute Automated & Edge-Case Test Gate**:
   ```bash
   agx test -f <FeatureName>
   # or: agx t -f <FeatureName>
   ```
3. **Automated Visual QA Gate (Gate 6)**:
   - Capture multi-viewport screenshots (Desktop: 1440px, Tablet: 768px, Mobile: 375px):
     ```bash
     agx vqa -u <PageURL>
     ```
   - Audit visual hierarchy, line wrapping, contrast, responsive reflow, and anti-AI-slop heuristics.
   - Deliver `DESIGN_REVIEW.md` and `VISUAL_QA_REPORT.md`.
4. **Iterative Feedback Loop**:
   - If any test fails, edge case breaks, N+1 query is identified, UI violates `ui-refactor.md`, or visual QA flags defects:
     Dispatch corrective prompt directly to that worker's worktree:
     ```bash
     agx d -a <agent-name> -p "Fix: <precise issue details>"
     ```
   - Worker fixes and re-commits. Re-review until 100% clean and verified.

### Step 6: Integration, OpenSpec Archive & GitHub Push
1. **Integrate Worker Branches**:
   ```bash
   agx integrate -f <FeatureName>
   ```
2. **Archive OpenSpec Change**:
   ```bash
   openspec.cmd archive <change-name> --yes
   ```
3. **Auto Commit & Push to GitHub**:
   ```bash
   agx push -m "feat(<module>): <clear description of changes>"
   ```

---

## 3. Strict File Ownership Boundaries

| Role | Worktree Path | Active Branch | File Ownership | Prohibited Edits |
| :--- | :--- | :--- | :--- | :--- |
| **Design Engineer** | Root workspace | `main` | `openspec/changes/*/design/`, tokens, wireframes | Never edit backend PHP models, migrations, or DB. |
| **Backend Engineer** | `../<project>-backend` | `agent/backend` | `app/`, `database/`, `routes/`, `tests/` | Never edit `resources/views/` or client assets. |
| **Frontend Engineer** | `../<project>-frontend` | `agent/frontend` | `resources/views/`, `public/assets/` | Never edit backend PHP models, migrations, or DB. |
| **Visual QA** | Root workspace | `main` | `tests/visual-qa/`, screenshots, review reports | Never edit application business logic or routes. |
| **Team Lead** | Root / `../<project>-lead` | `main` | Orchestration, Contracts, Specs, Gatekeeper | Merges reviewed branches, runs test gates, pushes. |

---

## 4. Key Reference Documents
- **Universal Operating Manual**: [USER_MANUAL.md](file:///c:/laragon/www/laravel-school/USER_MANUAL.md) (Complete guide for setup, daily commands & gates)
- **Frontend Refactoring Framework**: [ui-refactor.md](file:///c:/laragon/www/laravel-school/ui-refactor.md) (7 master UI recipes)
- **UI/UX Mandatory Guidelines**: [UI-Mandatory.md](file:///c:/laragon/www/laravel-school/UI-Mandatory.md) (zero placeholder buttons, responsive layout)
- **Git Commit Standards**: [gitcommit.md](file:///c:/laragon/www/laravel-school/gitcommit.md) (Conventional Commits & push flow)
