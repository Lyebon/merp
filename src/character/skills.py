from config import CharName, FIRST_SKILL_RANK, SECOND_SKILL_RANK

class Skill:
    def __init__(self, name: str, points: int, char: CharName):
        self._name: str = name
        if points < 1:
            raise ValueError(f"error {name} cannot have zero or negative points {points}")
        self._ranks: int = points
        self._characteristic: CharName = char

    def points_bonus(self) -> int:
        if self._ranks <= FIRST_SKILL_RANK:
            return self._ranks * 5
        elif self._ranks <= SECOND_SKILL_RANK:
            return ((self._ranks - FIRST_SKILL_RANK) * 2) + 50
        else:
            return (self._ranks - SECOND_SKILL_RANK) + 60 

    def add_ranks(self, num: int):
        if num < 1:
            raise ValueError(f"error: {num} cannot be zero or negative")
        self._ranks += num

    def __repr__(self):
        return (f"Name: {self._name}\nPoints: {self._ranks}\nCharacteristic: {self._characteristic}\n")
    