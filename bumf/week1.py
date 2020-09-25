import sys
arguments = sys.argv

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
        print("| " + element)
    print(border)

# Define functions for expected commands
def get_people():
    tabulate("people", people)
def get_drinks():
    tabulate("drinks", drinks)

# Return a message if no commands entered
if len(arguments) < 2:
    print("Please enter a command.")

# Check inputs for commands and print respective outputs
for i in range(1, len(arguments)):
    if arguments[i] == "get-people":
      get_people()
    elif arguments[i] == "get-drinks":
      get_drinks()
    else:
      print(f'"{arguments[i]}" is not a command I recognise.')

