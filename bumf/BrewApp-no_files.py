app_name = "TeaRun 1.0"

# Define commands
GET_PEOPLE_CMD = "1"
GET_DRINKS_CMD = "2"
ADD_PEOPLE_CMD = "3"
ADD_DRINKS_CMD = "4"
LINK_PERSON_DRINK_CMD = "5"
GET_FAVOURITES_CMD = "6"
EXIT_CMD = "9"


# Define lists
people = {1:"Johnny", 2:"Ross", 3:"Joachim", 4:"Charlotte"}
drinks = {1:"water", 2:"squash", 3:"beer", 4:"kefir"}

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

# User input setup
print(f"Welcome to {app_name}!" )

request_command = """
Please enter a number to select from the options below:

[1] Show people
[2] Show drinks
[3] Add people
[4] Add drinks
[5] Choose a person's favourite drink
[6] Show drink preferences
[9] Exit

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
        print("\nDrinks added to list.")
        wait()
    elif command == LINK_PERSON_DRINK_CMD:
        assign_person()
        wait()
    elif command == GET_FAVOURITES_CMD:
        get_favourites()
        wait()
    elif command == EXIT_CMD:
        print("\nExiting the programme, goodbye!\n")
        exit()
    else:
        print("\nPlease enter the number for a valid command.")
    print(request_command)
while True:
    get_command()
    

