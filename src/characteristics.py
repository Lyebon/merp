from enum import Enum

class Characteristics(Enum):
    strng = "str"
    agi = "agi"
    con = "con"
    int = "int"
    i = "i"
    pre = "pre"

class Bonif(Enum):
    plus35 = 35
    plus30 = 30
    plus25 = 25
    plus20 = 20
    plus15 = 15
    plus10 = 10
    plus5 = 5
    plus0 = 0


class Stats_char():
    def __init__(self):
        self.strengt = None
        self.agility = None
        self.constitution = None
        self.intelligence = None
        self.intuition = None
        self.precense = None

        self.bonif_strengt = None
        self.bonif_agility = None
        self.bonif_constitution = None
        self.bonif_intelligence = None
        self.bonif_intuition = None
        self.bonif_precense = None

    
    def from_dict(self, stats_roll: dict[str:int]):
        for stat, value in stats_roll.items():
            if value == None:
                return f"The {stat} is empty"
            match stat:
                case Characteristics.strng:
                    self.strengt = value
                case Characteristics.agi:
                    self.agility = value
                case Characteristics.con:
                    self.constitution = value
                case Characteristics.int:
                    self.intelligence = value
                case Characteristics.i:
                    self.intuition = value
                case Characteristics.pre:
                    self.precense = value
                case _:
                    return f"Unexpected stat: {stat}"
                