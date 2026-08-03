from src.character.character import Character
from src.enums import Dice, StatsName, Professions, Bonus, AllyRaces, HumanRaces
from src.character.characteristics import Stat
from src.engine.mechanic import dice_roll, range_checker
from src.data_loader import read_file
from pathlib import Path


def good_creator() -> Character:
    pass

def race_selector():
    file = read_file(Path("/src/data/races/ally_races.json"))
    race = range_checker(file, dice_roll(Dice.D100))
    if race.get("race") == "human":
        file = read_file(Path("/src/data/races/human_races.json"))
        race = range_checker(file, dice_roll(Dice.D100))
        


def profession_selector() -> dict[Professions:dict]:
    pass

def characteristics_setup(primary:str, race_bonus:dict[StatsName:Bonus]) -> dict[StatsName:Stat]:
    characteristics = {}
    for name in StatsName:
        stat = {}
        if name == primary:
            stat["roll"] = 90
            stat["race"] = race_bonus.get(name)
        else:
            stat["roll"] = dice_roll(Dice.D100)
            stat["race"] = race_bonus.get(name)
        characteristics[name] = Stat.from_dict(stat)
    return characteristics