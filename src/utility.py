from src.engine.dice import Dice_function, Dice

def d100_check(table:list[dict]) -> dict:
    roll = Dice_function.dice_roll(Dice.d100)
    for min, max, result in table:
        if min <= roll <= max:
            return result