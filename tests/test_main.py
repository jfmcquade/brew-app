import src.core.main as main
from src.models.person_class import Person
import unittest
from unittest import mock, TestCase

class Test_Main_Functions(TestCase):
    def test_add_elements(self):
        # Arrange
        new_elements = "John, Paul, George, Ringo"
        data = ["George Martin"]
        expected_output = ["George Martin", "John", "Paul", "George", "Ringo"]

        # Act
        actual_output = main.add_elements(new_elements, data)

        # Assert
        self.assertEqual(expected_output, actual_output)
    
    def test_dict_from_preferences(self):
        # Arrange
        person1 = Person("name 1", "preference 1")
        person2 = Person("name 2")
        people = [person1, person2]
        preferences = {}
        expected_output = {"Name 1": "preference 1"}
        # Act
        actual_output = main.dict_from_preferences(people, preferences)
        # Assert
        self.assertEqual(expected_output, actual_output)

    @mock.patch("builtins.print")
    @mock.patch("builtins.input")
    def test_assign_preference(self, mock_input, mock_print):
        # Arrange
        mock_print = None
        person1 = mock.Mock(Person)
        person1.name = "Name1"
        people = [person1]
        drinks = ["drink1", "drink2"]
        preferences = {}
        mock_input.side_effect = [1, 2]
        expected_output = {"Name1": "drink2"}

        # Act
        actual_output = main.assign_preference(people, drinks, preferences)

        # Assert
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(person1.preference, "drink2")

    # Doesn't work, different instances of class:
    # def test_add_person(self):
    #     # Arrange
    #     new_names = "name1    , name2"
    #     person1 = Person("name1")
    #     person2 = Person("name2")
    #     people = []
    #     expected_output = [person1, person2]

    #     # Act
    #     actual_output = main.add_person(new_names, people)

    #     # Assert
    #     self.assertEqual(expected_output, actual_output)

    #Trying with a mock:
    # @mock.patch("src.models.person_class.Person")
    # def test_add_person(self, mock_Person):
    #     # Arrange
    #     mock_instance = mock_Person.return_value

    #     # Act
    #     actual_instance = Person("name1")

    #     # Assert
    #     self.assertEqual(mock_instance, actual_instance)

# def add_person(new_names, people):
#     new_names_list = [name.strip() for name in new_names.split(",")]
#     for name in new_names_list:
#         person = Person(name)
#         people.append(person)
#     return people

            
if __name__ == "__main__":
    unittest.main()