from enum import Enum

class Dice(Enum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20
    D100 = 100

class AllyRaces(Enum):
    HOBBIT = "hobbit"
    UMLY = "umly"
    DWARF = "dwarf"
    WOSE = "wose"
    HUMAN = "human"
    HALF_ELF = "half elf"
    SILVANO = "silvano"
    SINDAR = "sindar"
    NOLDOR = "noldor"

class HumanRaces(Enum):
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
    BLACK_NUMENOREANS = "black numenoreans"

class Professions(Enum):
    WARRIOR = "warrior"
    SCOUT = "scout"
    RANGER = "ranger"
    MAGE = "mage"
    ANIMIST = "animist"
    BARD = "bard"


class StatsName(Enum):
    STRENGTH = "strength"
    AGILITY = "agility"
    CONSTITUTION = "constitution"
    INTELLIGENCE = "intelligence"
    INTUITION = "intuition"
    PRESENCE = "presence"

class Bonus(Enum):
    PLUS_35 = 35
    PLUS_30 = 30
    PLUS_25 = 25
    PLUS_20 = 20
    PLUS_15 = 15
    PLUS_10 = 10
    PLUS_5 = 5
    PLUS_2 = 2
    PLUS_1 = 1
    ZERO = 0
    MINUS_5 = -5
    MINUS_10 = -10
    MINUS_15 = -15
    MINUS_20 = -20