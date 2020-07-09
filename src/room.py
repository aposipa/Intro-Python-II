# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.n_to = ''
        self.e_to = ''
        self.s_to = ''
        self.w_to = ''
        self.loot = []
        
    def __str__(self):
      return f'You are in the {self.name}. Description: {self.description}'  

    def add_item(self, item):
        self.loot.append(item)

    def remove_item(self, item):
        self.loot.remove(item)