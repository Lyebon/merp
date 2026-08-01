from character.character import Character
from src.enums import Dice, StatsName, Professions, Bonus, AllyRaces, HumanRaces
from character.characteristics import Stat
from src.engine.mechanic import dice_roll, dice_try, range_checker
from src.data_loader import read_file
from pathlib import Path


def good_creator() -> Character:
    race = race_selector()
    profession = profession_selector()
    characteristics = characteristics_setup(profession["primary"], race["characteristics"])

def race_selector() -> dict[str:dict]:
    roll = dice_roll(Dice.d100)
    races = read_file(Path("docs/races/ally_races.json"))
    race = range_checker(races, roll)
    return race

def profession_selector() -> dict[str:dict]:
    roll = dice_roll(Dice.d6)
    profession = list(Professions)[roll-1]
    table = read_file(Path("docs/professions.json"))
    return table[profession.value]

def characteristics_setup(primary, race_banus) -> dict[StatsName:Stat]:
    characteristics = {}
    for name in StatsName:
        stat = {}
        if name.value == primary:
            pass
    return