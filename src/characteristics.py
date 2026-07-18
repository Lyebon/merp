from enum import Enum

class Characteristics(Enum):
    strengt = "str"
    agility = "agi"
    constitution = "con"
    intelligence = "int"
    intuition = "i"
    precense = "pre"

class Stats_char():
    def __init__(self):
        self.strengt = None
        self.agility = None
        self.constitution = None
        self.intelligence = None
        self.intuition = None
        self.precense = None

    
    @staticmethod
    def from_dict(self, stats_roll):
        for stat in stats_roll:
            if stats_roll[stat] == None:
                return f"The {stat} is empty"
            match stat:
                case "str":
                    self.strengt = stats_roll[stat]
                case "agi":
                    self.agility = stats_roll[stat]
                case "con":
                    self.constitution = stats_roll[stat]
                case "int":
                    self.intelligence = stats_roll[stat]
                case "i":
                    self.intuition = stats_roll[stat]
                case "pre":
                    self.precense = stats_roll[stat]
                case _:
                    return "The caracteristics have wrong or extra data!"