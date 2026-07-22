from src.data_loader import read_file
from src.engine.dice import Dice_function, Dice
from utility import table_check

class Race:
    def __init__(self):
        self.race = None

    def good_creator(self):
        table = read_file("./docs/races/good_races.json")
        roll = Dice_function.dice_roll(Dice.d100)
        for part in table:
            race = table_check(part, roll)
