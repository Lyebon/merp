class Characteristic:
    def __init__(self, roll, race_bonus, table):
        self.stat: int = roll
        self.race_bonus: int = race_bonus
        self.roll_bonus: int = self.roll_bonuses(table)
        self.total_bonus:int = self.sum()

    def roll_bonuses(self, table) -> int:
        table_roll = table.get("characteristics")
        if table_roll == None:
            print("failed")
        for min, max, bonus in table_roll:
            if min <= self.stat <= max:
                return bonus

    def sum(self) -> int:
        return self.roll_bonus + self.race_bonus

    def __repr__(self):
        return (f"Roll: {self.stat}\nRace Bonus: {self.race_bonus}\nRoll Bonus: {self.roll_bonus}\nTotal Bonus:{self.total_bonus}")