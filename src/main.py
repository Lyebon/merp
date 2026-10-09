from menu.menu import welcome_menu, profession_menu, race_menu, human_race_menu, alignment_menu
from menu.selectors import race_selector, human_race_selector, profession_select, alignment_selector

def builder()->dict:
    character_info = [
        "name", "hight", "weight", "gender", "age",
        "race", "profession", "alignment",
        "hair color", "eye color", "physical special", "personality", "motivation", "status", "family"
        ]
    new_character = {}
    for info in character_info:
            match info:
                case "race":
                    race_menu()
                    option = int(input("Enter a valid option..."))
                    if option == 5:
                        human_race_menu()
                        option = int(input("Enter a valid option..."))
                        new_character[info] = human_race_selector(option)
                    else:
                        new_character[info] = race_selector(option)
                case "profession":
                    profession_menu()
                    option = int(input("Enter a valid option..."))
                    new_character[info] = profession_select(option)
                case "alignment":
                    alignment_menu()
                    option = int(input("Enter a valid option..."))
                    new_character[info] =alignment_selector(option)
                case _:
                    new_character[info] =  input(f"""\
            What is your {info}?
    """)

def main():
    welcome_menu()
    new_character = builder()
    print(new_character)



main()