"""
Agentix (agx) — Unified Automated Test Runner & Health Dashboard.
Executes all unit, integration, and visual-qa tests with comprehensive reporting.
"""
import sys
import time
import unittest
from pathlib import Path

# Add project root and scripts to path
BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = BASE_DIR / "scripts"
TESTS_DIR = BASE_DIR / "tests"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))


def run_suite(suite_name: str, test_dir: Path, pattern: str = "test*.py"):
    print(f"\n{'=' * 70}")
    print(f"  RUNNING SUITE: {suite_name}")
    print(f"{'=' * 70}")

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(test_dir), pattern=pattern)

    runner = unittest.TextTestRunner(verbosity=2)
    start_time = time.time()
    result = runner.run(suite)
    elapsed = time.time() - start_time

    return {
        "name": suite_name,
        "total": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "passed": result.testsRun - len(result.failures) - len(result.errors),
        "elapsed": elapsed,
        "success": result.wasSuccessful(),
    }


def main():
    print("*" * 70)
    print("   AGENTIX (agx) MULTI-AGENT ORCHESTRATOR — AUTOMATED TEST SUITE")
    print("*" * 70)

    overall_start = time.time()
    suites = []

    # 1. Unit Tests
    unit_res = run_suite("Tier 1: Core Unit Tests (Parser, Config, Prompts, VQA)", TESTS_DIR / "unit")
    suites.append(unit_res)

    # 2. Integration Tests (Git worktrees & pipeline simulation)
    integ_res = run_suite("Tier 2 & 3: Git Worktrees & Pipeline Simulation", TESTS_DIR / "integration")
    suites.append(integ_res)

    overall_elapsed = time.time() - overall_start

    # Final Dashboard
    print("\n" + "#" * 70)
    print("   TEST EXECUTION SUMMARY & HEALTH DASHBOARD")
    print("#" * 70)
    print(f"{'Suite Name':<48} | {'Total':<6} | {'Pass':<6} | {'Fail':<6} | {'Time':<6}")
    print("-" * 78)

    all_success = True
    total_tests = 0
    total_passed = 0
    total_failed = 0

    for s in suites:
        status_flag = "[OK]" if s["success"] else "[FAIL]"
        print(f"{s['name']:<48} | {s['total']:<6} | {s['passed']:<6} | {s['failures'] + s['errors']:<6} | {s['elapsed']:.2f}s")
        if not s["success"]:
            all_success = False
        total_tests += s["total"]
        total_passed += s["passed"]
        total_failed += s["failures"] + s["errors"]

    print("-" * 78)
    print(f"{'TOTALS':<48} | {total_tests:<6} | {total_passed:<6} | {total_failed:<6} | {overall_elapsed:.2f}s")
    print("#" * 70)

    if all_success:
        print("\n [SUCCESS] ALL ORCHESTRATION TESTS PASSED! Framework is verified healthy.")
        print("#" * 70 + "\n")
        sys.exit(0)
    else:
        print("\n [FAILURE] Some orchestration tests failed. Please review the trace above.")
        print("#" * 70 + "\n")
        sys.exit(1)


if __name__ == "__main__":
    main()

