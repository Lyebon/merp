from dataclasses import dataclass
from src.data.data import StatsName
from src.engine.characteristics import Stat

@dataclass
class Character():
    name: str
    race: str
    profession:str
    characteristics: dict[StatsName:Stat]

    def from_dict(data):
        pass