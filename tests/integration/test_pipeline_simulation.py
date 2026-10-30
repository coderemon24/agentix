"""
Integration tests for the 10-Phase Autonomous Feature Pipeline.
Simulates subagent execution and verifies pipeline phase progression and error handling.
"""
import sys
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import agx


class TestPipelineSimulation(unittest.TestCase):
    """Test full pipeline simulation with mocked workers."""

    def test_pipeline_success_flow(self):
        """Simulate a completely successful 10-phase run."""
        mock_agent_result = {
            "agent": "backend-engineer",
            "worktree": "mock-wt",
            "returncode": 0,
            "stdout": "Implemented verified feature.",
            "stderr": "",
        }

        with patch.object(agx, "sync_worktrees") as mock_sync, \
             patch.object(agx, "run_cmd") as mock_cmd, \
             patch.object(agx, "run_agent_task", new_callable=AsyncMock) as mock_agent, \
             patch.object(agx, "review_diffs") as mock_review, \
             patch.object(agx, "run_tests", return_value=0) as mock_test, \
             patch.object(agx, "integrate_branches", return_value=True) as mock_integrate, \
             patch.object(agx, "run_visual_qa", return_value=0) as mock_vqa, \
             patch.object(agx, "archive_change", return_value=True) as mock_archive, \
             patch.object(agx, "push_to_github", return_value=True) as mock_push:

            # Mock OpenSpec check command returning success (exit code 0)
            mock_cmd_return = unittest.mock.MagicMock()
            mock_cmd_return.returncode = 0
            mock_cmd.return_value = mock_cmd_return

            mock_agent.return_value = mock_agent_result

            # Run pipeline asynchronously using asyncio.run
            import asyncio
            result = asyncio.run(agx.run_feature_pipeline(
                change_name="syllabus-directory",
                prompt="Implement syllabus viewing page",
                test_filter="SyllabusTest",
                visual_qa_url="http://127.0.0.1:8000/syllabus",
                skip_archive=False,
                skip_push=False,
            ))

            self.assertTrue(result, "Pipeline should return True on complete success")
            mock_sync.assert_called_once()
            self.assertEqual(mock_agent.call_count, 2)  # backend + frontend
            mock_review.assert_called_once()
            mock_integrate.assert_called_once_with("SyllabusTest")
            mock_vqa.assert_called_once()
            mock_archive.assert_called_once_with("syllabus-directory")
            mock_push.assert_called_once()

    def test_pipeline_integration_failure_halts_early(self):
        """Verify pipeline stops if branch integration fails (e.g. merge conflict or test fail)."""
        mock_agent_result = {
            "agent": "backend-engineer",
            "worktree": "mock-wt",
            "returncode": 0,
            "stdout": "Worker done.",
            "stderr": "",
        }

        with patch.object(agx, "sync_worktrees"), \
             patch.object(agx, "run_cmd"), \
             patch.object(agx, "run_agent_task", new_callable=AsyncMock) as mock_agent, \
             patch.object(agx, "review_diffs"), \
             patch.object(agx, "run_tests", return_value=0), \
             patch.object(agx, "integrate_branches", return_value=False) as mock_integrate, \
             patch.object(agx, "archive_change") as mock_archive, \
             patch.object(agx, "push_to_github") as mock_push:

            mock_agent.return_value = mock_agent_result

            import asyncio
            result = asyncio.run(agx.run_feature_pipeline(
                change_name="failing-feature",
                prompt="Some change that fails merge",
                skip_archive=False,
                skip_push=False,
            ))

            self.assertFalse(result, "Pipeline should return False when integration fails")
            mock_integrate.assert_called_once()
            # Archive and Push should NOT be called after integration failure
            mock_archive.assert_not_called()
            mock_push.assert_not_called()

    def test_pipeline_skip_flags(self):
        """Verify skip_archive and skip_push flags are honored."""
        mock_agent_result = {
            "agent": "worker",
            "worktree": "mock-wt",
            "returncode": 0,
            "stdout": "Worker done.",
            "stderr": "",
        }

        with patch.object(agx, "sync_worktrees"), \
             patch.object(agx, "run_cmd"), \
             patch.object(agx, "run_agent_task", new_callable=AsyncMock, return_value=mock_agent_result), \
             patch.object(agx, "review_diffs"), \
             patch.object(agx, "run_tests", return_value=0), \
             patch.object(agx, "integrate_branches", return_value=True), \
             patch.object(agx, "archive_change") as mock_archive, \
             patch.object(agx, "push_to_github") as mock_push:

            import asyncio
            result = asyncio.run(agx.run_feature_pipeline(
                change_name="skip-feature",
                prompt="Skip test prompt",
                skip_archive=True,
                skip_push=True,
            ))

            self.assertTrue(result)
            mock_archive.assert_not_called()
            mock_push.assert_not_called()


if __name__ == "__main__":
    unittest.main()

