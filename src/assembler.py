from data.character import Character
from data.races import Race
from data.professions import Profession
from engine.characteristics import Stats

def basic_ran_creator():
    pj = Character()
    race = Race()
    race.good_creator()
    pj.race = race.race
    prof = Profession()
    prof.get_proffesion()
    pj.profession = prof
    char = Stats()
    char.characteristic_build(Profession.primary_char, race.bonus_char)
    pj.characteristics = char

    