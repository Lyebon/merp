from src.engine.dice_roll import dice_roll
from enum import Enum

class Dice(Enum):
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100

class StatsName(Enum):
    strength = "strength"
    agility = "agility"
    constitution = "constitution"
    intelligence = "intelligence"
    intuition = "intuition"
    presence = "presence"

class Bonus(Enum):
    plus_35 = 35
    plus_30 = 30
    plus_25 = 25
    plus_20 = 20
    plus_15 = 15
    plus_10 = 10
    plus_5 = 5
    plus_2 = 2
    plus_1 = 1
    plus_0 = 0

def d100_check(table:list[dict], roll) -> dict:
    for r_table in table:
        if r_table["min"] <= roll <= r_table["max"]:
            return r_table["info"]

def d100_roll()->int:
    return dice_roll(Dice.d100)

def d6_roll()->int:
    return dice_roll(Dice.d6)