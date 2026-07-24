from src.data_loader import read_file
from src.utility import d100_check
from src.engine.characteristics import RaceStats
from pathlib import Path

class Race:
    def __init__(self):
        self.race = None

    def good_creator(self):
        table = read_file(Path('./docs/races/good_races.json'))
        hum_table = read_file(Path('./docs/races/human_races.json'))
        race_mod = d100_check(table)    # race is a dictionary with all the pertinent data about char, ability and else
        if race_mod == "human":
            race_mod = d100_check(hum_table)
        self.race = race_mod.get("race")
        bonus_char = race_mod.get("characteristics") # Push to characteristic module
        RaceStats.race_bonus(bonus_char)
