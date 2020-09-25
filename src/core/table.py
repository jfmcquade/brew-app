# Define tabulate functions
def get_width(title, data):
    max_length = len(title)
    extra_space = 5
    for item in data:
        if len(str(item)) > max_length:
            max_length = len(str(item))
    return max_length + extra_space

def tabulate(title, data): # Adds numbers
    width = get_width(title, data)
    border = "+" + ("=" * width) + "+"
    print(f"{border}\n| {str(title).upper()}\n{border}")
    data_enum = list(enumerate(data, 1))
    for a_tuple in data_enum:
        print("| " + str(a_tuple[0]) + " " + str(a_tuple[1]) + (" " * (width - len(str(a_tuple[0]) + str(a_tuple[1])) - 2)) + "|")
    print(border)

def tabulate_dict(title, data): # Does not add numbers
    width = get_width(title, list_from_dict(data))
    border = "+" + ("=" * width) + "+"
    print(f"{border}\n| {str(title).upper()}\n{border}")
    for key, value in data.items():
        print("| " + str(key) + ": " + value + " " * (width - len(str(key) + str(value)) - 3) + "|")
    print(border)

def list_from_dict(dict_name):
    dict_as_list = []
    for each_tuple in list(dict_name.items()):
        item_as_string = " ".join(each_tuple)
        dict_as_list.append(item_as_string)
    return dict_as_list