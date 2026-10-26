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

FIRST_SKILL_RANK = 10
SECOND_SKILL_RANK = 15