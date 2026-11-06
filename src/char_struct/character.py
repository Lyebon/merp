from dataclasses import dataclass
from characteristics import Characteristic
from skills import Skill
from validator import CharName

@dataclass
class Character:
    id: int
    name: str
    #description:dict[str,str] # edad, motivacion, alineamiento, etc
    race:str
    profession:str
    characteristics: dict[CharName,Characteristic] #Objeto que contiene caracteristicas y reglas
    skills:dict[str,Skill] # Objeto que contiene habilidades y reglas de habilidades
