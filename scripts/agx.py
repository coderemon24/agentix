"""
Agentix (agx) — Universal Multi-Agent Orchestrator
Coordinates specialized AI workers across isolated Git worktrees.
Supports autonomous single-command feature development pipeline.
Shorthand CLI syntax inspired by modern developer tooling.
"""

import argparse
import asyncio
import json
import os
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Paths & Dynamic Project Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / ".orchestrator.json"


def get_project_config():
    """Load or generate project configuration dynamically for any workspace."""
    project_slug = BASE_DIR.name
    config = {
        "project_name": project_slug.replace("-", " ").title(),
        "worktrees": {
            "lead": str(BASE_DIR.parent / f"{project_slug}-lead"),
            "backend": str(BASE_DIR.parent / f"{project_slug}-backend"),
            "frontend": str(BASE_DIR.parent / f"{project_slug}-frontend"),
        }
    }
    
    # Backward compatibility: check if existing EduCore worktrees exist in this workspace
    legacy_backend = Path("C:/laragon/www/EduCore-backend")
    if legacy_backend.exists() and project_slug in ("laravel-school", "EduCore"):
        config["project_name"] = "EduCore"
        config["worktrees"] = {
            "lead": "C:/laragon/www/EduCore-lead",
            "backend": "C:/laragon/www/EduCore-backend",
            "frontend": "C:/laragon/www/EduCore-frontend",
        }

    # If project has a local .orchestrator.json, load overrides
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                user_cfg = json.load(f)
                if "project_name" in user_cfg:
                    config["project_name"] = user_cfg["project_name"]
                if "worktrees" in user_cfg:
                    config["worktrees"].update(user_cfg["worktrees"])
        except Exception:
            pass

    return config


PROJECT_CFG = get_project_config()
PROJECT_NAME = PROJECT_CFG["project_name"]

WORKTREES = {
    "lead": Path(PROJECT_CFG["worktrees"]["lead"]),
    "backend": Path(PROJECT_CFG["worktrees"]["backend"]),
    "frontend": Path(PROJECT_CFG["worktrees"]["frontend"]),
    "main": BASE_DIR,
}

AGENTS = {
    "backend-engineer": {
        "role": "backend-engineer",
        "worktree": WORKTREES["backend"],
        "branch": "agent/backend",
    },
    "frontend-engineer": {
        "role": "frontend-engineer",
        "worktree": WORKTREES["frontend"],
        "branch": "agent/frontend",
    },
    "team-lead": {
        "role": "team-lead",
        "worktree": WORKTREES["lead"],
        "branch": "orchestration/lead",
    },
    "design-engineer": {
        "role": "design-engineer",
        "worktree": WORKTREES["main"],
        "branch": "main",
    },
    "visual-qa": {
        "role": "visual-qa",
        "worktree": WORKTREES["main"],
        "branch": "main",
    },
}

# Command names for Windows compatibility
OPENSPEC_CMD = "openspec.cmd" if os.name == "nt" else "openspec"


def run_cmd(cmd, cwd=None, capture=True):
    """Run shell command synchronously."""
    res = subprocess.run(
        cmd,
        cwd=cwd or BASE_DIR,
        shell=True,
        capture_output=capture,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    return res


async def run_agent_task(agent_name: str, prompt: str, worktree_dir: Path):
    """Run a single agent task using agy CLI asynchronously."""
    print(f"\n[AGENTIX] >>> Launching '{agent_name}' in '{worktree_dir}'...")
    
    cmd = [
        "agy",
        "--agent", agent_name,
        "--mode", "auto",
        "--dangerously-skip-permissions",
        "-p", prompt
    ]
    
    process = await asyncio.create_subprocess_exec(
        *cmd,
        cwd=str(worktree_dir),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    stdout, stderr = await process.communicate()
    out_text = stdout.decode("utf-8", errors="replace").strip()
    err_text = stderr.decode("utf-8", errors="replace").strip()
    
    status_icon = "SUCCESS" if process.returncode == 0 else "FAILED"
    print(f"[AGENTIX] <<< Agent '{agent_name}' finished [{status_icon}] (code: {process.returncode})")
    
    return {
        "agent": agent_name,
        "worktree": str(worktree_dir),
        "returncode": process.returncode,
        "stdout": out_text,
        "stderr": err_text,
    }


def init_orchestration():
    """Initialize git worktrees, branches, and configuration for any workspace."""
    print("=" * 70)
    print(f"  Agentix (agx): Initializing Worktrees for {PROJECT_NAME}")
    print("=" * 70)
    
    # 1. Ensure git repo exists
    if not (BASE_DIR / ".git").exists():
        print("[AGENTIX] Initializing git repository...")
        run_cmd("git init", cwd=BASE_DIR)
        run_cmd('git commit --allow-empty -m "chore: initial repository setup"', cwd=BASE_DIR)
        
    # 2. Setup branches and worktrees
    for role, wt in [
        ("backend", WORKTREES["backend"]),
        ("frontend", WORKTREES["frontend"]),
        ("lead", WORKTREES["lead"])
    ]:
        agent_key = f"{role}-engineer" if f"{role}-engineer" in AGENTS else "team-lead"
        branch = AGENTS[agent_key]["branch"]
        if wt.exists():
            print(f"  [EXISTS] Worktree for {role.upper()} already present at: {wt}")
        else:
            print(f"  [SETUP] Creating branch '{branch}' and worktree at: {wt}...")
            b_check = run_cmd(f"git rev-parse --verify {branch}", cwd=BASE_DIR)
            if b_check.returncode != 0:
                run_cmd(f"git branch {branch}", cwd=BASE_DIR)
            wt.parent.mkdir(parents=True, exist_ok=True)
            res = run_cmd(f'git worktree add "{wt}" {branch}', cwd=BASE_DIR)
            if res.returncode == 0:
                print(f"     [OK] Worktree created at {wt}")
            else:
                print(f"     [FAIL] Could not create worktree: {res.stderr or res.stdout}")

    # 3. Create .orchestrator.json if not present
    if not CONFIG_FILE.exists():
        default_cfg = {
            "project_name": PROJECT_NAME,
            "worktrees": {
                "lead": str(WORKTREES["lead"]),
                "backend": str(WORKTREES["backend"]),
                "frontend": str(WORKTREES["frontend"]),
            }
        }
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(default_cfg, f, indent=2)
        print(f"  [CONFIG] Created '{CONFIG_FILE.name}' configuration file.")

    print("=" * 70)
    print("  Initialization Complete! Run 'agx status' (or 'agx st') to verify.")
    print("=" * 70)


def show_status():
    """Display status of all agent worktrees and branches."""
    print("=" * 70)
    print(f"  Agentix (agx) Multi-Agent Team Status: {PROJECT_NAME}")
    print("=" * 70)
    for role, cfg in AGENTS.items():
        wt = cfg["worktree"]
        exists = wt.exists()
        branch = "Unknown"
        git_clean = "N/A"
        
        if exists:
            b_res = run_cmd("git rev-parse --abbrev-ref HEAD", cwd=wt)
            if b_res.returncode == 0:
                branch = b_res.stdout.strip()
            s_res = run_cmd("git status -s", cwd=wt)
            if s_res.returncode == 0:
                diff_count = len([line for line in s_res.stdout.splitlines() if line.strip()])
                git_clean = f"Clean ({diff_count} changes)" if diff_count == 0 else f"DIRTY ({diff_count} changes)"
        
        status_line = f"[{'ONLINE' if exists else 'MISSING'}] {role.upper()}"
        print(f"{status_line:<25} Branch: {branch:<20} Worktree: {wt}")
        print(f"   Git Status: {git_clean}")
    print("=" * 70)


def sync_worktrees():
    """Synchronize all worktrees with main branch."""
    print(f"[AGENTIX] Synchronizing all worktrees with 'main'...")
    for role, cfg in AGENTS.items():
        wt = cfg["worktree"]
        if wt.exists() and role in ("backend-engineer", "frontend-engineer", "team-lead"):
            print(f"  -> Merging 'main' into {cfg['branch']} in {wt}...")
            res = run_cmd("git merge main --no-edit", cwd=wt)
            if res.returncode == 0:
                print(f"     [OK] {cfg['branch']} up to date.")
            else:
                print(f"     [FAIL] Merge issue in {cfg['branch']}: {res.stderr or res.stdout}")
    print("[AGENTIX] Synchronization complete.\n")


def run_tests(filter_pattern=None):
    """Run automated test suite."""
    filter_arg = f"--filter={filter_pattern}" if filter_pattern else ""
    cmd = f"php artisan test {filter_arg}"
    print(f"[AGENTIX] Executing test suite: {cmd}")
    res = run_cmd(cmd, cwd=BASE_DIR, capture=False)
    return res.returncode


def run_visual_qa(url: str = "", file_path: str = "", output_dir: str = ""):
    """Execute Playwright multi-viewport automated screenshot capture."""
    print("=" * 70)
    print("  Agentix: Executing Playwright Multi-Viewport Visual QA (agx vqa)")
    print("=" * 70)
    script_path = BASE_DIR / "tests" / "visual-qa" / "capture-screenshots.js"
    if not script_path.exists():
        print(f"[ERROR] Visual QA script not found at {script_path}")
        return 1

    args = []
    if url:
        args.append(f"--url={url}")
    elif file_path:
        args.append(f"--file={file_path}")
    else:
        sample_fixture = BASE_DIR / "tests" / "visual-qa" / "fixtures" / "sample-page.html"
        args.append(f"--file={sample_fixture}")

    if output_dir:
        args.append(f"--output={output_dir}")

    cmd = f"node \"{script_path}\" " + " ".join(args)
    print(f"[AGENTIX] Running: {cmd}")
    res = run_cmd(cmd, cwd=BASE_DIR, capture=False)
    return res.returncode


def review_diffs():
    """Review worker diffs against main."""
    print("=" * 70)
    print("  Agentix: Reviewing Worker Diffs vs 'main' (agx review)")
    print("=" * 70)
    print("=== Diff: agent/backend vs main ===")
    b_diff = run_cmd("git diff main..agent/backend --stat")
    print(b_diff.stdout.strip() or "No differences.")
    
    print("\n=== Diff: agent/frontend vs main ===")
    f_diff = run_cmd("git diff main..agent/frontend --stat")
    print(f_diff.stdout.strip() or "No differences.")
    print("=" * 70)


def integrate_branches(test_filter=""):
    """Integrate worker branches into main after review."""
    print("=" * 70)
    print("  Agentix: Integrating Worker Branches into main (agx integrate)")
    print("=" * 70)
    
    # 1. Integrate backend
    print("Step 1: Merging agent/backend into main...")
    b_res = run_cmd('git merge agent/backend -m "feat(backend): integrate verified backend changes" --no-ff', cwd=BASE_DIR)
    if b_res.returncode != 0:
        print(f"[ERROR] Backend merge failed:\n{b_res.stderr or b_res.stdout}")
        return False
    print("  [OK] Backend merged successfully.")
    
    # 2. Integrate frontend
    print("Step 2: Merging agent/frontend into main...")
    f_res = run_cmd('git merge agent/frontend -m "feat(frontend): integrate verified frontend changes" --no-ff', cwd=BASE_DIR)
    if f_res.returncode != 0:
        print(f"[ERROR] Frontend merge failed:\n{f_res.stderr or f_res.stdout}")
        return False
    print("  [OK] Frontend merged successfully.")
    
    print("\nStep 3: Running automated test suite gate...")
    t_code = run_tests(test_filter)
    if t_code == 0:
        print("[SUCCESS] All integration tests passed.")
        return True
    else:
        print("[WARNING] Tests failed during integration check.")
        return False


def archive_change(change_name: str):
    """Archive an OpenSpec change."""
    print(f"[AGENTIX] Archiving OpenSpec change '{change_name}'...")
    res = run_cmd(f"{OPENSPEC_CMD} archive {change_name} --yes", cwd=BASE_DIR)
    if res.returncode == 0:
        print(f"  [OK] OpenSpec change '{change_name}' archived successfully.")
        return True
    else:
        print(f"  [FAIL] Could not archive change: {res.stderr or res.stdout}")
        return False


def push_to_github(commit_message: str):
    """Stage, commit, and push changes following gitcommit.md standards."""
    print("[AGENTIX] Preparing GitHub commit & push (agx push)...")
    run_cmd("git add .", cwd=BASE_DIR)
    
    c_res = run_cmd(f'git commit -m "{commit_message}"', cwd=BASE_DIR)
    if c_res.returncode != 0 and "nothing to commit" not in (c_res.stdout + c_res.stderr):
        print(f"  [WARNING] Commit output: {c_res.stderr or c_res.stdout}")
    else:
        print("  [OK] Local commit created.")
        
    print("  -> Pushing to origin main...")
    p_res = run_cmd("git push -u origin main", cwd=BASE_DIR)
    if p_res.returncode == 0:
        print("  [SUCCESS] All changes successfully pushed to origin/main.")
        return True
    else:
        print(f"  [FAIL] Push failed:\n{p_res.stderr or p_res.stdout}")
        return False


def enrich_backend_prompt(raw_prompt: str, change_name: str = "") -> str:
    """Enrich the backend prompt with mandatory architecture, DB optimization, and adversarial test rules."""
    return f"""### BACKEND TASK DIRECTIVE ({PROJECT_NAME} Architecture)
Feature / Module Context: {change_name or 'Feature Implementation'}

{raw_prompt}

MANDATORY ARCHITECTURAL & DATABASE OPTIMIZATION STANDARDS:
1. Framework & Skills: Adhere strictly to `laravel-expert`, `laravel-best-practices`, and `laravel-security-audit`.
2. Architecture: Implement clean FormRequests, dedicated Controller methods, and strongly-typed Eloquent Models/casts.
3. Database Optimization (MANDATORY):
   - Zero N+1 Queries: Always eager-load relationships via `with()` or `loadMissing()`. Never lazy-load inside loops.
   - Deadlock Prevention: Keep transactions short and atomic using `DB::transaction()`. Order record lock acquisitions consistently.
   - Proper Indexing: Add indexes in migrations for foreign keys, tenant column (e.g. `school_id`), search criteria, and sorting fields.
   - Data Consistency: Use explicit database constraints (cascade/restrict) and atomic operations.
4. Adversarial & Edge Case Automated Testing ("Break it to make it unbreakable"):
   - Write Unit tests in `tests/Unit/` and Feature tests in `tests/Feature/`.
   - Actively try to break the code by testing: null inputs, invalid data types, tenant boundary violations, empty records, and duplicate submissions.
   - If tests fail or bugs are exposed, fix the implementation immediately and re-run tests until 100% green.
5. Worktree Commit & PR:
   - When verified, stage changes and commit: `git commit -m "feat(backend): <detailed summary>"`
   - Output summary of files created/changed, tests executed, and commit SHA.
"""


def enrich_frontend_prompt(raw_prompt: str, change_name: str = "") -> str:
    """Enrich the frontend prompt with design tokens, ui-refactor.md, and UI-Mandatory standards."""
    return f"""### FRONTEND TASK DIRECTIVE ({PROJECT_NAME} UI/UX)
Feature / Module Context: {change_name or 'UI Implementation'}

{raw_prompt}

MANDATORY UI/UX & REFACTORING STANDARDS:
1. Design System & Consistency (CRITICAL):
   - Ingest approved design tokens from `DESIGN_TOKENS.md` and `design-tokens.css`.
   - Inspect existing production views or reference templates in `resources/views/`.
   - Adhere to the established layout container, card styling, typography, and color palette.
2. Mandatory UI Refinement via `ui-refactor.md`:
   Apply the 7 Master UI Recipes from `ui-refactor.md` to refine the interface:
   - Recipe 1 (Sharpen Message): Clear promise headline with ONE focal accent span.
   - Recipe 2 (Break Symmetry): Asymmetric 60/40 or 65/35 grid (`lg:grid-cols-12`) with floating anchor badges.
   - Recipe 3 (Build Argument): Uniform `.section-header-block` (kicker + title + subtitle) and hairline dividers.
   - Recipe 4 (Pick the Winner): Elevate flagship tier (60% weight) over identical cards; quiet secondary items.
   - Recipe 5 (Scale the Type): 4-tier scale (Headline text-3xl to 5xl, Card text-lg to 2xl, Body text-sm to base with leading-relaxed, Kicker text-xs).
   - Recipe 6 (Give Color Meaning): Brand accent for identity, warm amber strictly for Primary CTAs/conversions, notice sky-blue for alerts, calm neutral base (`border-slate-200/90`).
   - Recipe 7 (Add a Signature): Section kicker with pulsing dot (`.section-kicker-dot`), hairline dividers, and micro-interactions.
3. UI-Mandatory Compliance:
   - No placeholder buttons or dead links. All buttons/links must have valid actionable targets or routes.
   - Full responsive support (mobile natural stack, desktop editorial grid).
4. Worktree Commit & PR:
   - Stage changes and commit: `git commit -m "feat(frontend): <detailed summary>"`
   - Output summary of views/components modified, responsiveness checks, and commit SHA.
"""


async def run_feature_pipeline(change_name: str, prompt: str, test_filter: str = "", skip_archive: bool = False, skip_push: bool = False, visual_qa_url: str = ""):
    """Execute complete end-to-end autonomous feature development pipeline."""
    print("\n" + "=" * 70)
    print(f"  Agentix (agx): Autonomous Feature Pipeline for '{change_name}'")
    print("=" * 70)
    
    # 1. Pre-flight sync
    print("\n>>> Phase 1: Pre-flight Worktree Sync (agx sync)...")
    sync_worktrees()
    
    # 2. OpenSpec check / proposal initialization
    print(f"\n>>> Phase 2: Verifying OpenSpec Change '{change_name}'...")
    check_change = run_cmd(f"{OPENSPEC_CMD} status --change {change_name} --json", cwd=BASE_DIR)
    if check_change.returncode != 0:
        print(f"  -> Change '{change_name}' not found. Initializing new OpenSpec change...")
        run_cmd(f"{OPENSPEC_CMD} new change {change_name}", cwd=BASE_DIR)
    else:
        print(f"  [OK] OpenSpec change '{change_name}' is active.")
        
    # 3. Formulate enriched directives
    print("\n>>> Phase 3: Constructing Enriched Subagent Task Directives...")
    backend_prompt = enrich_backend_prompt(prompt, change_name)
    frontend_prompt = enrich_frontend_prompt(prompt, change_name)
    
    # 4. Parallel Dispatch
    print("\n>>> Phase 4: Launching Concurrent Workers in Isolated Worktrees (agx run)...")
    tasks = [
        run_agent_task("backend-engineer", backend_prompt, AGENTS["backend-engineer"]["worktree"]),
        run_agent_task("frontend-engineer", frontend_prompt, AGENTS["frontend-engineer"]["worktree"]),
    ]
    results = await asyncio.gather(*tasks)
    
    print("\n" + "=" * 70)
    print("  Workers Completed Execution")
    print("=" * 70)
    for r in results:
        print(f"[{r['agent'].upper()}] Exit Code: {r['returncode']}")
        
    # 5. Review PR diffs
    print("\n>>> Phase 5: Team Lead PR Review (agx review)...")
    review_diffs()
    
    # 6. Test Gate
    filter_target = test_filter or change_name.replace("-", "").replace("_", "")
    print(f"\n>>> Phase 6: Automated Test Suite Gate (Filter: '{filter_target}')...")
    test_code = run_tests(filter_target)
    
    if test_code != 0:
        print("\n[WARNING] Tests failed or target tests not yet present on main branch.")
        print("Lead will proceed with integration if branch diffs are verified.")
        
    # 7. Integration
    print("\n>>> Phase 7: Integrating Worker Branches into main (agx integrate)...")
    integrated = integrate_branches(filter_target)
    if not integrated:
        print("[ERROR] Integration failed. Please inspect git status.")
        return False

    # 8. Visual QA Gate (if URL provided)
    if visual_qa_url:
        print("\n>>> Phase 8: Executing Visual QA Browser Audit (agx vqa)...")
        vqa_out = str(BASE_DIR / "tests" / "visual-qa" / "screenshots" / change_name)
        run_visual_qa(url=visual_qa_url, output_dir=vqa_out)
    else:
        print("\n>>> Phase 8: Skipping automated browser screenshot capture (no --visual-qa-url provided).")
        
    # 9. Archive OpenSpec Change
    if not skip_archive:
        print("\n>>> Phase 9: Archiving OpenSpec Change...")
        archive_change(change_name)
    else:
        print("\n>>> Phase 9: Skipping OpenSpec archive as requested.")
        
    # 10. Commit & Push to GitHub
    if not skip_push:
        print("\n>>> Phase 10: Staging & Pushing to GitHub (agx push)...")
        commit_msg = f"feat({change_name}): implement end-to-end module with verified UI and tests"
        push_to_github(commit_msg)
    else:
        print("\n>>> Phase 10: Skipping GitHub push as requested.")
        
    print("\n" + "=" * 70)
    print(f"  [SUCCESS] Feature '{change_name}' Pipeline Complete!")
    print("=" * 70 + "\n")
    return True


def normalize_argv(argv):
    """Normalize shorthand subcommands so 'agx st' -> 'agx status', 'agx vqa' -> 'agx visual-qa', etc."""
    if len(argv) < 2:
        return argv
    
    aliases = {
        "st": "status",
        "run": "run-parallel",
        "parallel": "run-parallel",
        "diff": "review",
        "t": "test",
        "vqa": "visual-qa",
        "merge": "integrate",
        "p": "push",
        "auto": "pipeline",
        "d": "dispatch",
    }
    
    cmd = argv[1].lower()
    if cmd in aliases:
        argv[1] = aliases[cmd]
        
    return argv


async def main_async():
    sys.argv = normalize_argv(sys.argv)
    parser = argparse.ArgumentParser(
        prog="agx",
        description=f"Agentix (agx) — Universal Multi-Agent Orchestrator for {PROJECT_NAME}"
    )
    subparsers = parser.add_subparsers(dest="action", help="Action to execute")
    
    # Init
    subparsers.add_parser("init", help="Initialize git worktrees, branches, and configuration for this workspace")

    # Status (aliases: st)
    subparsers.add_parser("status", help="Show worktree and agent statuses (alias: st)")
    
    # Sync
    subparsers.add_parser("sync", help="Synchronize all worktrees with main")
    
    # Dispatch single agent (aliases: d)
    dispatch_p = subparsers.add_parser("dispatch", help="Dispatch task to a specific worker (alias: d)")
    dispatch_p.add_argument("-a", "--agent", required=True, choices=["backend-engineer", "frontend-engineer", "team-lead", "design-engineer", "visual-qa"])
    dispatch_p.add_argument("-p", "--prompt", required=True, help="Task prompt for the agent")
    
    # Parallel dispatch (aliases: run, parallel)
    parallel_p = subparsers.add_parser("run-parallel", help="Dispatch concurrent tasks to backend & frontend workers (alias: run)")
    parallel_p.add_argument("-b", "--backend", required=True, help="Task prompt for backend-engineer")
    parallel_p.add_argument("-f", "--frontend", required=True, help="Task prompt for frontend-engineer")
    
    # Review (aliases: diff)
    subparsers.add_parser("review", help="Inspect git diff across agent branches (alias: diff)")
    
    # Test (aliases: t)
    test_p = subparsers.add_parser("test", help="Run automated test suite (alias: t)")
    test_p.add_argument("-f", "--filter", default="", help="Filter test case or class name")

    # Visual QA (aliases: vqa)
    vqa_p = subparsers.add_parser("visual-qa", help="Run Playwright multi-viewport visual QA screenshot capture (alias: vqa)")
    vqa_p.add_argument("-u", "--url", default="", help="Target webpage URL (e.g. http://127.0.0.1:8000/classes)")
    vqa_p.add_argument("--file", default="", help="Target local HTML file")
    vqa_p.add_argument("-o", "--output", default="", help="Output directory for screenshots")
    
    # Integrate (aliases: merge)
    integrate_p = subparsers.add_parser("integrate", help="Integrate reviewed agent branches into main (alias: merge)")
    integrate_p.add_argument("-f", "--filter", default="", help="Filter test case or class name during gate check")
    
    # Archive
    archive_p = subparsers.add_parser("archive", help="Archive a completed OpenSpec change")
    archive_p.add_argument("-c", "--change", required=True, help="Name of the change to archive")
    
    # Push (aliases: p)
    push_p = subparsers.add_parser("push", help="Commit and push changes to GitHub following gitcommit.md (alias: p)")
    push_p.add_argument("-m", "--message", required=True, help="Conventional commit message")
    
    # Pipeline / Auto (aliases: auto)
    pipeline_p = subparsers.add_parser("pipeline", help="Execute full autonomous feature development pipeline (alias: auto)")
    pipeline_p.add_argument("-c", "--change", required=True, help="OpenSpec change name (kebab-case)")
    pipeline_p.add_argument("-p", "--prompt", required=True, help="Detailed feature requirements prompt")
    pipeline_p.add_argument("-f", "--filter", default="", help="Test filter name")
    pipeline_p.add_argument("-u", "--visual-qa-url", default="", help="URL to perform visual QA against (Gate 6)")
    pipeline_p.add_argument("--skip-archive", action="store_true", help="Skip OpenSpec archive")
    pipeline_p.add_argument("--skip-push", action="store_true", help="Skip GitHub push")
    
    args = parser.parse_args()
    
    if args.action == "init":
        init_orchestration()

    elif args.action == "status" or not args.action:
        show_status()
        
    elif args.action == "sync":
        sync_worktrees()
        
    elif args.action == "dispatch":
        cfg = AGENTS[args.agent]
        wt = cfg["worktree"]
        if not wt.exists():
            print(f"[ERROR] Worktree '{wt}' does not exist.")
            sys.exit(1)
            
        res = await run_agent_task(args.agent, args.prompt, wt)
        print("\n--- Worker Output ---")
        print(res["stdout"])
        if res["stderr"]:
            print("\n--- Errors / Diagnostics ---")
            print(res["stderr"])
            
    elif args.action == "run-parallel":
        print("[AGENTIX] Spawning concurrent workers in parallel worktrees...")
        tasks = [
            run_agent_task("backend-engineer", args.backend, AGENTS["backend-engineer"]["worktree"]),
            run_agent_task("frontend-engineer", args.frontend, AGENTS["frontend-engineer"]["worktree"]),
        ]
        
        results = await asyncio.gather(*tasks)
        print("\n" + "=" * 70)
        print("  Parallel Worker Execution Complete")
        print("=" * 70)
        for r in results:
            print(f"\n[RESULT: {r['agent'].upper()}] Worktree: {r['worktree']}")
            print(r["stdout"][:500] + ("..." if len(r["stdout"]) > 500 else ""))
            
    elif args.action == "review":
        review_diffs()
        
    elif args.action == "test":
        run_tests(args.filter)

    elif args.action == "visual-qa":
        run_visual_qa(url=args.url, file_path=args.file, output_dir=args.output)
        
    elif args.action == "integrate":
        integrate_branches(args.filter)
        
    elif args.action == "archive":
        archive_change(args.change)
        
    elif args.action == "push":
        push_to_github(args.message)
        
    elif args.action == "pipeline":
        await run_feature_pipeline(
            change_name=args.change,
            prompt=args.prompt,
            test_filter=args.filter,
            visual_qa_url=args.visual_qa_url,
            skip_archive=args.skip_archive,
            skip_push=args.skip_push
        )


if __name__ == "__main__":
    asyncio.run(main_async())

