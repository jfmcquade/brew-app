import src.core.table as table
from src.models.person_class import Person
from typing import List, Dict
import os

def clear_screen():
    os.system('clear')

def get_people(people):
    people_names = []
    for person in people:
        people_names.append(person.name)
    table.tabulate("people", people_names)

def get_drinks(drinks: List[str]):
    table.tabulate("drinks", drinks)

def add_person(new_names, people):
    new_names_list = [name.strip() for name in new_names.split(",")]
    for name in new_names_list:
        person = Person(name)
        people.append(person)
    return people

def add_elements(new_elements, data):
    new_elements_list = [element.strip() for element in new_elements.split(",")]
    for element in new_elements_list:
        data.append(element)
    return data

def remove_drink(drinks):
    get_drinks(drinks)
    try:
        element_number = int(input("\nPlease enter the number of the drink you would like to remove:\n")) - 1
        drinks.pop(element_number)
        print("\nDrink was successfully removed.")
        return drinks
    except:
        print("\nPlease enter a valid number.")

def remove_person(people):
    get_people(people)
    try:
        element_number = int(input("\nPlease enter the number of the person you would like to remove:\n")) - 1
        people.pop(element_number)
        print("\nPerson was successfully removed.")
        return people
    except:
        print("\nPlease enter a valid number.")

def add_persons_preference_to_round(chosen_person):
    try:
        self.orders[chosen_person.name] = chosen_person.preference
        print(f"\n{chosen_person.name}'s order of {chosen_person.preference} has been added to the round.")
    except:
        print("\nThis person does not have a preference stored.")

# def remove_element(data_name, list_var):
#     try:
#         element_number = int(input(f"\nPlease enter the number of the {data_name} you would like to remove:\n")) - 1
#         list_var.pop(element_number)
#         print(f"\n{data_name.title()} was successfully removed.")
#         return list_var
#     except:
#         print("\nPlease enter a valid number.")

# def test_remove_element():
#     # Arrange
#     data_name = "letter"
#     list_var = ["a", "b", "c"]
#     expected = ["a", "c"]

#     # Act
#     actual = remove_element(data_name, list_var)

#     # Assert
#     assert expected == actual

# test_remove_element()

def dict_from_preferences(people, preferences):
        for person in people:
            if person.preference == "":
                continue
            else:
                preferences[person.name] = person.preference
        return preferences

def assign_preference(people: List[Person], drinks: List[str], preferences: Dict):
    try:
        get_people(people)
        chosen_person = int(input("\nPlease enter the number for a person of your choice:\n")) - 1
        get_drinks(drinks)
        chosen_drink = int(input("\nPlease enter the number for a drink of your choice:\n")) - 1
        people[chosen_person].preference = drinks[chosen_drink]
        dict_from_preferences(people, preferences)
        print("\nThis drink preference has been registered.")
        return preferences
    except:
        print("\nPlease try again, make sure you enter a valid number in each case.")

def get_preferences(preferences: Dict):
    table.tabulate_dict("Preferences", preferences)

# Preferences in dictionary:
# #    
# def assign_preference(people: List[str], drinks: List[str], preferences: Dict):
#     try:
#         get_people(people)
#         chosen_person = int(input("\nPlease enter the number for a person of your choice:\n")) - 1
#         get_drinks(drinks)
#         chosen_drink = int(input("\nPlease enter the number for a drink of your choice:\n")) - 1
#         preferences[people[chosen_person]] = drinks[chosen_drink]
#         print("\nThis drink preference has been registered.")
#         return preferences
#     except:
#         print("\nPlease try again, make sure you enter a valid number in each case.")

# def get_preferences(preferences: Dict):
#     table.tabulate_dict("Preferences", preferences)