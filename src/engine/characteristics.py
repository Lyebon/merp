from src.utility import Stats_name, Bonus
from dataclasses import dataclass

@dataclass
class Stat:
    roll:int
    bonus:int
    r_bonus:int = 0

@dataclass
class Stats:
    characteristic:dict[Stats_name: Stat]

    def characteristic_build(self):
        pass

    def char_set_bonus(self):
        pass
    
    def bonus_calculation(self):
        pass


