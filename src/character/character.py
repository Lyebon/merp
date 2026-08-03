from dataclasses import dataclass
from src.enums import StatsName, AllyRaces, HumanRaces, Professions
from src.character.characteristics import Stat

@dataclass
class Character():
    race: AllyRaces|HumanRaces
    profession:Professions
    characteristics: dict[StatsName:Stat]

    @classmethod
    def from_dict(cls, data):
        cls.race = data.get("race")
        cls.profession = data.get("profession")
        cls.characteristics = data.get("characteristics")
        return cls