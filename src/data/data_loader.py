import json
from copy import deepcopy

class Manuals:
    def __init__(self):
        self._bonuses = self.open_file("src/data/bonuses.json")
        self._leveling = self.open_file("src/data/leveling.json")
        self._professions = self.open_file("src/data/professions.json")
        self._race_ally = self.open_file("src/data/race_ally.json")
        self._race_human = self.open_file("src/data/race_human.json")
        
    def open_file(self, path_file: str)->dict:
        with open(path_file, "r", encoding="UTF-8") as f:
            file = json.load(f)
            return file

    def bonnuses_search(self, bonus:str) -> tuple[tuple]:
        rules = self._bonuses.get(bonus)
        copy_rules = deepcopy(rules)
        if rules is not None:
            return copy_rules
        raise ValueError(f"{bonus} is not in the bonuses.json file")

    def leveling_search(self, profession:str) -> dict:
        rules = self._leveling.get(profession)
        copy_rules = deepcopy(rules)
        if rules is not None:
            return copy_rules
        raise ValueError(f"{profession} is not in the leveling.json file")

    def professions_search(self, profession:str) -> dict:
        rules = self._professions.get(profession)
        copy_rules = deepcopy(rules)
        if rules is not None:
            return copy_rules
        raise ValueError(f"{profession} is not in the professions.json file")

    def race_ally_search(self, race:str) -> dict:
        rules = self._race_ally.get(race)
        copy_rules = deepcopy(rules)
        if rules is not None:
            return copy_rules
        raise ValueError(f"{race} is not in the race_ally.json file")

    def race_human_search(self, race:str) -> dict:
        rules = self._race_human.get(race)
        copy_rules = deepcopy(rules)
        if rules is not None:
            return copy_rules
        raise ValueError(f"{race} is not in the race_human.json file")
    