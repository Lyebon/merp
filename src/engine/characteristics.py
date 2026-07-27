from src.engine.mechanic import StatsName, Bonus
from dataclasses import dataclass
from src.engine.mechanic import d100_roll

@dataclass
class Stat:
    roll:int
    race_bonus:Bonus
    roll_bonus:Bonus = 0
    total=int

@dataclass
class Stats:
    characteristic:dict[StatsName: Stat]

    def characteristic_build(self, primary:StatsName, race_bon:dict[str:int]):
        char = {}
        for stat in StatsName:
            info = Stat()
            race = race_bon[stat.value]
            if stat.value == primary:
                info.roll = 90
                info.race_bonus = Bonus(race)
                info.roll_bonus = self.char_set_bonus(info)
                char[stat] = info
            else:
                info.roll = d100_roll()
                info.race_bonus = Bonus(race)
                info.roll_bonus = self.char_set_bonus(info)
                info.total = self.bonus_calculation(info.race_bonus,info.roll_bonus)
                char[stat] = info
        self.characteristic = char


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
