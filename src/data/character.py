from dataclasses import dataclass
from professions import Profession
from src.engine.characteristics import Stats

@dataclass
class Character():
    name: str
    race: str
    profession: Profession
    characteristics: Stats

