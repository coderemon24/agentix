"""
Unit tests for Backend and Frontend prompt enrichment logic.
"""
import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import agx


class TestPromptEnrichment(unittest.TestCase):
    """Test enrichment directives for subagents."""

    def test_backend_prompt_enrichment_contains_critical_directives(self):
        raw_prompt = "Create Student Management CRUD API with grade filtering."
        change_name = "student-management"
        enriched = agx.enrich_backend_prompt(raw_prompt, change_name)

        # 1. Contains user raw prompt and feature context
        self.assertIn(raw_prompt, enriched)
        self.assertIn("Feature / Module Context: student-management", enriched)

        # 2. Contains framework expert skills
        self.assertIn("laravel-expert", enriched)
        self.assertIn("laravel-best-practices", enriched)
        self.assertIn("laravel-security-audit", enriched)

        # 3. Contains mandatory database optimization directives
        self.assertIn("Zero N+1 Queries", enriched)
        self.assertIn("with()", enriched)
        self.assertIn("loadMissing()", enriched)
        self.assertIn("Deadlock Prevention", enriched)
        self.assertIn("DB::transaction()", enriched)
        self.assertIn("Proper Indexing", enriched)

        # 4. Contains adversarial testing requirements
        self.assertIn("Adversarial & Edge Case Automated Testing", enriched)
        self.assertIn("Break it to make it unbreakable", enriched)
        self.assertIn("tests/Unit/", enriched)
        self.assertIn("tests/Feature/", enriched)

        # 5. Contains git commit format
        self.assertIn("feat(backend):", enriched)

    def test_frontend_prompt_enrichment_contains_all_seven_recipes(self):
        raw_prompt = "Build public syllabus directory page."
        change_name = "syllabus-hub"
        enriched = agx.enrich_frontend_prompt(raw_prompt, change_name)

        # 1. Contains raw prompt and feature context
        self.assertIn(raw_prompt, enriched)
        self.assertIn("Feature / Module Context: syllabus-hub", enriched)

        # 2. Contains Design System references
        self.assertIn("DESIGN_TOKENS.md", enriched)
        self.assertIn("design-tokens.css", enriched)

        # 3. Contains all 7 Master UI Recipes from ui-refactor.md
        self.assertIn("Recipe 1 (Sharpen Message)", enriched)
        self.assertIn("Recipe 2 (Break Symmetry)", enriched)
        self.assertIn("Recipe 3 (Build Argument)", enriched)
        self.assertIn("Recipe 4 (Pick the Winner)", enriched)
        self.assertIn("Recipe 5 (Scale the Type)", enriched)
        self.assertIn("Recipe 6 (Give Color Meaning)", enriched)
        self.assertIn("Recipe 7 (Add a Signature)", enriched)

        # 4. Contains UI-Mandatory rules
        self.assertIn("UI-Mandatory Compliance", enriched)
        self.assertIn("No placeholder buttons or dead links", enriched)

        # 5. Contains git commit format
        self.assertIn("feat(frontend):", enriched)


if __name__ == "__main__":
    unittest.main()

