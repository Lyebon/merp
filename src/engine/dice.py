from random import randint

class Dice_function:
    def __init__(self):
        self.result = 0
        self.dice_list = []

    @staticmethod
    def dice_roll(dice: int) -> int:
        return randint(1, dice)
    
    def dice_try(self, dice: int, num: int, all=False) -> int | list[int]:
        self.result = 0
        self.dice_list = []
        for i in range(0, num):
            throw = self.dice_roll(dice)
            self.result += throw
            self.dice_list.append(throw)
        if all == True:
            return self.dice_list
        return self.result