from src.data_loader import read_file
from src.utility import d100_check
from src.engine.characteristics import RaceStats
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Race:
    race:str
    bonus_char:dict
    adolecence:dict
    magic_mod:dict


    def good_creator(self):
        table = read_file(Path('./docs/races/good_races.json'))
        hum_table = read_file(Path('./docs/races/human_races.json'))
        race_mod = d100_check(table)    # race is a dictionary with all the pertinent data about char, ability and else
        if race_mod == "human":
            race_mod = d100_check(hum_table)
        self.race = race_mod.get("race")
        self.bonus_char = race_mod.get("characteristics") # Push to characteristic module
        # self.adolecence = race_mod.get("ability")
        # self.magic_mod = race_mod.get("magic_tr")
