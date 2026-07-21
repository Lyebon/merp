from enum import Enum

class Characteristics(Enum):
    strng = "str"
    agi = "agi"
    con = "con"
    inte = "int"
    i = "i"
    pre = "pre"

class Stats_char:
    def __init__(self):
        #armar validador para el diccionario y que no cree objetos vacios -> siguiente paso
        self.strengt = None
        self.agility = None
        self.constitution = None
        self.intelligence = None
        self.intuition = None
        self.precense = None


    def from_dict(self, stats_roll: dict[str:int]):
        for stat, value in stats_roll.items():
            match stat:
                case Characteristics.strng:
                    self.strengt = value
                case Characteristics.agi:
                    self.agility = value
                case Characteristics.con:
                    self.constitution = value
                case Characteristics.inte:
                    self.intelligence = value
                case Characteristics.i:
                    self.intuition = value
                case Characteristics.pre:
                    self.precense = value
                case _:
                    return f"Unexpected stat: {stat}"


class Stats(Stats_char):
    def __init__(self):
        super().__init__()
        self.bonif_strengt = None
        self.bonif_agility = None
        self.bonif_constitution = None
        self.bonif_intelligence = None
        self.bonif_intuition = None
        self.bonif_precense = None

    @staticmethod
    def bonus_char(stat):
        if stat == 102:
            return 35
        elif stat == 101:
            return 30
        elif stat == 100:
            return 25
        elif stat == 99 or stat == 98:
            return 20
        elif 95 <= stat <=97:
            return 15
        elif 90 <= stat <= 94:
            return 10
        elif 75 <= stat <= 89:
            return 5
        else:
            return 0

    def from_dict(self, stats_roll: dict):
        super().from_dict(stats_roll)
        self._calc_all_bonuses()
        return self

    def _calc_all_bonuses(self):
        self.bonif_strengt = self.bonus_char(self.strengt)
        self.bonif_agility = self.bonus_char(self.agility)
        self.bonif_constitution = self.bonus_char(self.constitution)
        self.bonif_intelligence = self.bonus_char(self.intelligence)
        self.bonif_intuition = self.bonus_char(self.intuition)
        self.bonif_precense = self.bonus_char(self.precense)