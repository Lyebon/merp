from dataclasses import dataclass
from character.characteristics import Characteristic
from skills import Skill

@dataclass
class Character:
    name: str
    description:dict[str:str] # edad, motivacion, alineamiento, etc
    race:str
    profession:str
    characteristics: dict[str:Characteristic] #Objeto que contiene caracteristicas y reglas
    skills:dict[str:Skill] # Objeto que contiene habilidades y reglas de habilidades

    def from_dict(sheet:dict):
        pass

    def __repr__(self):
        pass