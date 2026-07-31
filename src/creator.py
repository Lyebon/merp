from src.data.character import Character
from src.data.data import Dice, StatsName, Professions, Bonus, AllyRaces, HumanRaces
from src.engine.characteristics import Stat
from src.engine.mechanic import dice_roll, dice_try, range_checker
from src.data_loader import read_file
from pathlib import Path


def good_creator() -> Character:
    pass    

def race_selector() -> dict[str:dict]:
    select = "random"
    if select == "random":
        roll = dice_roll(Dice.d100)
        races = read_file(Path("docs/races/ally_races.json"))
        race = range_checker(races, roll)
        return race
    