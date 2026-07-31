from enum import Enum

class Dice(Enum):
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100

class AllyRaces(Enum):
    hobbit = "hobbit"
    umly = "umly"
    dwarf = "dwarf"
    wose = "wose"
    human = "human"
    half_elf = "half elf"
    silvano = "silvano"
    sindar = "sindar"
    noldor = "noldor"

class HumanRaces(Enum):
    dunedain = "dunedain"
    rohirrim = "rohirrim"
    beornida = "beornida"
    woodmen = "woodmen"
    dorwinadan = "dorwinadan"
    lossadan = "lossadan"
    eriadorians = "eriadorians"
    bourgeois = "bourgeois"
    dunlendino = "dunlendino"
    easterlings = "easterlings"
    haradan = "haradan"
    corsair = "corsair"
    variag = "variag"
    black_numenoreans = "black numenoreans"

class Professions(Enum):
    warrior = "warrior"
    scout = "scout"
    ranger = "ranger"
    mage = "mage"
    animist = "animist"
    bard = "bard"


class StatsName(Enum):
    strength = "strength"
    agility = "agility"
    constitution = "constitution"
    intelligence = "intelligence"
    intuition = "intuition"
    presence = "presence"

class Bonus(Enum):
    plus_35 = 35
    plus_30 = 30
    plus_25 = 25
    plus_20 = 20
    plus_15 = 15
    plus_10 = 10
    plus_5 = 5
    plus_2 = 2
    plus_1 = 1
    plus_0 = 0