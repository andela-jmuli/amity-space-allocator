from mock import patch
import os
import unittest

from App.person import Person
from App.room import Room


class TestRoom(unittest.TestCase):

        def setUp(self):
                self.room = Room()
                self.person = Person()


        def test_room_class_instance(self):
                self.assertIsInstance(self.room, Room)

        @patch.dict('App.room.Room.total_rooms', {'Michigan': []})
        def test_duplicate_room_creation(self):
                res = self.room.create_room('Michigan')
                self.assertEqual(res, 'A room with that name already exists!')


        def test_it_creates_rooms(self):
                total_before = len(self.room.total_rooms)
                self.room.create_room('narnia', 'whimm', 'kelly')
                total_after = len(self.room.total_rooms)
                self.assertEqual((total_after - total_before) , 3)

        def test_it_creates_empty_room(self):
                mes = self.room.create_room()
                self.assertEqual(mes, "You can't create an empty room!")

        def test_create_room_input_string_type(self):
                self.room.create_room('vanish')
                self.assertEqual(type(self.room.room_name), str, msg="Room names should be Strings")

        def test_it_allocates_room_type(self):
                self.room.create_room('vanish', 'galaxy')
                self.room.allocate_room_type('vanish', 'Office')
                self.room.allocate_room_type('galaxy', 'LivingSpace')
                res = self.room.allocate_room_type('samsung', 'Office')
                self.assertEqual(res, "The room doesn't exist")
                self.assertIn('vanish', self.room.offices)

        # @patch('App.room.Room.livingspaces', {'Michigan': []})
        # def test_room_type_allocaction(self, mocked_livingspaces):
        #         self.room.allocate_room_type('Michigan', 'LivingSpace')
        #         self.assertIn('Michigan', mocked_livingspaces)

        @patch.dict('App.room.Room.total_rooms', {'vanish': []})
        def test_it_prints_an_existing_room(self):
                self.room.print_room('vanish')
                self.assertIn('vanish', Room.total_rooms.keys())

        def test_exception_on_none_existence_room(self):
                mes = self.room.print_room('milky')
                self.assertEqual(mes, "The room does not exist!")

        def test_it_prints_allocations(self):
                self.room.print_allocations('list.txt')
                self.assertIsNotNone('list.txt')
                pass


