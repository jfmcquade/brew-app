
import table
import classes
import storage

app_name = "TeaRun 1.0"

# testing by yousef

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

# Person class
# 


# # Make lists and dictionaries from files
# def list_from_file(filepath, list_name):
#     file_var = open(filepath, "r")
#     file_list = file_var.readlines()
#     try:
#         file_list = [item.strip() for item in file_list]
#         for item in file_list:
#             list_name.append(item)
#         file_var.close()
#         return list_name
#     except FileNotFoundError as fnfe:
#         print("Unable to open file:" + str(fnfe))
#         return list_name
#     except:
#         print("An error occurred")
#         wait()
#     finally:
#         file_var.close()

people = []
drinks = []

storage.list_from_file("people.txt", people)
storage.list_from_file("drinks.txt", drinks)

# def dict_from_csv(filepath, dict_name):
#     try:
#         with open(filepath, "r") as csv_file:
#             csv_reader = csv.reader(csv_file)
#             for row in csv_reader:
#                 dict_name[row[0]] = row[1]
#             return dict_name
#     except FileNotFoundError as fnfe:
#         print("Unable to open file:" + str(fnfe))
#         return dict_name
#     except:
#         print("An error occurred")
#         wait()

preferences = {}

storage.dict_from_csv("preferences.csv", preferences)

# # Save data to files
# def save_dict_to_csv(filepath, dict_name):
#     try:
#         with open(filepath, "w") as csv_file:
#             csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
#             for key, value in dict_name.items():
#                 csv_writer.writerow([key, value])
#     except:
#         print(f"An error occurred when trying to save to {filepath}.")
#         wait()

# def save_list_to_file(filepath, list_name):
#     file_var = open(filepath, "w")
#     try:
#         for item in list_name:
#             file_var.write(item + "\n")
#     except:
#         print(f"Unable to write to {filepath}.")
#     finally:
#         file_var.close()




# Define functions for expected commands
def get_people():
    table.tabulate("people", people)

def get_drinks():
    table.tabulate("drinks", drinks)

def add_elements(new_elements, data):
    new_elements_list = [element.strip() for element in new_elements.split(",")]
    for element in new_elements_list:
        data.append(element)
    return data

def remove_element(data_name, dict_name):
    element_number = int(input(f"\nPlease enter the number of the {data_name} you would like to remove:\n")) - 1
    try:
        dict_name.pop(element_number)
        print(f"\n{data_name.title()} was successfully removed.")
        return dict_name
    except:
        print("\nPlease enter a valid number.")

def assign_person():
    try:
        get_people()
        chosen_person = int(input("\nPlease enter the number for a person of your choice:\n")) - 1
        get_drinks()
        chosen_drink = int(input("\nPlease enter the number for a drink of your choice:\n")) - 1
        preferences[people[chosen_person]] = drinks[chosen_drink]
        print("\nThis drink preference has been registered.")
        return preferences
    except:
        print("\nPlease try again, make sure you enter a valid number in each case.")

def get_preferences():
    table.tabulate_dict("Preferences", preferences)

# Rounds
active_round = None

class Round:
    def __init__(self, round_name):
        self.name = round_name
        self.active = active_round == self
        self.orders = {} # name:drink
        self.round_menu_text = f"""\nPlease enter a number to select from the options below:

[1] Add an order to the round, '{round_name}'
[2] Populate '{round_name}' with all saved preferences
[3] Print '{round_name}'
[4] Return to menu
"""

    def activate_round(self):
        active_round = self
        return active_round

    def add_all_preferences(self):
        for person, drink in preferences.items():
            self.orders[person] = drink

    # self.orders[name] = preferences[name]
    def add_to_round(self):
        try:
            get_people()
            chosen_person = people[int(input("\nPlease enter the number for a person of your choice:\n")) - 1]
            add_to_round_input = input(f"\nWould you like to:\n\n[1] Add {chosen_person}'s stored preference\n[2] Select drink manually\n")
            if add_to_round_input == "1":
                # Add person's preference
                try:
                    self.orders[chosen_person] = preferences[chosen_person]
                    print(f"\n{chosen_person}'s order of {preferences[chosen_person]} has been added to {self.name}.")
                except:
                    print("\nThis person does not have a preference stored.")
            elif add_to_round_input == "2":
                get_drinks()
                chosen_drink = drinks[int(input("\nPlease enter the number for a drink of your choice:\n")) - 1]
                self.orders[chosen_person] = chosen_drink
                print("\nOrder added to round.")
            else:
                print("Please enter a valid selection.")
            return self.orders
        except:
            print("\nPlease try again, make sure you enter a valid number in each case.")


def make_round(round_name): 
    print(f"\nNew round, '{round_name}', created.")
    return Round(round_name)

def round_menu():
    new_round = make_round(input("\nPlease enter a name for the round:\n"))
    print(new_round.round_menu_text)
    while True:
        command = input()
        if command == "1":
            new_round.add_to_round()
            print(new_round.round_menu_text)
        elif command == "2":
            new_round.add_all_preferences()
            print("\nPreferences added to round.")
            print(new_round.round_menu_text)
        elif command == "3":
            table.tabulate_dict(new_round.name, new_round.orders)
            print(new_round.round_menu_text)
        elif command == "4":
            print(main_menu_text)
            break
        else:
            print("\nPlease enter a valid command.")
            print(new_round.round_menu_text)


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
        get_people()
        wait()
    elif command == GET_DRINKS_CMD:
        get_drinks()
        wait()
    elif command == ADD_PEOPLE_CMD:
        add_elements(input("\nEnter the names of people to add, separated by commas:\n"), people)
        print("\nNames added to list.")
        wait()
    elif command == ADD_DRINKS_CMD:
        add_elements(input("\nEnter the names of drinks to add, separated by commas:\n"), drinks)
        print("\nDrink(s) added to list.")
        wait()
    elif command == REMOVE_PERSON_CMD:
        get_people()
        remove_element("person", people)
        wait()
    elif command == REMOVE_DRINK_CMD:
        get_drinks()
        remove_element("drink", drinks)
        wait()
    elif command == LINK_PERSON_DRINK_CMD:
        assign_person()
        wait()
    elif command == GET_PREFERENCES_CMD:
        get_preferences()
        wait()
    elif command == MAKE_ROUND_CMD:
        round_menu()
    elif command == SAVE_CMD:
        print("\nSaving data..."
        storage.save_list_to_file("drinks.txt", drinks)
        storage.save_list_to_file("people.txt", people)
        save_dict_to_csv("preferences.csv", preferences)
        print("\nYour changes have been saved.")
        wait()
    elif command == EXIT_CMD:
        print("\nExiting the programme, goodbye!\n")
        exit()
    else:
        print("\nPlease enter the number for a valid command.")
    print(main_menu_text)

def start_app():
    while True:
        main_menu()
        
if __name__ == "__main__":
    start_app()