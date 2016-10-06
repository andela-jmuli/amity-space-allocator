import unittest
import os
from App.room import Room
from App.person import Person

class TestRoom(unittest.TestCase):

        def setUp(self):
                self.room = Room()
                self.person = Person()


        def test_room_class_instance(self):
                self.assertIsInstance(self.room, Room)


        def test_it_creates_rooms(self):
                self.room.create_room('narnia', 'whimm', 'kelly')
                self.assertEqual(len(self.room.total_rooms), 3)


        def test_create_room_input_string_type(self):
                self.room.create_room('vanish')
                self.assertEqual(type('vanish'), str, msg="Enter a String")


        def test_it_allocates_room_type(self):
                self.room.create_room('vanish', 'galaxy')
                self.room.allocate_room_type('vanish', 'Office')
                self.room.allocate_room_type('galaxy', 'Office')
                self.assertEqual(len(self.room.offices), 2)


        def test_it_prints_an_existing_room(self):
                self.room.create_room('vanish')
                self.person.add_person('Joseph', 'Muli', 'Fellow', 'Y')
                self.room.print_room('vanish')
                self.assertIn('vanish', self.room.total_rooms)


        def test_it_prints_allocations(self):
                pass


        def test_room_is_fully_occupied(self):
                pass
