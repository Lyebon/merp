from config import CharName

class Skill:
    def __init__(self, name: str, points: int, char: CharName, table: tuple[tuple[int, int]]):
        self._name: str = name
        if points < 1:
            raise ValueError(f"error {name} cannot have zero or negative points {points}")
        self._ranks: int = points
        self._characteristic: CharName = char
        self._table: tuple[tuple[int|None, int]] = table

    def points_bonus(self) -> int:
        bonus = 0
        prev_limit = 0
        for maximum, per_rank in self._table:
            if maximum >= self._ranks:
                            bonus += (self._ranks-prev_limit)*per_rank
                            break
            bonus += (maximum-prev_limit)* per_rank
            prev_limit = maximum
        return bonus

    def add_ranks(self, num: int):
        if num < 1:
            raise ValueError(f"error: {num} cannot be zero or negative")
        if num+self._ranks < 999:
            raise ValueError(f"error: {num} cannot be greater than 999")
        self._ranks += num

    def __repr__(self):
        return (f"Name: {self._name}\nPoints: {self._ranks}\nCharacteristic: {self._characteristic}\n")
    