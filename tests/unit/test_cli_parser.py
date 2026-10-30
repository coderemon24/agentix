"""
Unit tests for CLI parser and argument normalization.
"""
import sys
import unittest
from pathlib import Path

# Add scripts directory to path
SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import agx


class TestCLIParser(unittest.TestCase):
    """Test CLI argument normalization and shorthands."""

    def test_empty_or_single_arg(self):
        self.assertEqual(agx.normalize_argv([]), [])
        self.assertEqual(agx.normalize_argv(["agx"]), ["agx"])

    def test_status_alias(self):
        self.assertEqual(agx.normalize_argv(["agx", "st"]), ["agx", "status"])
        self.assertEqual(agx.normalize_argv(["agx", "ST"]), ["agx", "status"])

    def test_run_parallel_aliases(self):
        self.assertEqual(agx.normalize_argv(["agx", "run"]), ["agx", "run-parallel"])
        self.assertEqual(agx.normalize_argv(["agx", "parallel"]), ["agx", "run-parallel"])

    def test_review_alias(self):
        self.assertEqual(agx.normalize_argv(["agx", "diff"]), ["agx", "review"])

    def test_test_alias(self):
        self.assertEqual(agx.normalize_argv(["agx", "t"]), ["agx", "test"])

    def test_visual_qa_alias(self):
        self.assertEqual(agx.normalize_argv(["agx", "vqa"]), ["agx", "visual-qa"])

    def test_integrate_alias(self):
        self.assertEqual(agx.normalize_argv(["agx", "merge"]), ["agx", "integrate"])

    def test_push_alias(self):
        self.assertEqual(agx.normalize_argv(["agx", "p"]), ["agx", "push"])

    def test_pipeline_alias(self):
        self.assertEqual(agx.normalize_argv(["agx", "auto"]), ["agx", "pipeline"])

    def test_dispatch_alias(self):
        self.assertEqual(agx.normalize_argv(["agx", "d"]), ["agx", "dispatch"])

    def test_unknown_command_preserved(self):
        self.assertEqual(agx.normalize_argv(["agx", "unknown"]), ["agx", "unknown"])
        self.assertEqual(agx.normalize_argv(["agx", "status"]), ["agx", "status"])


if __name__ == "__main__":
    unittest.main()

