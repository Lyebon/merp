from src.engine.dice import Dice_function, Dice
from dataclasses import dataclass
from enum import Enum

class Stats_name(Enum):
    strength = "strength"
    agility = "agility"
    constitution = "constitution"
    intelligence = "intelligence"
    intuition = "intuition"
    presence = "presence"



class Stats:
    def __init__(self):
        self.char_try()
        self.bon_strength = None
        self.bon_agility = None
        self.bon_constitution = None
        self.bon_intelligence = None
        self.bon_intuition = None
        self.bon_presence = None

    def char_try(self):
        for stat in Stats_name:
            roll = 0
            while roll< 25:
                roll = Dice_function.dice_roll(Dice.d100)
            self.char_roll[stat] = roll
            self.char_set_bonus(stat, roll)

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

@dataclass
class Characteristics(Stats):
    def __init__(self):
        super().__init__()
        self.strength = None
        self.agility = None
        self.constitution = None
        self.intelligence = None
        self.intuition = None
        self.presence = None

@dataclass
class RaceStats(Stats):
    def __init__(self):
        super().__init__()
        self.r_strength = None
        self.r_agility = None
        self.r_constitution = None
        self.r_intelligence = None
        self.r_intuition = None
        self.r_presence = None
    

    def race_bonus(self, table:dict):
        self.r_strenght = table["strenght"]
        self.r_agility = table["agility"]
        self.r_constitution = table["constitution"]
        self.r_intelligence = table["intelligence"]
        self.r_intuition = table["intuition"]
        self.r_presence = table["presence"]