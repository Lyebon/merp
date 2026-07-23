from src.data_loader import read_file
from utility import d100_check
from src.engine.characteristics import Characteristics

class Race:
    def __init__(self):
        self.race = None

    def good_creator(self):
        table = read_file("./docs/races/good_races.json")
        hum_table = read_file("./docs/races/human_races.json")
        race_mod = d100_check(table)    # race is a dictionary with all the pertinent data about char, ability and else
        if race_mod.get("race") == "human":
            race_mod = d100_check(hum_table)
        self.race = race_mod.get("race")
        bonus_char = race_mod.get("characteristics") # Push to characteristic module
        Characteristics.race_bonus(bonus_char)
