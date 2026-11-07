from src.char_struct.character import Character
from src.char_struct.characteristics import Characteristic
from src.char_struct.skills import Skill
from src.char_struct.validator import CharName, RaceAlly, RaceHuman
from src.data.data_loader import Manuals

def builder(info:dict[str, str|int])->Character:
    try:
        manual = Manuals()
        race_info = info.get("race")
        profession = info.get("profession")
        character_race = race_creator(race_info)
        race_bonus = character_race.get("characteristics")
        if race_bonus is None:
            raise ValueError("The table for characteristis of the race is missing")
        characteristic_info = info.get("characteristics")
        character_characteristic = characteristics_creator(characteristic_info, race_bonus, manual)
    except:
        print("Character not created")


def race_creator(race:RaceAlly|RaceHuman)->dict[str,dict]:
    if race in RaceAlly:
        race_manual = Manuals.race_ally_search(race)
    elif race in RaceHuman:
        race_manual = Manuals.race_human_search(race)
    else:
        raise ValueError("The {race} race selected are not a valid race")
    return race_manual


def characteristics_creator(characteristic_list:dict[CharName,int],
                    bonus_for_race:dict[CharName, int],
                    manual: Manuals) -> dict[CharName,Characteristic]:
    result = {}
    for name in CharName:
        roll = characteristic_list[name]
        race_bonus = bonus_for_race[name]
        bonus_table = manual.bonuses_search("characteristics")
        result[name] = Characteristic(roll, race_bonus, bonus_table)
    return result