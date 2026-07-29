from random import randint
from src.data.data import Dice

def range_checker(table:list[dict], roll) -> dict:
    for r_table in table:
        if r_table["min"] <= roll <= r_table["max"]:
            return r_table["info"]

def dice_roll(dice:Dice)->int:
    return randint(1, dice.value)

def dice_try(dice:Dice, rep:int, verbose:bool=False)->int:
    rolls = [dice_roll(dice) for i in range(rep)]
    result = sum(rolls)
    if verbose:
        return rolls, result
    return result