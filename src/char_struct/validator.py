from enum import Enum

class CharName(Enum):
    STRENGTH = "strength"
    AGILITY = "agility"
    CONSTITUTION = "constitution"
    INTELLIGENCE = "intelligence"
    INTUITION = "intuition"
    PRESENCE = "presence"


from enum import Enum

class RaceAlly(str, Enum):
    HOBBIT = "hobbit"
    UMLY = "umly"
    DWARF = "dwarf"
    WOSE = "wose"
    HUMAN = "human"
    HALF_ELF = "half_elf"
    SILVANO = "silvano"
    SINDAR = "sindar"
    NOLDOR = "noldor"


class RaceHuman(str, Enum):
    DUNEDAIN = "dunedain"
    ROHIRRIM = "rohirrim"
    BEORNIDA = "beornida"
    WOODMEN = "woodmen"
    DORWINADAN = "dorwinadan"
    LOSSADAN = "lossadan"
    ERIADORIANS = "eriadorians"
    BOURGEOIS = "bourgeois"
    DUNLENDINO = "dunlendino"
    EASTERLINGS = "easterlings"
    HARADAN = "haradan"
    CORSAIR = "corsair"
    VARIAG = "variag"
    BLACK_NUMENOREANS = "black_numenoreans"
