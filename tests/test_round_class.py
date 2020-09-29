import unittest
from unittest import mock, TestCase
from src.models.round_class import Round
from src.models.person_class import Person


class Test_Round(TestCase):
    def test_round_add_all_preferences_method(self):
        # Arrange
        test_round = Round("test_round")
        preferences = {"key1":"value1", "key2":"value2"}

        # Act
        test_round.add_all_preferences(preferences)
        
        # Assert
        self.assertEqual(test_round.orders, preferences)

    # @mock.patch("src.models.round_class.Round")
    def test_add_persons_preference_to_round_pref_exists(self):
        # Arrange
        chosen_person = mock.Mock(Person)
        chosen_person.name = "Johnny"
        chosen_person.preference = "tea"
        
        test_round = Round(chosen_person)

        expected_order = {"Johnny": "tea"}

        # Act
        test_round.add_persons_preference_to_round(chosen_person)

        #Assert
        self.assertEqual(test_round.orders, expected_order)

    # @mock.patch("builtins.print")
    # def test_add_persons_preference_to_round_pref_doesnt_exist(self, mock_print):
    #     # Arrange
    #     chosen_person = mock.Mock(Person)
    #     chosen_person.name = "Johnny"
    #     chosen_person.preference = ""
        
    #     test_round = Round(chosen_person)

    #     mock_print.return_value = 123
    #     expected_output = 123

    #     # Act
    #     actual_output = test_round.add_persons_preference_to_round(chosen_person)

    #     #Assert
    #     self.assertEqual(actual_output, expected_output)

# def add_persons_preference_to_round(self, chosen_person):
#     try:
#         self.orders[chosen_person.name] = chosen_person.preference
#         print(f"\n{chosen_person.name}'s order of {chosen_person.preference} has been added to the round.")
#         return self.orders
#     except:
#         print("\nThis person does not have a preference stored.")