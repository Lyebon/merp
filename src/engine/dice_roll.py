from random import randint

def dice_roll(dice: int) -> int:
    return randint(1, dice)

def dice_try(dice:int, times:int, record=False)->int |list[int]:
    roll_list = []
    result = 0
    for i in range(0, times):
        roll =dice_roll(dice)
        result += roll
        roll_list.append(roll)
    if record:
        return result, roll_list
    return result