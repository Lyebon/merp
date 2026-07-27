from src.engine.mechanic import StatsName, Bonus
from dataclasses import dataclass
from src.engine.mechanic import d100_roll

@dataclass
class Stat:
    roll:int
    race_bonus:int
    r_bonus:int = 0

@dataclass
class Stats:
    characteristic:dict[StatsName: Stat]

    def characteristic_build(self, primary, race_bon):
        char = {}
        for stat in StatsName:
            info = Stat()
            if stat.value == primary:
                info.roll = 90
                info.race_bonus = self.char_set_bonus(race_bon)
                char[stat] = info
            else:
                info.roll = d100_roll()
                char[stat] = info
        self.characteristic = char


    def char_set_bonus(self):
        pass
    
    def bonus_calculation(self):
        pass


