from dataclasses import dataclass
from data.characteristics import Stats

@dataclass
class Character():
    name: str
    race: str
    profession:str
    characteristics: Stats

