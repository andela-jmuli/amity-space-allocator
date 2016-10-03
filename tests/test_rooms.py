import unittest
import os
from App.room import Room


class TestRoom(unittest.TestCase):

        def setUp(self):
                self.room = Room()

        def test_room_class_instance(self):
                self.assertIsInstance(self.room, Room)


        def test_it_creates_rooms(self):
                self.room.create_room('narnia', 'whimm', 'kelly')
                self.assertEqual(len(self.room.total_rooms), 3)

        def test_it_allocates_room_type(self):
                self.room.create_room('vanish', 'galaxy')
                self.room.allocate_room_type('vanish', 'Office')
                self.room.allocate_room_type('galaxy', 'Office')
                self.assertEqual(len(self.room.offices), 2)




        def test_it_prints_rooms(self):
                pass


        def test_it_prints_allocations(self):
                pass
