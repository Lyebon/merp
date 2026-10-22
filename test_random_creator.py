import unittest
from src.character.characteristics import Characteristic
from src.character.skills import Skill
from random import randint

def dice(dice:int)->int:
    return randint(1,dice)



class TestCharacteristic(unittest.TestCase):
    def test_characteristic_creation(self):
        bonus = [
            [1, 74, 0],[75, 89, 5], [90, 94, 10],
            [95, 97, 15], [98,99,20], [100,100,25],
            [101,101,30], [102,102,35]
            ]
        race_bonus = 10
        characteristic = Characteristic(dice(100),race_bonus, bonus)

        self.assertIsInstance(characteristic, Characteristic)
        print(repr(characteristic))
        print()

    def test_skills_creator(self):
        skill = Skill("sin_armadura", 1, "agylity")

        self.assertIsInstance(skill, Skill)
        print(repr(skill))

if __name__ == "__main__":
    unittest.main()