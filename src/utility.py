from src.engine.dice import Dice_function
from enum import Enum

class Dice(Enum):
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100

class Stats_name(Enum):
    strength = "strength"
    agility = "agility"
    constitution = "constitution"
    intelligence = "intelligence"
    intuition = "intuition"
    presence = "presence"

class Bonus(Enum):
    plus_35 = 35

def d100_check(table:list[dict]) -> dict:
    roll = Dice_function.dice_roll(Dice.d100.value)
    for r_table in table:
        if r_table["min"] <= roll <= r_table["max"]:
            return r_table["info"]

