# Implement a class to hold room information. This should have name and
# description attributes.
#ROOM WILL HAVE ITEMS IN IT EVENTUALLY

class Room():
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    def __str__(self):
        return f"This room is called {self.name}"
    def list_items(self):
        # print(self.items[0].name)
        output = f"{self.name}'s items:\n"
        for i, c in enumerate(self.items):
            output += "  " + str(i+1) + ". " + c.name + "\n"
        
        print(output)


