class Skill:
    def __init__(self, name, points, char):
        self.name: str = name
        self.assigned_points: int = points
        self.characteristic: str = char
        self.bonus: int = self.bonus_calculator()

    def bonus_calculator(self):
        if self.assigned_points <= 10:
            return self.assigned_points * 5
        elif self.assigned_points <= 15:
            return ((self.assigned_points - 10) * 2) + 50
        else:
            return (self.assigned_points - 15) + 60 

    def __repr__(self):
        return (f"Name: {self.name}\nPoints: {self.assigned_points}\nCharacteristic: {self.characteristic}\nBonus: {self.bonus}")