app_name = "TeaRun 1.0"

# Define commands
GET_PEOPLE_CMD = "1"
GET_DRINKS_CMD = "2"
ADD_PEOPLE_CMD = "3"
ADD_DRINKS_CMD = "4"
REMOVE_PERSON_CMD = "5"
REMOVE_DRINK_CMD = "6"
LINK_PERSON_DRINK_CMD = "7"
GET_FAVOURITES_CMD = "8"
SAVE_CMD = "9"
EXIT_CMD = "0"

# Open data files
# people_file = open("people.txt", "r")
# people_list = people_file.readlines()
# for i in range(len(people_list)):
#     people_list[i] = people_list[i].strip()

# Make dictionaries from files
def dict_from_file(filepath, dict_name):
    file_var = open(filepath, "r")
    file_list = file_var.readlines()
    try:
        for i in range(len(file_list)):
            file_list[i] = file_list[i].strip()
        for i in range(len(file_list)):
            dict_name[i + 1] = file_list[i]
        file_var.close()
        return dict_name
    except FileNotFoundError as fnfe:
        print("Unable to open file:" + str(fnfe))
        return dict_name
    except:
        print("An error occurred")
        wait()
    finally:
        file_var.close()

people = {}
drinks = {}

dict_from_file("people.txt", people)
dict_from_file("drinks.txt", drinks)

# Define width of table 
def get_width(title, data):
    max_length = len(title)
    extra_space = 3
    for key, value in data.items():
        if len(str(key) + str(value)) > max_length:
            max_length = len(str(key) + str(value))
    return max_length + extra_space

# Define tabulate function
def tabulate(title, data):
    width = get_width(title, data)
    border = "+" + ("=" * width) + "+"
    print(f"{border}\n| {str(title).upper()}\n{border}")
    for key, value in data.items():
        print("| " + str(key) + " " + value + " " * (width - len(str(key) + str(value)) - 2) + "|")
    print(border)

# Define functions for expected commands
def get_people():
    tabulate("people", people)

def get_drinks():
    tabulate("drinks", drinks)

def add_elements(new_elements, data):
    new_elements_list = new_elements.split(",")
    for i in range(len(new_elements_list)):
        new_elements_list[i] = new_elements_list[i].strip()
    for i in range(len(new_elements_list)):
        data[len(data) + 1] = new_elements_list[i]

def remove_element(data_name, dict_name):
    element_number = input(f"\nPlease enter the number of the {data_name} you would like to remove:\n")
    try:
        dict_name.pop(int(element_number))
        print(f"\n{data_name.title()} was successfully removed.")
        return dict_name
    except:
        print("\nPlease enter a valid number.")

def wait():
    input("\nPress ENTER to return to the menu.")

favourite_drinks = {}
def assign_person():
    try:
        get_people()
        chosen_person = input("\nPlease enter the number for a person of your choice:\n")
        get_drinks()
        chosen_drink = input("\nPlease enter the number for a drink of your choice:\n")
        favourite_drinks[people[int(chosen_person)]] = drinks[int(chosen_drink)]
        print("\nThis drink preference has been registered.")
        return favourite_drinks
    except:
        print("\nPlease try again, make sure you enter a valid number in each case.")

def get_favourites():
    tabulate("favourites", favourite_drinks)

# Save data to files
def save_dict_to_file(filepath, dict_name):
    file_var = open(filepath, "w")
    try:
        for value in dict_name.values():
            file_var.write(value + "\n")
    finally:
        file_var.close()

# User input setup
print(f"Welcome to {app_name}!" )

request_command = """
Please enter a number to select from the options below:

[1] Show people
[2] Show drinks
[3] Add people
[4] Add drinks
[5] Remove person
[6] Remove drink
[7] Choose a person's favourite drink
[8] Show drink preferences
[9] Save
[0] Exit

Enter your selection:"""

print(request_command)

def get_command():
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
    elif command == GET_FAVOURITES_CMD:
        get_favourites()
        wait()
    elif command == SAVE_CMD:
        save_dict_to_file("drinks.txt", drinks)
        save_dict_to_file("people.txt", people)
        print("\nYour changes have been saved.")
        wait()
    elif command == EXIT_CMD:
        print("\nExiting the programme, goodbye!\n")
        exit()
    else:
        print("\nPlease enter the number for a valid command.")
    print(request_command)

while True:
    get_command()
    

