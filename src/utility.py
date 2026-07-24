from src.engine.dice import Dice_function, Dice

def d100_check(table:list[dict]) -> dict:
    roll = Dice_function.dice_roll(Dice.d100)
    for r_table in table:
        if r_table["min"] <= roll <= r_table["max"]:
            return r_table["info"]