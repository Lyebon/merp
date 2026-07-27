from enum import Enum
from dataclasses import dataclass
from src.engine.dice_roll import dice_roll
from src.engine.mechanic import Dice, StatsName
from src.data_loader import read_file
from pathlib import Path

class Professions(Enum):
    warrior = "warrior"
    scout = "scout"
    ranger = "ranger"
    bard = "bard"
    mage = "mage"
    animist = "animist"

@dataclass
class Profession:
    profession: str
    primary_char: StatsName
    lvl_up_aby: dict


    
    def get_proffesion(self):
        roll = dice_roll(Dice.d6)
        self.profession = (Professions)[roll-1]
        table = read_file(Path('./docs/profession.json'))
        table = table.get(self.profession)
        self.primary_char = table.get("primary")
        #self.lvl_up_aby = table.get("progresion")
