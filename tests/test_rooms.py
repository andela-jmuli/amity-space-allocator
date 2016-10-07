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
                total_before = len(self.room.total_rooms)
                self.room.create_room('narnia', 'whimm', 'kelly')
                total_after = len(self.room.total_rooms)
                self.assertEqual((total_after - total_before) , 3)


        def test_create_room_input_string_type(self):
                self.room.create_room('vanish')
                self.assertEqual(type(self.room.room_name), str, msg="Room names should be Strings")

                self.room.create_room(4)
                self.assertEqual


        def test_it_allocates_room_type(self):
                self.room.create_room('vanish', 'galaxy')
                self.room.allocate_room_type('vanish', 'Office')
                self.room.allocate_room_type('galaxy', 'Office')
                self.assertEqual(len(self.room.offices), 2)


        def test_it_prints_an_existing_room(self):
                self.room.create_room('vanish')
                self.person.add_person('Joseph', 'Muli', 'Fellow', 'Y')
                self.room.print_room('vanish')
                self.assertIn('vanish', Room.total_rooms.keys())


        def test_it_prints_allocations(self):
                self.room.print_allocations('unallocated')
                self.assertIsNotNone('unallocated')


