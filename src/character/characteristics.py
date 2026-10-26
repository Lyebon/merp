from src.config import LOW_ROLL, HIGH_ROLL

class Characteristic:
    def __init__(self, roll:int , race_bonus:int, table:tuple[tuple[int, int, int],...]):
        if LOW_ROLL > roll or roll > HIGH_ROLL:
            raise ValueError(f"Invalid roll value: {roll} is out of range")
        self._roll: int = roll
        self._race_bonus: int = race_bonus
        self._table:tuple[tuple[int, int, int],...] = table

    def roll_bonuses(self) -> int:
        for minimum, maximum, bonus in self._table:
            if minimum <= self._roll <= maximum:
                return bonus
        raise ValueError(f"No bonus was encountered for the {self._roll} roll")

    def total_bonus(self) -> int:
        return self.roll_bonuses() + self._race_bonus

    @property
    def roll(self) -> int:
        return self._roll

    @property
    def race_bonus(self) -> int:
        return self._race_bonus
    
    def __repr__(self):
        return (f"Characteristic(roll={self._roll}, race_bonus={self._race_bonus})")