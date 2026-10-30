"""
Integration tests for Git Worktree lifecycle and multi-agent branch orchestration.
Executes against an isolated, temporary Git sandbox without touching workspace state.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import agx


class TestGitWorktreesIntegration(unittest.TestCase):
    """Hermetic Git integration test suite in temporary sandbox."""

    def setUp(self):
        # Create temporary root for sandbox
        self.test_dir = tempfile.mkdtemp(prefix="agentix_test_")
        self.root_path = Path(self.test_dir) / "repo-root"
        self.root_path.mkdir(parents=True, exist_ok=True)

        # Configure git identity in sandbox
        subprocess.run(["git", "init"], cwd=self.root_path, capture_output=True, check=True)
        subprocess.run(["git", "config", "user.name", "Agentix Test"], cwd=self.root_path, capture_output=True, check=True)
        subprocess.run(["git", "config", "user.email", "test@agentix.local"], cwd=self.root_path, capture_output=True, check=True)

        # Ensure initial commit exists on 'main'
        readme_file = self.root_path / "README.md"
        readme_file.write_text("# Test Repo Root\n", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=self.root_path, capture_output=True, check=True)
        subprocess.run(["git", "commit", "-m", "chore: initial sandbox commit"], cwd=self.root_path, capture_output=True, check=True)

        # Ensure branch is named 'main'
        subprocess.run(["git", "branch", "-M", "main"], cwd=self.root_path, capture_output=True, check=True)

        # Define worktree paths
        self.lead_wt = Path(self.test_dir) / "worktrees" / "lead"
        self.backend_wt = Path(self.test_dir) / "worktrees" / "backend"
        self.frontend_wt = Path(self.test_dir) / "worktrees" / "frontend"

        self.mock_worktrees = {
            "lead": self.lead_wt,
            "backend": self.backend_wt,
            "frontend": self.frontend_wt,
            "main": self.root_path,
        }

        self.mock_agents = {
            "backend-engineer": {
                "role": "backend-engineer",
                "worktree": self.backend_wt,
                "branch": "agent/backend",
            },
            "frontend-engineer": {
                "role": "frontend-engineer",
                "worktree": self.frontend_wt,
                "branch": "agent/frontend",
            },
            "team-lead": {
                "role": "team-lead",
                "worktree": self.lead_wt,
                "branch": "orchestration/lead",
            },
            "design-engineer": {
                "role": "design-engineer",
                "worktree": self.root_path,
                "branch": "main",
            },
            "visual-qa": {
                "role": "visual-qa",
                "worktree": self.root_path,
                "branch": "main",
            },
        }

        self.mock_config_file = self.root_path / ".orchestrator.json"

        # Apply patches
        self.patchers = [
            patch.object(agx, "BASE_DIR", self.root_path),
            patch.object(agx, "WORKTREES", self.mock_worktrees),
            patch.object(agx, "AGENTS", self.mock_agents),
            patch.object(agx, "CONFIG_FILE", self.mock_config_file),
            patch.object(agx, "PROJECT_NAME", "TestSandbox"),
        ]
        for p in self.patchers:
            p.start()

    def tearDown(self):
        for p in reversed(self.patchers):
            p.stop()
        # Clean up sandbox directory
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_init_orchestration_creates_worktrees_and_config(self):
        agx.init_orchestration()

        # Check that worktree directories exist
        self.assertTrue(self.lead_wt.exists(), "Lead worktree was not created")
        self.assertTrue(self.backend_wt.exists(), "Backend worktree was not created")
        self.assertTrue(self.frontend_wt.exists(), "Frontend worktree was not created")

        # Check branches are assigned correctly
        lead_branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=self.lead_wt, capture_output=True, text=True).stdout.strip()
        backend_branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=self.backend_wt, capture_output=True, text=True).stdout.strip()
        frontend_branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=self.frontend_wt, capture_output=True, text=True).stdout.strip()

        self.assertEqual(lead_branch, "orchestration/lead")
        self.assertEqual(backend_branch, "agent/backend")
        self.assertEqual(frontend_branch, "agent/frontend")

        # Check configuration file was created
        self.assertTrue(self.mock_config_file.exists(), ".orchestrator.json was not created")
        with open(self.mock_config_file, "r", encoding="utf-8") as f:
            cfg = json.load(f)
            self.assertEqual(cfg["project_name"], "TestSandbox")
            self.assertEqual(cfg["worktrees"]["backend"], str(self.backend_wt))

    def test_show_status_detects_clean_and_dirty_states(self):
        agx.init_orchestration()

        # Initially all worktrees should be clean
        backend_status = subprocess.run(["git", "status", "-s"], cwd=self.backend_wt, capture_output=True, text=True).stdout.strip()
        self.assertEqual(backend_status, "")

        # Modify a file in backend worktree (make it dirty)
        dirty_file = self.backend_wt / "test_api.php"
        dirty_file.write_text("<?php // new change", encoding="utf-8")

        backend_status_dirty = subprocess.run(["git", "status", "-s"], cwd=self.backend_wt, capture_output=True, text=True).stdout.strip()
        self.assertIn("test_api.php", backend_status_dirty)

    def test_sync_worktrees_propagates_main_commits(self):
        agx.init_orchestration()

        # Commit a new file to main
        new_feature = self.root_path / "SHARED_CONTRACT.md"
        new_feature.write_text("# Contracts", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=self.root_path, capture_output=True, check=True)
        subprocess.run(["git", "commit", "-m", "feat: add shared contract"], cwd=self.root_path, capture_output=True, check=True)

        # Before sync, backend worktree should not have SHARED_CONTRACT.md
        self.assertFalse((self.backend_wt / "SHARED_CONTRACT.md").exists())

        # Execute sync
        agx.sync_worktrees()

        # After sync, SHARED_CONTRACT.md should be merged into backend worktree
        self.assertTrue((self.backend_wt / "SHARED_CONTRACT.md").exists())

    def test_integrate_branches_merges_worker_commits_into_main(self):
        agx.init_orchestration()

        # 1. Backend commit
        be_file = self.backend_wt / "api.php"
        be_file.write_text("<?php echo 'backend ok';", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=self.backend_wt, capture_output=True, check=True)
        subprocess.run(["git", "commit", "-m", "feat(backend): add api"], cwd=self.backend_wt, capture_output=True, check=True)

        # 2. Frontend commit
        fe_file = self.frontend_wt / "view.html"
        fe_file.write_text("<h1>Frontend View</h1>", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=self.frontend_wt, capture_output=True, check=True)
        subprocess.run(["git", "commit", "-m", "feat(frontend): add view"], cwd=self.frontend_wt, capture_output=True, check=True)

        # Integrate with mocked test runner passing (exit code 0)
        with patch.object(agx, "run_tests", return_value=0):
            success = agx.integrate_branches(test_filter="test")
            self.assertTrue(success)

        # Check both files now exist on main
        self.assertTrue((self.root_path / "api.php").exists(), "api.php was not merged to main")
        self.assertTrue((self.root_path / "view.html").exists(), "view.html was not merged to main")

        # Verify git log on main shows merge commits
        log_out = subprocess.run(["git", "log", "--oneline", "-n", "5"], cwd=self.root_path, capture_output=True, text=True).stdout
        self.assertIn("feat(backend): integrate verified backend changes", log_out)
        self.assertIn("feat(frontend): integrate verified frontend changes", log_out)


if __name__ == "__main__":
    unittest.main()

