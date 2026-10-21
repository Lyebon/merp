from data_loader import read_file
from builder import dice

def profession_select(option:int)-> dict | str:
    table = read_file("src/data/professions.json")
    if option == 7:
        option = dice(6)
    match option:
        case 1:
            return table.get("warrior")
        case 2:
            return table.get("scout")
        case 3:
            return table.get("ranger")
        case 4:
            return table.get("mage")
        case 5:
            return table.get("animist")
        case 6:
            return table.get("bard")
        case _:
            return "Select a valid option"

def race_selector(option: int) -> dict | str:
    table = read_file("src/data/races/ally_races.json")
    if option == 10:
        option = random_race_selector(dice(100), table.get("table"))
        if option == 5:
            return  human_race_selector(15)
    match option:
        case 1:
            return table.get("hobbit")
        case 2:
            return table.get("umly")
        case 3:
            return table.get("dwarf")
        case 4:
            return table.get("wose")
        case 5:
            return table.get("human")
        case 6:
            return table.get("half elf")
        case 7:
            return table.get("silvano")
        case 8:
            return table.get("sindar")
        case 9:
            return table.get("noldor")
        case _:
            return "Select a valid option"

def human_race_selector(option:int)->dict | str:
    table = read_file("src/data/races/human_races.json")
    if option == 15:
        option = random_race_selector(dice(100), table.get("table"))
    match option:
        case 1:
            return table.get("dunedain")
        case 2:
            return table.get("rohirrim")
        case 3:
            return table.get("beornida")
        case 4:
            return table.get("woodmen")
        case 5:
            return table.get("dorwinadan")
        case 6:
            return table.get("lossadan")
        case 7:
            return table.get("eriadorians")
        case 8:
            return table.get("bourgeois")
        case 9:
            return table.get("dunlendino")
        case 10:
            return table.get("easterlings")
        case 11:
            return table.get("haradan")
        case 12:
            return table.get("corsair")
        case 13:
            return table.get("variag")
        case 14:
            return table.get("black numenoreans")
        case _:
            return "Select a valid option"

def random_race_selector(roll:int, table:list)->int:
    for case in table:
        if case["min"] >= roll >= case["max"]:
            return case["race"]

def alignment_selector(option:int) -> str:
    if option == 10:
        option = dice(9)
    match option:
            case 1:
                return "Lawful Good"
            case 2:
                return "Lawful Neutral"
            case 3:
                return "Lawful Evil"
            case 4:
                return "Neutral Good"
            case 5:
                return "True Neutral"
            case 6:
                return "Neutral Evil"
            case 7:
                return "Chaotic Good"
            case 8:
                return "Chaotic Neutral"
            case 9:
                return "Chaotic Evil"
            case _:
                print("Select a valid option")