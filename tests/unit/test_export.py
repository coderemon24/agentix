"""
Unit tests for the agx export / bundle production packaging subsystem.
"""
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import agx


class TestExportProduction(unittest.TestCase):
    """Test clean production export packaging."""

    def test_export_zip_excludes_all_agent_and_orchestration_files(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_zip = Path(tmp_dir) / "test-clean-release.zip"

            zip_path_str, file_count = agx.export_project(output_path=str(out_zip), format_type="zip")

            self.assertTrue(out_zip.exists(), "Export zip archive was not created")
            self.assertGreater(file_count, 0, "Clean package must contain project files")

            # Inspect zip contents
            with zipfile.ZipFile(out_zip, "r") as zf:
                names = zf.namelist()

                # Verify clean project files ARE present
                self.assertIn("README.md", names)
                self.assertIn("LICENSE", names)

                # Verify ZERO agent, orchestrator, or internal test files exist
                for name in names:
                    self.assertFalse(name.startswith(".agents"), f"Agent directory leaked into package: {name}")
                    self.assertFalse(name.startswith(".cursor"), f"Cursor directory leaked: {name}")
                    self.assertFalse(name.startswith("tests/"), f"Test files leaked into production zip: {name}")
                    self.assertFalse("agx" in name and name != "package.json", f"Orchestrator executable leaked: {name}")
                    self.assertNotIn(name, [
                        "AGENTS.md", "USER_MANUAL.md", "CLAUDE.md",
                        "UI-Mandatory.md", "ui-refactor.md", "gitcommit.md",
                        "install.ps1", "install.sh", ".orchestrator.json"
                    ])

    def test_export_directory_format(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_dir = Path(tmp_dir) / "production-dist"

            dir_path_str, file_count = agx.export_project(output_path=str(out_dir), format_type="dir")

            self.assertTrue(out_dir.exists(), "Export directory was not created")
            self.assertTrue((out_dir / "README.md").exists())
            self.assertFalse((out_dir / "AGENTS.md").exists())
            self.assertFalse((out_dir / ".agents").exists())
            self.assertFalse((out_dir / "tests").exists())


if __name__ == "__main__":
    unittest.main()

