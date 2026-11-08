from src.char_struct.character import Character
from src.char_struct.characteristics import Characteristic
from src.char_struct.skills import Skill
from src.char_struct.validator import CharName, RaceAlly, RaceHuman
from src.data.data_loader import Manuals

#info son las respuestas del usuario
def builder(pc_info:dict[str, str|int], manual: Manuals)->Character:
    race_info = pc_info.get("race")
    profession = pc_info.get("profession")

    character_race = race_creator(race_info, manual)

    race_char_bonus = character_race.get("characteristics")
    race_adolescence = character_race.get("adolescence")
    if race_char_bonus is None or race_adolescence is None:
        return

    profession_property = profession_creator(profession, manual)
    
    characteristic_info = pc_info.get("characteristics")
    character_characteristic = characteristics_creator(characteristic_info, race_char_bonus, manual)

    


#devuelve un diccionario con las partes de la raza
#caracteristicas:{fuerza:5...}... asi
def race_creator(race:str, manual:Manuals)->dict[str,dict]:
    if race in RaceAlly:
        race_manual = manual.manual_races()
    elif race in RaceHuman:
        race_manual = manual.manual_humans_races()
    else:
        raise ValueError("The {race} race selected are not a valid race")
    return race_manual.get(race)

def profession_creator(profession:str, manual:Manuals)->dict[str,dict]:
    profession_manual = manual.manual_professions()
    pc_profession = profession_manual.get(profession)
    if pc_profession is None:
        return
    return pc_profession


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
