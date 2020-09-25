import src.core.table as table
import unittest
from unittest import mock, TestCase

# path to print = "builtins.print"


class Test_Table(TestCase):
    @mock.patch("builtins.print")
    def test_tabulate(self, mock_print):
        # Arrange
        title = "Test title"
        data = ["item1", "item2"]
        mock_print.return_value = 1
        
        # Act
        print(table.tabulate(title, data))

        # Assert


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


# Stuart's example
# class Test_Select_Person_From_Menu(unittest.TestCase):
    # When a function/class is imported using `from X import Y` the resolution path to the
    # target being patched is actually in the namespace where the import occurs instead of
    # where the target is defined.
    #
    # This means that if module z.py import Y using `from X import Y` syntax the patch target
    # path tto patch Y is z.Y instead of X.Y
    # @patch("src.core.input.select_from_menu")
    # def test_when_number_is_returned_from_select_return_the_person_at_that_position(self, mock_select_from_menu):
    #     # Arrange
    #     person = Mock(Person)
    #     person.first_name = "Stuart"
    #     people = [person]
    #     mock_select_from_menu.return_value = 0
    #     # Act
    #     actual = select_person_from_menu(people)
    #     # Assert
    #     self.assertEqual(actual, people[0])
            
if __name__ == "__main__":
    unittest.main()