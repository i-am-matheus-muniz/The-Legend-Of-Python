class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = int(entry)
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    
    def speak(self):
        print(self.name, self.name)
    
    def display_details(self):
        print(vars(self))

pikachu = Pokemon(25, 'Pikachu', 'Electric', 'When it is angered, it immediately discharges the energy stored in the pouches in its cheeks.', False)

pikachu.speak()
pikachu.display_details()