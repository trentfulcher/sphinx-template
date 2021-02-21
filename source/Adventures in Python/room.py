class Room:
    """
    This is a class that represents a room.
    """
    def __init__(self, description, north, south, east, west):
        """This is a method that sets up the variables in the object."""
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():

    """Creating an empty array for the individual rooms to go into"""
    room_list = []

    """Create a few rooms"""
    southhall = Room("You are in the south hall.", 1, 1, None, 1)
    room_list.append(southhall)

    diningroom = Room("You are in the dining room", 1, None, None, 1)
    room_list.append(diningroom)

    bedroom1 = Room("You are in a bedroom", None, 1, 1, None)
    room_list.append(bedroom1)

    bedroom2 = Room("You are in a 2nd bedroom", 1, 1, None, None)
    room_list.append(bedroom2)

    northhall = Room("You are in the north hall", 1, 1, 1, 1)
    room_list.append(northhall)

    kitchen = Room("You are in the kitchen", None, None, 1, 1)
    room_list.append(kitchen)

    balcony = Room("You are standing on the balcony", None, None, 1, None)
    room_list.append(balcony)

    current_room = Room("", 0, 0, 0, 0)
    room_list.append(current_room)

    for current_room in room_list:
        print(current_room.description)


# Call (run) the main function
main()

