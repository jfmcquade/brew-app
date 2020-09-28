import src.core.main as main
from src.models.person_class import Person

active_round = None

class Round:
    def __init__(self, round_owner: Person):
        # self.name = f"{round_owner.name}'s Round"
        self.owner = round_owner
        self.active = active_round == self
        self.orders = {} # name:drink
#         self.round_menu_text = f"""\nPlease enter a number to select from the options below:

# [1] Add an order to the round, "{round_owner.name}'s Round".
# [2] Populate "{round_owner.name}'s Round" with all saved preferences
# [3] Print "{round_owner.name}'s Round".
# [4] Return to menu
# """
    def round_menu_text(self, round_owner: Person):
        round_menu_text = f"""\nPlease enter a number to select from the options below:

[1] Add an order to the round, "{round_owner.name}'s Round".
[2] Populate "{round_owner.name}'s Round" with all saved preferences
[3] Print "{round_owner.name}'s Round".
[4] Return to menu
"""
        return round_menu_text
    def activate_round(self):
        active_round = self
        return active_round

    def add_all_preferences(self, preferences):
        for person, drink in preferences.items():
            self.orders[person] = drink

    # self.orders[name] = preferences[name]
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

