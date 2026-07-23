from dice import Dice_function, Dice
from enum import Enum

class Stats(Enum):
    strength = "strength"
    agility = "agility"
    constitution = "constitution"
    intelligence = "intelligence"
    intuition = "intuition"
    presence = "presence"



class Characteristics:
    def __init__(self):
        self.char_roll = {Stats.strength: None, Stats.agility: None, Stats.constitution: None,
                          Stats.intelligence: None, Stats.intuition: None, Stats.presence: None}
        
        self.r_bonus = {Stats.strength: None, Stats.agility: None, Stats.constitution: None,
                          Stats.intelligence: None, Stats.intuition: None, Stats.presence: None}
        
        self.char_roll_bonus = {Stats.strength: None, Stats.agility: None, Stats.constitution: None,
                                Stats.intelligence: None, Stats.intuition: None, Stats.presence: None}
        self.char_try()
        self.bonus = {Stats.strength: None, Stats.agility: None, Stats.constitution: None,
                     Stats.intelligence: None, Stats.intuition: None, Stats.presence: None}



    def char_try(self):
        for char in self.char_roll:
            roll = 0
            while roll< 25:
                roll = Dice_function.dice_roll(Dice.d100)
            self.char_roll[char] = roll
            self.char_set_bonus(char, roll)


    def race_bonus(self, table:dict):
        for bonus in self.race_bonus:
            self.race_bonus[bonus] = table[bonus.value]
            if self.race_bonus[bonus] == None:
                return f"The characteristic name {table.key} is invalid or empty"

    def char_set_bonus(self, stat, roll):
        if roll == 102:
            self.char_roll_bonus[stat] = 35
        elif roll == 101:
            self.char_roll_bonus[stat] = 30
        elif roll == 100:
            self.char_roll_bonus[stat] = 25
        elif 98 <= roll <=99:
            self.char_roll_bonus[stat] = 20
        elif 95 <= roll <=97:
            self.char_roll_bonus[stat] = 15
        elif 90 <= roll <=94:
            self.char_roll_bonus[stat] = 10
        elif 75 <= roll <=89:
            self.char_roll_bonus[stat] = 5
        else:
            self.char_roll_bonus[stat] = 0

    def bonus_calculation(self):
        for stat in Stats:
            a = self.char_roll_bonus.get(stat)
            b = self.r_bonus.get(stat)
            self.bonus[stat] = a+b