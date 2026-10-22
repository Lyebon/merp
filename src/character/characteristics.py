class Characteristic:
    def __init__(self, roll:int , race_bonus:int, table:list[list[int]]):
        self.stat: int = roll
        self.race_bonus: int = race_bonus
        self.roll_bonus: int = self.roll_bonuses(table)
        self.total_bonus:int = self.sum()

    def roll_bonuses(self, table:list[list[int]]) -> int:
        for min, max, bonus in table:
            if min <= self.stat <= max:
                return bonus

    def sum(self) -> int:
        return self.roll_bonus + self.race_bonus

    def __repr__(self):
        return (f"Roll: {self.stat}\nRace Bonus: {self.race_bonus}\nRoll Bonus: {self.roll_bonus}\nTotal Bonus:{self.total_bonus}")