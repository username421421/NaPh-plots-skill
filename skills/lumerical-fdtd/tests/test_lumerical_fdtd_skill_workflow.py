from pathlib import Path
import unittest


SKILL_ROOT = Path(__file__).resolve().parents[1]


class LumericalFdtdSkillWorkflowTest(unittest.TestCase):
    def test_skill_requires_local_research_before_coding(self):
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        required_phrases = [
            "Before writing code",
            "Search Similar Local Examples",
            "Function And Argument Audit",
            "Implementation Notes Before Coding",
            "Do not write or modify simulation code until",
            "references/examples-and-commands.md",
            "references/pylumerical.md",
            "references/corpus-index.md",
            "references/keyword-index.md",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, skill)

    def test_skill_routes_to_local_reference_files_not_web_first(self):
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Use local files first", skill)
        self.assertIn("references/pylumerical.md", skill)
        self.assertIn("references/python-api.md", skill)
        self.assertIn("references/mesh.md", skill)
        self.assertIn("references/sources.md", skill)
        self.assertIn("references/monitors-results.md", skill)
        self.assertNotIn("browse the web first", skill.lower())

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
