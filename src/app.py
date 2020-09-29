
import src.core.table as table
import src.core.main as main
from src.models.round_class import Round
from src.models.person_class import Person
import src.data_store.storage as storage

app_name = "TeaRun 1.0"

# Define commands
GET_PEOPLE_CMD = "1"
GET_DRINKS_CMD = "2"
ADD_PEOPLE_CMD = "3"
ADD_DRINKS_CMD = "4"
REMOVE_PERSON_CMD = "5"
REMOVE_DRINK_CMD = "6"
LINK_PERSON_DRINK_CMD = "7"
GET_PREFERENCES_CMD = "8"
MAKE_ROUND_CMD = "9"
SAVE_CMD = "s"
EXIT_CMD = "x"


# Saving and loading
people = []
drinks = []
preferences = {}

# Load data into lists, dictionary
def load_all_data():
    loader = storage.File_Handling("loader")
    loader.load_people_from_csv("./data/people.csv", people)
    loader.list_from_file("./data/drinks.txt", drinks)
    # loader.dict_from_csv("./data/preferences.csv", preferences)
    main.dict_from_preferences(people, preferences)

# Save people and drinks to file
def save_all():
    saver = storage.File_Handling("saver")
    saver.save_list_of_person_instances_to_csv("./data/people.csv", people)
    saver.save_list_to_file("./data/drinks.txt", drinks)
    # saver.save_dict_to_csv("./data/preferences.csv", preferences)
    saver.save_drinks_list_to_db(drinks)
    print("\nYour changes have been saved.")


# Rounds
def make_round(round_owner): 
    print(f"\nNew round, \"{round_owner.name}'s Round\", created.")
    return Round(round_owner)

def round_menu():
    # new_round = make_round(input("\nPlease enter a name for the round:\n"))
    main.get_people(people)
    round_owner = people[int(input("\nWho is making this round? Please select from the people above using the relevant number:\n")) - 1]
    new_round = make_round(round_owner)
    print(new_round.round_menu_text(round_owner))
    while True:
        command = input()
        if command == "1":
            new_round.add_to_round(people, drinks, preferences)
            print(new_round.round_menu_text(round_owner))
        elif command == "2":
            new_round.add_all_preferences(preferences)
            print("\nPreferences added to round.")
            print(new_round.round_menu_text(round_owner))
        elif command == "3":
            table.tabulate_dict(new_round.owner.name, new_round.orders)
            print(new_round.round_menu_text(round_owner))
        elif command == "4":
            print(main_menu_text)
            break
        else:
            print("\nPlease enter a valid command.")
            print(new_round.round_menu_text(round_owner))


# User input setup
print(f"Welcome to {app_name}!" )

main_menu_text = """
Please enter a number to select from the options below:

[1] Show people
[2] Show drinks
[3] Add people
[4] Add drinks
[5] Remove person
[6] Remove drink
[7] Add a person's drink preference
[8] Show drink preferences
[9] Make a round
[s] Save
[x] Exit

Enter your selection:"""

print(main_menu_text)

def wait():
    input("\nPress ENTER to return to the menu.")

def main_menu():
    command = input()
    if command == GET_PEOPLE_CMD:
        main.get_people(people)
        wait()
    elif command == GET_DRINKS_CMD:
        main.get_drinks(drinks)
        wait()
    elif command == ADD_PEOPLE_CMD:
        main.add_person(input("\nEnter the names of people to add, separated by commas:\n"), people)
        print("\nName(s) added to list.")
        wait()
    elif command == ADD_DRINKS_CMD:
        main.add_elements(input("\nEnter the names of drinks to add, separated by commas:\n"), drinks)
        print("\nDrink(s) added to list.")
        wait()
    elif command == REMOVE_PERSON_CMD:
        main.remove_person(people)
        wait()
    elif command == REMOVE_DRINK_CMD:
        main.remove_drink(drinks)
        wait()
    elif command == LINK_PERSON_DRINK_CMD:
        main.assign_preference(people, drinks, preferences)
        wait()
    elif command == GET_PREFERENCES_CMD:
        main.get_preferences(preferences)
        wait()
    elif command == MAKE_ROUND_CMD:
        round_menu()
    elif command == SAVE_CMD:
        save_all()
        wait()
    elif command == EXIT_CMD:
        print("\nExiting the programme, goodbye!\n")
        exit()
    else:
        print("\nPlease enter the number for a valid command.")
    print(main_menu_text)

def start_app():
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