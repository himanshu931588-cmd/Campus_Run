import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from item import Item, create_timetable
from player import CLASS_TIME, Player
from room import Room


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.room = Room("Main Gate", width=3, height=3, walls={(1, 0)})
        self.player = Player(current_room=self.room)

    def test_starting_state(self):
        self.assertEqual(self.player.current_room.name, "Main Gate")
        self.assertEqual(self.player.inventory, [])
        self.assertEqual(self.player.get_current_time(), "9:27 AM")

    def test_movement_and_collision(self):
        self.assertEqual(self.player.move("S"), "You move to Main Gate.")
        self.assertEqual(self.player.move("D"), "You move to Main Gate.")
        self.assertEqual(self.player.move("A"), "You move to Main Gate.")
        self.assertEqual(self.player.move("W"), "You move to Main Gate.")
        self.assertEqual(self.player.move("D"), "You cannot move there. That is a wall.")
        self.assertEqual(self.player.move("X"), "Invalid direction. Use W, A, S, or D.")

    def test_boundary(self):
        self.assertEqual(self.player.move("A"), "You cannot move there. That is a wall.")
        self.assertEqual((self.player.x, self.player.y), (0, 0))

    def test_room_transition(self):
        stairs = Room("Stairs")
        self.room.connect("A", stairs)
        self.assertEqual(self.player.move("A"), "You enter Stairs.")
        self.assertIs(self.player.current_room, stairs)

    def test_time(self):
        self.player.advance_time(10)
        self.assertEqual(self.player.get_current_time(), "9:27 AM")
        self.player.time = CLASS_TIME - 5
        self.player.advance_time(10)
        self.assertEqual(self.player.get_current_time(), "9:30 AM")
        self.assertTrue(self.player.is_late())
        self.assertEqual(self.player.get_time_left(), 0)
        self.assertEqual(self.player.get_arrival_band(), "9:30-9:32")

    def test_inventory_and_use(self):
        timetable = create_timetable()
        badge = Item("ID Card", usable=True)
        self.assertIn("picked up", self.player.pick_item(timetable))
        self.player.pick_item(badge)
        self.assertTrue(self.player.has_item("Timetable"))
        self.assertIn("Timetable", self.player.show_inventory())
        timetable_text = self.player.use_item("Timetable")
        self.assertIn("Python Programming", timetable_text)
        self.assertIn("Room 404", timetable_text)
        self.assertIn("removed", self.player.remove_item("Timetable"))
        self.assertFalse(self.player.has_item("Timetable"))

    def test_invalid_inventory_and_interaction(self):
        self.assertEqual(self.player.remove_item("Phone"), "That item is not in your inventory.")
        self.assertEqual(self.player.use_item("Phone"), "That item is not in your inventory.")
        self.assertEqual(self.player.interact(), "There is nothing to interact with here.")

    def test_room_item_and_classroom_integration(self):
        classroom = Room("Classroom 404", room_type="classroom")
        self.room.connect("D", classroom)
        self.assertEqual(self.player.move("D"), "You enter Classroom 404.")
        self.assertTrue(self.player.is_in_classroom())


if __name__ == "__main__":
    unittest.main()