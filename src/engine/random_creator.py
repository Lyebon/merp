from src.character.character import Character
from src.enums import Dice, StatsName, Professions, Bonus
from src.character.characteristics import Stat
from src.engine.mechanic import dice_roll, range_checker
from src.data_loader import read_file
from pathlib import Path


def good_creator() -> Character:
    character = {}
    pass
    


def race_selector() -> dict[str:dict]:
    roll = dice_roll(Dice.D100)
    races = read_file(Path("src/data/races/ally_races.json"))
    race = range_checker(races, roll)
    if races == "human":
        roll = dice_roll(Dice.D100)
        races = read_file(Path("src/data/races/human_races.json"))
        race = range_checker(races, roll)
    return race

def profession_selector() -> dict[Professions:dict]:
    roll = dice_roll(Dice.D6)
    profession = list(Professions)[roll-1]
    table = read_file(Path("src/data/professions.json"))
    return {profession:table[profession.value]}

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