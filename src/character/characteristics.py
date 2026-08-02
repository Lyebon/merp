from src.enums import Bonus
from dataclasses import dataclass

@dataclass
class Stat:
    roll:int
    race_bonus:Bonus
    roll_bonus:Bonus
    total:int

    @classmethod
    def from_dict(cls, base:dict[str:int|Bonus])-> None:
        cls.roll = base.get("roll")
        cls.race_bonus = base.get("race")
        cls.roll_bonus = cls.char_set_bonus(cls)
        cls.total = cls.bonus_calculation(cls)
        return cls

    def char_set_bonus(self)->Bonus:
        if self.roll == 102:
            return Bonus.PLUS_35
        elif self.roll == 101:
            return Bonus.PLUS_30
        elif self.roll == 100:
            return Bonus.PLUS_25
        elif 98 <= self.roll <= 99:
            return Bonus.PLUS_20
        elif 95 <= self.roll <= 97:
            return Bonus.PLUS_15
        elif 90 <= self.roll <= 94:
            return Bonus.PLUS_10
        elif 75<= self.roll <= 89:
            return Bonus.PLUS_5
        else:
            return Bonus.CERO

    def bonus_calculation(self)->int:
        return self.race_bonus.value + self.roll_bonus.value