class Person:
    def __init__(self, person_id, name, preference = ""):
        self.person_id = person_id
        self.name = name.title()
        self.preference = preference