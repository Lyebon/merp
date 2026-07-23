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
        self.dice_list = []

    @staticmethod
    def dice_roll(dice: Dice) -> int:
        return randint(1, dice.value)
    
    def dice_try(self, dice: Dice, num: int, all: bool) -> int:
        self.result = 0
        self.dice_list = []
        for i in range(0, num):
            throw = self.dice_roll(dice)
            self.result += throw
            self.dice_list.append(throw)
        if all == True:
            return self.dice_list
        return self.result