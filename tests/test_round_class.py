import unittest
from unittest import mock, TestCase
from src.models.round_class import Round
from src.models.person_class import Person
# test comment
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


# def test_round_add_to_round_method():
#     # Arrange
#     people = ["Person A", "Person B"]
#     drinks = ["Drink 1", "Drink 2"]