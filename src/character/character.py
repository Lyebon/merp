from dataclasses import dataclass
from src.enums import StatsName
from character.characteristics import Stat

@dataclass
class Character():
    name: str
    race: str
    profession:str
    characteristics: dict[StatsName:Stat]

    def from_dict(data):
        pass