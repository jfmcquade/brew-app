def add_to_round(self):
        try:
            get_people()
            chosen_person = people[int(input("\nPlease enter the number for a person of your choice:\n")) - 1]
            
            
            
            
            add_to_round_input = input(f"\nWould you like to:\n\n[1] Add {chosen_person}'s stored preference\n[2] Select drink manually\n")
            if add_to_round_input == "1":
                # Add person's preference
                try:
                    self.orders[chosen_person] = preferences[chosen_person]
                    print("\nOrder added to round.")
                except:
                    print("\nThis person does not have a preference stored.")
            elif add_to_round_input == "2":
                get_drinks()
                chosen_drink = drinks[int(input("\nPlease enter the number for a drink of your choice:\n")) - 1]
                self.orders[chosen_person] = chosen_drink
                print("\nOrder added to round.")
            else:
                print("Please enter a valid selection.")
            return self.orders
        except:
            print("\nPlease try again, make sure you enter a valid number in each case.")