"""
Unit tests for Project Configuration Loader.
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import agx


class TestProjectConfig(unittest.TestCase):
    """Test project configuration resolution and overrides."""

    def test_default_config_structure(self):
        cfg = agx.get_project_config()
        self.assertIn("project_name", cfg)
        self.assertIn("worktrees", cfg)
        self.assertIn("lead", cfg["worktrees"])
        self.assertIn("backend", cfg["worktrees"])
        self.assertIn("frontend", cfg["worktrees"])
        self.assertIsInstance(cfg["project_name"], str)

    def test_config_file_overrides(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            cfg_file = tmp_path / ".orchestrator.json"
            custom_data = {
                "project_name": "Custom Test App",
                "worktrees": {
                    "lead": str(tmp_path / "custom-lead"),
                    "backend": str(tmp_path / "custom-backend"),
                    "frontend": str(tmp_path / "custom-frontend"),
                }
            }
            with open(cfg_file, "w", encoding="utf-8") as f:
                json.dump(custom_data, f)

            with patch.object(agx, "CONFIG_FILE", cfg_file):
                loaded_cfg = agx.get_project_config()
                self.assertEqual(loaded_cfg["project_name"], "Custom Test App")
                self.assertEqual(loaded_cfg["worktrees"]["backend"], str(tmp_path / "custom-backend"))
                self.assertEqual(loaded_cfg["worktrees"]["frontend"], str(tmp_path / "custom-frontend"))
                self.assertEqual(loaded_cfg["worktrees"]["lead"], str(tmp_path / "custom-lead"))


if __name__ == "__main__":
    unittest.main()

