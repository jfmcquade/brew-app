active_round = None

class Round:
    def __init__(self, round_name):
        self.round_name = round_name
        self.active = active_round == self
        self.orders = {}

    def activate_round(self):
        active_round = self
        return active_round

    def add_preferences(self, preferences):
        for person, drink in preferences.items():
            self.orders[person] = drink
    
    def add_to_round(self, person, drink)
        self.orders[person] = 
        
