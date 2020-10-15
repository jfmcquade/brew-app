
import src.core.table as table
import src.core.main as main
import src.core.animation as animation
from src.models.round_class import Round
from src.models.person_class import Person
import src.data_store.storage as storage
import time




# SAVING AND LOADING
# Setting up variables
people = []
drinks = []
preferences = {}
deleted_people = []

# Load data from database into lists, dictionary
def load_all_data():
    loader = storage.File_Handling("loader")
    # loader.load_people_from_csv("./data/people.csv", people)
    loader.load_people_from_db(people)
    loader.list_from_file("./data/drinks.txt", drinks)
    # loader.dict_from_csv("./data/preferences.csv", preferences)
    main.dict_from_preferences(people, preferences)

# Save people and drinks to files and database
def save_all():
    main.clear_screen()
    saver = storage.File_Handling("saver")
    saver.save_list_of_person_instances_to_csv("./data/people.csv", people)
    saver.save_list_to_file("./data/drinks.txt", drinks)
    # saver.save_dict_to_csv("./data/preferences.csv", preferences)
    saver.save_drinks_list_to_db(drinks)
    saver.save_people_list_to_db(people, deleted_people)
    print("\nYour changes have been saved.")


def wait():
    input("\nPress ENTER to return to the menu.")

def invalid_input(command):
    print(f"'{command}' does not refer to a command in the menu. Please enter a valid command.")
    wait()

# PEOPLE MENU
people_menu_text = """
Please enter a number to select from the options below:

[1] Add people
[2] Remove people
[3] Return to main menu

Enter your selection:"""

def people_menu():
    while True:
        main.clear_screen()
        main.get_people(people)
        print(people_menu_text)
        command = input()
        if command == "1":
            main.clear_screen()
            main.add_person(people)
            wait()
        elif command == "2":
            main.clear_screen()
            main.remove_person(people, deleted_people)
            wait()
        elif command == "3":
            break
        else:
            invalid_input(command)
        
# DRINKS MENU
drinks_menu_text = """
Please enter a number to select from the options below:

[1] Add drinks
[2] Remove drinks
[3] Return to main menu

Enter your selection:"""

def drinks_menu():
    while True:
        main.clear_screen()
        main.get_drinks(drinks)
        print(drinks_menu_text)
        command = input()
        if command == "1":
            main.clear_screen()
            main.add_drinks(drinks)
            wait()
        elif command == "2":
            main.clear_screen()
            main.remove_drink(drinks)
            wait()
        elif command == "3":
            break
        else:
            invalid_input(command)

# PREFERENCES MENU
preferences_menu_text = """
Please enter a number to select from the options below:

[1] Add a person's preference
([2] Remove a person's preference)
[3] Return to main menu

Enter your selection:"""

def preferences_menu():
    while True:
        main.clear_screen()
        main.get_preferences(preferences)
        print(preferences_menu_text)
        command = input()
        if command == "1":
            main.clear_screen()
            main.assign_preference(people, drinks, preferences)
            wait()
        elif command =="2":
            main.clear_screen()
            print("This feature has not yet been implemented.")
            wait()
        elif command == "3":
            break
        else:
            invalid_input(command)

# ROUND MENU
active_round = None

def make_round(round_owner): 
    print(f"\nNew round, \"{round_owner.name}'s Round\", created.")
    return Round(round_owner)

def round_menu():
    # new_round = make_round(input("\nPlease enter a name for the round:\n"))
    main.clear_screen()
    main.get_people(people)
    round_owner = people[int(input("\nWho is making this round? Please select from the people above using the relevant number:\n")) - 1]
    new_round = make_round(round_owner)
    while True:
        main.clear_screen()
        print(new_round.round_menu_text(round_owner))
        command = input()
        if command == "1":
            main.clear_screen()
            new_round.add_to_round(people, drinks, preferences)
            wait()
        elif command == "2":
            main.clear_screen()
            new_round.add_all_preferences(preferences)
            wait()
        elif command == "3":
            main.clear_screen()
            table.tabulate_dict(new_round.name, new_round.orders)
            wait()
        elif command == "4":
            break
        else:
            invalid_input(command)


# MAIN MENU
# Define commands
PEOPLE_MENU_CMD = "1"
DRINKS_MENU_CMD = "2"
PREFERENCES_MENU_CMD = "3"
MAKE_ROUND_CMD = "4"
SAVE_CMD = "s"
EXIT_CMD = "x"



main_menu_text = """
Main Menu

Please enter a number to select from the options below:

[1] View/edit people
[2] View/edit drinks
[3] View/edit preferences
[4] Make a round
[s] Save
[x] Exit

Enter your selection:"""

def main_menu():
    main.clear_screen()
    print(main_menu_text)
    command = input()
    if command == PEOPLE_MENU_CMD:
        people_menu()
    elif command == DRINKS_MENU_CMD:
        drinks_menu()    
    elif command == PREFERENCES_MENU_CMD:
        preferences_menu()
    elif command == MAKE_ROUND_CMD:
        round_menu()
    elif command == SAVE_CMD:
        save_all()
        wait()
    elif command == EXIT_CMD:
        main.clear_screen()
        print(f"\nExiting {animation.app_name}, goodbye!\n")
        exit()
    else:
        invalid_input(command)


def start_app():
    while True:
        animation.welcome_animation(5)
        # input("\nPress ENTER to continue")
        break
    try:
        load_all_data()
    except:
        print("\nData could not be loaded from file.\nExiting app.")
        exit()
    finally:
        while True:
            main_menu()
    

if __name__ == "__main__":
    start_app()