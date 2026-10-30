"""
Automated tests for Playwright Visual QA subsystem (agx vqa).
"""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import agx


class TestVisualQA(unittest.TestCase):
    """Test Visual QA runner and screenshot capture."""

    def setUp(self):
        self.base_dir = Path(__file__).resolve().parent.parent.parent
        self.script_path = self.base_dir / "tests" / "visual-qa" / "capture-screenshots.js"
        self.fixture_path = self.base_dir / "tests" / "visual-qa" / "fixtures" / "sample-page.html"

    def test_visual_qa_files_exist(self):
        self.assertTrue(self.script_path.exists(), "capture-screenshots.js must exist")
        self.assertTrue(self.fixture_path.exists(), "sample-page.html fixture must exist")

    def test_visual_qa_screenshot_generation(self):
        """Execute capture-screenshots against fixture in temporary output directory."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_dir = Path(tmp_dir) / "screenshots"
            exit_code = agx.run_visual_qa(file_path=str(self.fixture_path), output_dir=str(out_dir))

            self.assertEqual(exit_code, 0, "Visual QA execution should return exit code 0")

            desktop_img = out_dir / "desktop-1440.png"
            tablet_img = out_dir / "tablet-768.png"
            mobile_img = out_dir / "mobile-375.png"

            self.assertTrue(desktop_img.exists(), "Desktop screenshot desktop-1440.png was not generated")
            self.assertTrue(tablet_img.exists(), "Tablet screenshot tablet-768.png was not generated")
            self.assertTrue(mobile_img.exists(), "Mobile screenshot mobile-375.png was not generated")

            # Check files are non-empty
            self.assertGreater(desktop_img.stat().st_size, 1000)
            self.assertGreater(tablet_img.stat().st_size, 1000)
            self.assertGreater(mobile_img.stat().st_size, 1000)


if __name__ == "__main__":
    unittest.main()

