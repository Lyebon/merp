from src.data.data import StatsName, Bonus
from dataclasses import dataclass

@dataclass
class Stat:
    roll:int
    race_bonus:Bonus
    roll_bonus:Bonus
    total:int

@dataclass
class Stats:
    characteristic:dict[StatsName: Stat]

    def characteristic_build(self):
        pass


    def char_set_bonus(self, stat:Stat)->Bonus:
        if stat.roll == 102:
            return Bonus.plus_35
        elif stat.roll == 101:
            return Bonus.plus_30
        elif stat.roll == 100:
            return Bonus.plus_25
        elif 98 <= stat.roll <= 99:
            return Bonus.plus_20
        elif 95 <= stat.roll <= 97:
            return Bonus.plus_15
        elif 90 <= stat.roll <= 94:
            return Bonus.plus_10
        elif 75<= stat.roll <= 89:
            return Bonus.plus_5
        else:
            return Bonus.plus_0


    def bonus_calculation(self, a:Bonus, b:Bonus)->int:
        return a.value + b.value
