# Write a class to hold player information, e.g. what room they are in
# currently.
#player will have name, what room they're in, items they have, methods to move north, south, east, west, and method to pickup items
from item import Item
class Player:
    def __init__(self, name, current_room, items = []):
        self.name = name
        self.current_room = current_room
        self.items = items
    def __str__(self): 
        return f"This is {self.name}, they are located in {self.current_room}"
    #add function to print out the contents of player items
    def list_items(self):
        # print(self.items[0].name)
        output = f"{self.name}'s items:\n"
        
        for i, c in enumerate(self.items):
            output += "  " + str(i+1) + ". " + c.name + "\n"

        # print(self.items)
        print(output)
    def get_item(self):
        #function will add item to players list from the room it's in if the user invokes it
        for item in self.current_room.items:
            #set variable for what's typed into parser
            pickup_option = input(f'If you wish to pickup any items from {self.current_room.name} type: get and the exact name of the item: ')
            # if pickup option == item.name:
            if pickup_option == item.name:
                print(f'you now have {item.name}')
                #add item to your list:
                self.items.append(item)
                break

                
            #   remove item.name from current_room instance items
            #   add item.name to player instance
            
        











# class Item:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#     def __str__(self): 
#         return f"This is a {self.name}"

# michael = Player('Michael', 'Livingroom', [Item('basketball', 'orange'), Item('tennis ball', 'green')])
# print(michael.list_items())
    # #add functions to move in each direction:
    # def north(self):
    #     #what would the result of this function even be? string saying player moved north
    #     print(f"{self.name} moved north out of {self.current_room}")
    # def east(self):
    #     print(f"{self.name} moved east out of {self.current_room}")
    # def west(self):
    #     print(f"{self.name} moved west out of {self.current_room}")
    # def south(self):
    #     print(f"{self.name} moved south out of {self.current_room}")


