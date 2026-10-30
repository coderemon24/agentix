---
description: "Autonomous End-to-End Multi-Agent Feature Development (Explore -> Plan -> Propose -> Parallel Workers -> PR Review -> Test Gate -> Integration -> Archive -> Git Push)"
---

# Universal Autonomous Feature Pipeline (Agentix)

Use this workflow to develop, test, refine, review, integrate, and deploy any feature or module across isolated Git worktrees with a single command or orchestrated pipeline.

---

## Workflow Steps

### Step 1: Ingest Feature Requirements & UX Discovery (Gate 1 & Gate 2)
- Receive the feature requirements from the user (from `/opsx-explore`, detailed prompt, or change specifications).
- Identify the target capability and derive a kebab-case change name (e.g., `user-profile`, `billing-checkout`, `analytics-dashboard`).
- **Gate 1 (Discovery Approval)**: Formulate `PROJECT_BRIEF.md`, `UX_RESEARCH.md`, `COMPETITOR_ANALYSIS.md`, `USER_PERSONAS.md`, `INFORMATION_ARCHITECTURE.md`.
- **Gate 2 (Visual Direction Approval)**: Formulate `DESIGN_DIRECTION.md`, `DESIGN_REFERENCES.md`, `VISUAL_MOODBOARD.md`.

### Step 2: OpenSpec Change Setup & Design Tokens (Gate 3 & Gate 4)
1. Verify OpenSpec status or initialize the change:
   ```bash
   openspec.cmd new change <change-name>
   ```
2. Populate or verify planning artifacts in `openspec/changes/<change-name>/`:
   - `proposal.md`: Context, motivation, user value.
   - `specs/<capability>/spec.md`: Delta requirements and acceptance criteria.
   - `design.md`: Technical architecture and database schema.
   - `tasks.md`: Decoupled backend and frontend task checklists.
3. **Gate 3 (Design System Approval)**: Produce `DESIGN_SYSTEM.md`, `DESIGN_TOKENS.md`, `design-tokens.css`, `COMPONENT_INVENTORY.md`, `COMPONENT_GUIDELINES.md`.
4. **Gate 4 (Wireframe Approval)**: Formulate content-first structural layouts in `WIREFRAMES.md`.
5. Check apply instructions:
   ```bash
   openspec.cmd instructions apply --change <change-name> --json
   ```

### Step 3: Establish Shared Contracts
Extract and verify shared interface contracts:
- **Routes / API Endpoints**: HTTP method, URI, named route or endpoint path.
- **Controller-to-View / Response Payloads**: Exact variable names, collections, pagination keys, DTO structures.
- **Form Payloads**: Field names, validation rules, error message keys.
- **Database Schema**: Table names, foreign key constraints, indexes.

### Step 4: Pre-flight Worktree Sync
Ensure all agent worktrees are up-to-date with `main`:
```bash
agx sync
```

### Step 5: Concurrent Worker Dispatch (Gate 5)
Launch the Backend and Frontend engineers simultaneously in their isolated worktrees:
```bash
agx run \
  -b "<Enriched Backend prompt with DB optimization & adversarial tests>" \
  -f "<Enriched Frontend prompt with design tokens, UI-Mandatory & ui-refactor.md>"
```

#### Frontend Engineer Mandatory Protocols:
- **Adopt Approved Design Tokens**: Follow `DESIGN_TOKENS.md` and `design-tokens.css`.
- **Design Consistency**: Match styling, card patterns, typography, and palette of existing app pages.
- **UI Refactoring Framework (`ui-refactor.md`)**:
  - Recipe 1 (Sharpen Message): Headline focal span with primary brand highlight.
  - Recipe 2 (Break Symmetry): Asymmetric 60/40 or 65/35 grid with floating anchor badges.
  - Recipe 3 (Build Argument): Uniform section headers and section dividers.
  - Recipe 4 (Pick the Winner): 60% flagship card dominance; quiet secondary stack.
  - Recipe 5 (Scale the Type): 4-tier scale (Headline, Card title, Body with leading-relaxed, Kicker).
  - Recipe 6 (Give Color Meaning): 60-30-10 color distribution with clear semantic hierarchy.
  - Recipe 7 (Add a Signature): Section kicker with pulsing status dot, hairline dividers, and micro-interactions.
- **UI-Mandatory Guidelines**: Zero placeholder buttons, full CRUD, responsive layouts.
- **Worktree Commit**: Staged and committed to `agent/frontend` as PR for Lead.

#### Backend Engineer Mandatory Protocols:
- **Framework Best Practices**: Follow language/framework conventions, Clean Architecture, and security audits.
- **Database Optimization (Mandatory)**:
  - **Zero N+1 Queries**: Eager-load relations (`with()`, `loadMissing()`). No lazy loading inside loops.
  - **Deadlock Prevention**: Short atomic transactions, consistent record lock order.
  - **Proper Indexing**: Add indexes for foreign keys, tenant columns, search/filter columns.
  - **Data Consistency**: Foreign key cascades/restricts and atomic counters.
- **Automated & Adversarial Testing ("Break it to make it unbreakable")**:
  - Write Unit tests and Feature/Integration tests.
  - Actively test edge cases to break the feature: invalid types, nulls, tenant boundary violations, empty records, and duplicate submissions.
  - If broken, diagnose, fix, and re-test until 100% green.
- **Worktree Commit**: Staged and committed to `agent/backend` as PR for Lead.

### Step 6: Team Lead PR Review
Inspect worker diffs against `main`:
```bash
agx review
# or: agx diff
```

### Step 7: Automated Test Gate & Edge Case Verification
Run the automated test suite:
```bash
agx test -f <FeatureName>
# or: agx t -f <FeatureName>
```

### Step 8: Automated Visual QA & Design Criticism (Gate 6)
Run Playwright browser capture and visual audit:
```bash
agx vqa -u http://127.0.0.1:8000/<route>
```
Audit rendered output against `DESIGN_TOKENS.md`, `no-slop-ui`, and responsive standards. Deliver `DESIGN_REVIEW.md` and `VISUAL_QA_REPORT.md`.

### Step 9: Iterative Feedback Loop
If any issue, broken test, N+1 query, or UI defect is detected:
1. Dispatch corrective prompt to that worker:
   ```bash
   agx dispatch -a <agent-name> -p "Fix: <details of issue>"
   # Shorthand: agx d -a <agent-name> -p "..."
   ```
2. Worker fixes the issue in its worktree, re-runs tests, and re-commits.
3. Team Lead re-reviews.

### Step 10: Integration
Merge verified worker branches into `main`:
```bash
agx integrate -f <FeatureName>
# or: agx merge -f <FeatureName>
```

### Step 11: OpenSpec Archive
Archive the completed change:
```bash
openspec.cmd archive <change-name> --yes
```

### Step 12: Auto Commit & Push to GitHub
Follow [gitcommit.md](file:///c:/laragon/www/laravel-school/gitcommit.md) standards:
```bash
agx push -m "feat(<change-name>): implement end-to-end module with verified UI and tests"
```
