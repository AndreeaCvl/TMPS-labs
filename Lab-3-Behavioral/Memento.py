class Memento:
    def __init__(self, weapon, name, position, time_served, superior):
        self.weapon = weapon
        self.name = name
        self.position = position
        self.time_served = time_served
        self.superior = superior

    def get_states(self):
        return (self.weapon, self.name, self.position, self.time_served, self.superior)

