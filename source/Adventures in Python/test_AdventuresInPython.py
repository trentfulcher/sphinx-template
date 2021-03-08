import unittest
from room import Room
from room import GameEngine


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()


# Function to test the navigation between rooms
def test_navigation():

    # Testing directions traveled are correct
    game_engine = GameEngine()
    room = Room("testroom", 3, None, 1, None)
    game_engine.room_list.append(room)
    game_engine.go_north()
    assert game_engine.current_room == 3

    game_engine = GameEngine()
    room = Room("testroom", None, None, 1, None)
    game_engine.room_list.append(room)
    game_engine.go_north()
    assert game_engine.current_room == 0

    game_engine = GameEngine()
    room = Room("testroom1", 1, None, None, None)
    game_engine.room_list.append(room)
    room = Room("testroom2", None, 0, None, None)
    game_engine.room_list.append(room)
    game_engine.go_north()
    assert game_engine.current_room == 1
    game_engine.go_south()
    assert game_engine.current_room == 0
