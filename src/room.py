# Implement a class to hold room information. This should have name and
# description attributes.
#ROOM WILL HAVE ITEMS IN IT EVENTUALLY

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"This room is called {self.name}, it could be described as {self.description}"


