import unittest
from src.data.data_loader import Manuals
from src.char_struct.validator import CharName
from src.char_struct.characteristics import Characteristic
from src.constructor.char_builder import characteristics_creator


class TestSkills(unittest.TestCase):

    def test_characteristics_creator(self):
        roll = {
            CharName.STRENGTH: 95,
            CharName.AGILITY: 90,
            CharName.CONSTITUTION: 75,
            CharName.INTELLIGENCE: 80,
            CharName.INTUITION: 98,
            CharName.PRESENCE: 100,
        }
        race_bonus = {
            CharName.STRENGTH:5, CharName.AGILITY:-5,
            CharName.CONSTITUTION:15, CharName.INTELLIGENCE:0,
            CharName.INTUITION:-5, CharName.PRESENCE:-5
        }

        result = characteristics_creator(roll, race_bonus, Manuals())
        strength = result[CharName.STRENGTH]
        agility = result[CharName.AGILITY]
        constitution = result[CharName.CONSTITUTION]
        intelligence = result[CharName.INTELLIGENCE]
        intuition = result[CharName.INTUITION]
        presence = result[CharName.PRESENCE]
        
        self.assertIsInstance(result, dict)
        self.assertEqual(strength.roll_bonuses(), 15)
        self.assertEqual(strength.total_bonus(), 20)
        self.assertEqual(agility.roll_bonuses(), 10)
        self.assertEqual(agility.total_bonus(), 5)
        self.assertEqual(constitution.roll_bonuses(), 5)
        self.assertEqual(constitution.total_bonus(), 20)
        self.assertEqual(intelligence.roll_bonuses(), 5)
        self.assertEqual(intelligence.total_bonus(), 5)
        self.assertEqual(intuition.roll_bonuses(), 20)
        self.assertEqual(intuition.total_bonus(), 15)
        self.assertEqual(presence.roll_bonuses(), 25)
        self.assertEqual(presence.total_bonus(), 20)

if __name__ == "__main__":
    unittest.main()