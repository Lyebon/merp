import unittest
from src.engine.mechanic import dice_roll
from character.characteristics import Stat
from src.enums import StatsName, Dice, Bonus
from engine.random_creator import race_selector, profession_selector

class TestCharacteristics(unittest.TestCase):
    def test_stat_creator(self):
        pj = {}
        race = [Bonus.plus_5,Bonus.plus_0,Bonus.plus_0,Bonus.plus_0,Bonus.plus_0,Bonus.plus_0]
        caracteristics= [Stat(dice_roll(Dice.d100), race[x]) for x in range(6)]
        char_name = list(StatsName)
        for i in range(6):
            pj[char_name[i]] = caracteristics[i]
        new_pj = pj

        self.assertIsInstance(new_pj, dict)

    def test_race_selector_ran(self):
        race = race_selector(1)

        self.assertIsInstance(race, dict)

    def test_profession_selector_ran(self):
        profession = profession_selector(1)

        self.assertIsInstance(profession, dict)

    