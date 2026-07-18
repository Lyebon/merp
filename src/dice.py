from random import randint
from enum import Enum

class Dice(Enum):
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100

class Dice_function:
    def __init__(self):
        self.result = 0

    @staticmethod
    def dice_roll(dice: Dice) -> int:
        return randint(1, dice.value)
    
    def dice_try(self, dice: Dice, num: int) -> int:
        self.result = 0
        for i in range(0, num):
            self.result += self.dice_roll(dice.value)
        return self.result