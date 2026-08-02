from dataclasses import dataclass
from src.enums import StatsName
from src.character.characteristics import Stat

@dataclass
class Character():
    race: str
    profession:str
    characteristics: dict[StatsName:Stat]

    @classmethod
    def from_dict(cls, data:dict[str:str|dict]):
        cls.race = data.get("race")
        cls.profession = data.get("profession")
        cls.characteristics = data.get("characteristics")
        return cls