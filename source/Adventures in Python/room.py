class Room:
    # This is a class that represents a room.

    def __init__(self, description, north, south, east, west):
        # This is a method that sets up the variables in the object
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


class GameEngine:
    # This is a class that is used for testing the game

    def __init__(self):
        self.room_list = []
        self.current_room = 0

    # Function to take the user north
    def go_north(self):
        # If the user selected 'N' or 'n'
        next_room = self.room_list[self.current_room].north

        # Make sure the user entered the correct information
        if next_room is None:
            print()
            print("You can't go that way.")

        # Set the current room to equal the next room
        else:
            self.current_room = next_room

    # Function to take the user south
    def go_south(self):
        # If the user selected 'S' or 's'
        next_room = self.room_list[self.current_room].south

        # Make sure the user entered the correct information
        if next_room is None:
            print()
            print("You can't go that way.")

        # Set the current room to equal the next room
        else:
            self.current_room = next_room

    # Function to take the user east
    def go_east(self):
        # If the user selected 'E' or 'e'
        next_room = self.room_list[self.current_room].east

        # Make sure the user entered the correct information
        if next_room is None:
            print()
            print("You can't go that way.")

        # Set the current room to equal the next room
        else:
            self.current_room = next_room

    # Function to take the user west
    def go_west(self):
        # If the user selected 'W' or 'w'
        next_room = self.room_list[self.current_room].west

        # Make sure the user entered the correct information
        if next_room is None:
            print()
            print("You can't go that way.")

        # Set the current room to equal the next room
        else:
            self.current_room = next_room

    def quit_game(self):
        print()
        print("Sorry to hear that, have a great day.")
        print()
        exit()

    def user_input_check(self):
        print()
        print("That is an invalid selection, please try again")
        print()


# Defining out main program.
def main():

    # Creating an empty array for the individual rooms to go into
    game_engine = GameEngine()

    # Create a few rooms and add them to the list
    bedroom2 = Room("You are in a bedroom. \nThere is a door to the East, "
                    "and a door to the North.", 3, None, 1, None)
    game_engine.room_list.append(bedroom2)

    southhall = Room("You are in the south hall. \nThere is a door to the "
                     "East, 1 to the West, and a door to the North.", 4,
                     None, 2, 0)
    game_engine.room_list.append(southhall)

    diningroom = Room("You are in the dining room. \nThere is a door to the "
                      "North, and a door to the West", 5, None, None, 1)
    game_engine.room_list.append(diningroom)

    bedroom1 = Room("You are in a bedroom. \nThere is a door to the South, "
                    "and a door to the East.", None, 0, 4, None)
    game_engine.room_list.append(bedroom1)

    northhall = Room("You are in the north hall. \nThere are doors in all "
                     "directions.", 6, 1, 5, 3)
    game_engine.room_list.append(northhall)

    kitchen = Room("You are in the kitchen. \nThere is a door to the "
                   "South, and a door to the West", None, 2, None, 4)
    game_engine.room_list.append(kitchen)

    balcony = Room("You are standing on the balcony. \nThere is a door to the "
                   "South", None, 4, None, None)
    game_engine.room_list.append(balcony)

    # Set the current Room to 0
    current_room = 0

    # Create a variable called done and set it to false
    done = False

    while not done:
        print()
        print(game_engine.room_list[game_engine.current_room].description)
        print()
        user_input = input("What would you like to do? Please select 'N', 'S', "
                           "'E', or 'W'!(or press Q to quit.)")
        print()

        # If the user selected 'N' or 'n'
        if user_input == 'N' or user_input == "n":
            game_engine.go_north()

        # If the user selected 'S' or 's'
        if user_input == 'S' or user_input == "s":
            game_engine.go_south()

        # If the user selected 'E' or 'e'
        if user_input == 'E' or user_input == "e":
            game_engine.go_east()

        # If the user selected 'W' or 'w'
        if user_input == 'W' or user_input == "w":
            game_engine.go_west()

        # If user selects 'Q' or 'q', quit the game
        if user_input == 'Q' or user_input == 'q':
            game_engine.quit_game()

        # If user selects anything else
        if user_input != 'N' and user_input != 'n' and user_input != 'S' and \
           user_input != 's' and user_input != 'E' and user_input != 'e' and \
           user_input != 'W' and user_input != 'w' and user_input != 'Q' and \
           user_input != 'q':
            game_engine.user_input_check()


if __name__ == "__main__":
    # Call (run) the main function
    main()

# Add if's to a function to test to be able to test that function easily
# def user_options
# does it work if they put in fred
# Did they actually move rooms
