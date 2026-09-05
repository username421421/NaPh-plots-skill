from pathlib import Path
import re
import unittest


SKILL_ROOT = Path(__file__).resolve().parents[1]


class LumericalFdtdSkillWorkflowTest(unittest.TestCase):
    def test_skill_reference_routes_resolve(self):
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        routes = re.findall(r"`(references/[^`<>]+\.md)`", skill)
        self.assertTrue(routes, "Entrypoint must expose package guidance")
        for route in routes:
            with self.subTest(route=route):
                target = SKILL_ROOT / route
                self.assertTrue(target.is_file(), f"Broken route: {route}")
                self.assertTrue(target.read_text(encoding="utf-8").strip())

    def test_skill_exposes_api_and_physics_guidance(self):
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("references/pylumerical.md", skill)
        self.assertIn("references/python-api.md", skill)
        self.assertIn("references/mesh.md", skill)
        self.assertIn("references/sources.md", skill)
        self.assertIn("references/monitors-results.md", skill)
        self.assertIn("references/api-audit.md", skill)
        self.assertIn("references/convergence-checklist.md", skill)

    def test_pylumerical_reference_exists_and_is_actionable(self):
        reference = (SKILL_ROOT / "references" / "pylumerical.md").read_text(encoding="utf-8")

        required_phrases = [
            "ansys-lumerical-core",
            "ansys.lumerical.core",
            "LUMERICAL_HOME",
            "serverArgs",
            "OrderedDict",
            "SimObject",
            "getresult",
            "getdata",
            "lumopt2",
            "Basic FDTD Simulation - Python style commands",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, reference)


if __name__ == "__main__":
    unittest.main()
