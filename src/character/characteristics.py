from src.enums import StatsName, Bonus


class Stat:
    def __init__(self, roll, race_bonus):
        self.roll:int = roll
        self.race_bonus:Bonus = race_bonus
        self.roll_bonus:Bonus = self.char_set_bonus()
        self.total:int = self.bonus_calculation()


    def char_set_bonus(self)->Bonus:
        if self.roll == 102:
            return Bonus.plus_35
        elif self.roll == 101:
            return Bonus.plus_30
        elif self.roll == 100:
            return Bonus.plus_25
        elif 98 <= self.roll <= 99:
            return Bonus.plus_20
        elif 95 <= self.roll <= 97:
            return Bonus.plus_15
        elif 90 <= self.roll <= 94:
            return Bonus.plus_10
        elif 75<= self.roll <= 89:
            return Bonus.plus_5
        else:
            return Bonus.plus_0

    def bonus_calculation(self)->int:
        return self.race_bonus.value + self.roll_bonus.value

    def __repr__(self):
       return f"\nroll: {self.roll}\nRoll bonus: {self.roll_bonus.value}\nRace bonus: {self.race_bonus.value}\nTotal bonus: {self.total}\n"