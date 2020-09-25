import sys
arguments = sys.argv

# Define commands
GET_PEOPLE_CMD = 1
GET_DRINKS_CMD = 2
ADD_PEOPLE_CMD = 3
ADD_DRINKS_CMD = 4
EXIT_CMD = 5

# Define lists
people = ["Johnny", "Ross", "Joachim", "Charlotte"]
drinks = ["water", "squash", "beer", "kefir"]

# Define width of table 
def get_width(title, data):
    max_length = len(title)
    extra_space = 2
    for element in data:
        if len(element) > max_length:
            max_length = len(element)
    return max_length + extra_space

# Define tabulate function
def tabulate(title, data):
    border = "+" + ("=" * get_width(title, data)) + "+"
    print(f"{border}\n| {str(title).upper()}\n{border}")
    for element in data:
        print("| " + element + " " * (get_width(title, data) - len(element) - 1) + "|")
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
    data += new_elements_list

# User input setup
print("Welcome to Drinks and People Getter 1.0!" )

request_command = """
Please enter a number to select from the options below:

[1] Get all people
[2] Get all drinks
[3] Add people
[4] Add drinks
[5] Exit

Enter your selection:"""

print(request_command)

def wait():
    input("\nPress ENTER to return to the menu.")

def get_command():
    command = input()
    if int(command) == GET_PEOPLE_CMD:
        get_people()
        wait()
    elif int(command) == GET_DRINKS_CMD:
        get_drinks()
        wait()
    elif int(command) == ADD_PEOPLE_CMD:
        add_elements(input("\nEnter the names of people to add, separated by commas:\n"), people)
        print("\nNames added to list.")
        wait()
    elif int(command) == ADD_DRINKS_CMD:
        add_elements(input("\nEnter the names of drinks to add, separated by commas:\n"), drinks)
        print("\nDrinks added to list.")
        wait()
    elif int(command) == EXIT_CMD:
        print("\nExiting the programme, goodbye!\n")
        exit()
    else:
        print("\nPlease enter the number for a valid command.")
    print(request_command)
while True:
    get_command()
    



""" Terminal argument funtionality: """
""" # Return a message if no commands entered
if len(arguments) < 2:
    print("Please enter a command.") """

# Check inputs for commands and print respective outputs
if len(arguments) >=2:
    for i in range(1, len(arguments)):
        if arguments[i] == "get-people":
          get_people()
        elif arguments[i] == "get-drinks":
          get_drinks()
        else:
          print(f'"{arguments[i]}" is not a command I recognise.')

