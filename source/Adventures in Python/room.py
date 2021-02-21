class Room:
    """
    This is a class that represents a room.
    """
    def __init__(self, description, north, south, east, west):
        """This is a method that sets up the variables in the object."""
        self.description = ""
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0

def main():

    """Creating an empty array for the individual rooms to go into"""
    room_list = []

    """Create a few rooms"""
    current_room = Room("This is the current room", 0, 0, 0, 0)
    room_list.append(current_room)

    room1 = Room("You are in Room 1, there is a passage to the North", 1, 2, 3, 4)
    room_list.append(room1)

    room2 = Room("You are in Room 2, there is a passage to the South", 1, 2, 3, 4)
    room_list.append(room2)

    room3 = Room("You are in Room 3, there is a passage to the East", 1, 2, 3, 4)
    room_list.append(room3)

    room4 = Room("You are in Room 4, there is a passage to the West", 1, 2, 3, 4)
    room_list.append(room4)

    """Iterate through the list and print the description"""
    for current_room in room_list:
        print(current_room)


# Call (run) the main function
main()

