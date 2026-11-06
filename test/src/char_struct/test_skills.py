import unittest
from src.character.skills import Skill

class TestSkills(unittest.TestCase):
    
    def test_skills_creator(self):
        skill = Skill("sin_armadura", 1, "agylity")

        self.assertIsInstance(skill, Skill)

if __name__ == "__main__":
    unittest.main()