import unittest
from unittest import mock, TestCase
from src.models.round_class import Round
from src.models.person_class import Person
# test comment
# test comment 2  
# This was made on test_branch
# This comment was made on test-branch-2
# test comment 2
class Test_Round(TestCase):
    def test_round_add_all_preferences_method(self):
        # Arrange
        test_round = Round("test_round")
        preferences = {"key1":"value1", "key2":"value2"}

        # Act
        test_round.add_all_preferences(preferences)
        
        # Assert
        self.assertEqual(test_round.orders, preferences)

    @mock.patch("builtins.input")
    def test_round_add_to_round_method(self, mock_input):
        # Arrange
        people = ["Person A", "Person B"]
        drinks = ["Drink 1", "Drink 2"]
        preferences = {}


   
def add_to_round(self, people, drinks, preferences):
    try:
        main.get_people(people)
        chosen_person = people[int(input("\nPlease enter the number for a person of your choice:\n")) - 1]
        add_to_round_input = input(f"\nWould you like to:\n\n[1] Add {chosen_person.name}'s stored preference\n[2] Select drink manually\n")
        if add_to_round_input == "1":
            # Add person's preference
            try:
                self.orders[chosen_person.name] = chosen_person.preference
                print(f"\n{chosen_person.name}'s order of {chosen_person.preference} has been added to the round.")
            except:
                print("\nThis person does not have a preference stored.")
        elif add_to_round_input == "2":
            main.get_drinks(drinks)
            chosen_drink = drinks[int(input("\nPlease enter the number for a drink of your choice:\n")) - 1]
            self.orders[chosen_person.name] = chosen_drink
            print("\nOrder added to round.")
        else:
            print("Please enter a valid selection.")
        return self.orders
    except:
        print("\nPlease try again, make sure you enter a valid number in each case.")