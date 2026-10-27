from enum import Enum


class CharName(Enum):
    STRENGTH = "strength"
    AGILITY = "agility"
    CONSTITUTION = "constitution"
    INTELLIGENCE = "intelligence"
    INTITUTION = "intuition"
    PRESENCE = "presence"


LOW_ROLL = 1
HIGH_ROLL = 102

MAX_SKILL_RANKS = 999