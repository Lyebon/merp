import unittest
from src.data.data_loader import Manuals
from src.char_struct.validator import CharName
from src.char_struct.skills import Skill

class TestSkills(unittest.TestCase):
    
    def test_skills_creator(self):
        manual = Manuals()
        skill = Skill("sin_armadura", 1, CharName.AGILITY, manual.bonuses_search("skills"))

        self.assertIsInstance(skill, Skill)

if __name__ == "__main__":
    unittest.main()