from enum import Enum

class Characteristics(Enum):
    strng = "str"
    agi = "agi"
    con = "con"
    inte = "int"
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

class Stats_char:
    def __init__(self):
        #armar validador para el diccionario y que no cree objetos vacios
        self._strengt = None
        self._agility = None
        self._constitution = None
        self._intelligence = None
        self._intuition = None
        self._precense = None


    def from_dict(self, stats_roll: dict[str:int]):
        for stat, value in stats_roll.items():
            if value == None:
                return f"The {stat} is empty"
            match stat:
                case Characteristics.strng:
                    self._strengt = value
                case Characteristics.agi:
                    self._agility = value
                case Characteristics.con:
                    self._constitution = value
                case Characteristics.inte:
                    self._intelligence = value
                case Characteristics.i:
                    self._intuition = value
                case Characteristics.pre:
                    self._precense = value
                case _:
                    return f"Unexpected stat: {stat}"


class Stats_bonif(Stats_char):
    def __init__(self):
        super().__init__()
        self._bonif_strengt = None
        self._bonif_agility = None
        self._bonif_constitution = None
        self._bonif_intelligence = None
        self._bonif_intuition = None
        self._bonif_precense = None

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
        self._bonif_strengt = self.bonus_char(self._strengt)
        self._bonif_agility = self.bonus_char(self._agility)
        self._bonif_constitution = self.bonus_char(self._constitution)
        self._bonif_intelligence = self.bonus_char(self._intelligence)
        self._bonif_intuition = self.bonus_char(self._intuition)
        self._bonif_precense = self.bonus_char(self._precense)