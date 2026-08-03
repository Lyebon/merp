import unittest
from src.engine.random_creator import race_selector, profession_selector, characteristics_setup, good_creator
from src.character.character import Character
from src.enums import Bonus, StatsName, AllyRaces, HumanRaces

class TestCharacterCreator(unittest.TestCase):
    def test_race_selector_ran(self):
        race = race_selector()

        print(race)
        self.assertIsInstance(race, dict)
        self.assertIsInstance(race["race"], AllyRaces|HumanRaces)

    def test_profession_selector_ran(self):
        profession = profession_selector()

        self.assertIsInstance(profession, dict)

    def test_stat_creator(self):
        race_bon = {StatsName.STRENGTH:Bonus.PLUS_5, StatsName.AGILITY:Bonus.MINUS_5, StatsName.CONSTITUTION:Bonus.PLUS_15,
                    StatsName.INTELLIGENCE:Bonus.CERO, StatsName.INTUITION:Bonus.MINUS_5, StatsName.PRESENCE:Bonus.MINUS_5}
        stats = characteristics_setup("strength", race_bon)

        self.assertIsInstance(stats, dict)


    # def test_good_creator(self):
    #     pj = good_creator()

    #     print(pj)

    #     self.assertIsInstance(pj, Character)