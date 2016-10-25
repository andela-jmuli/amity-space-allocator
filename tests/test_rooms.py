from mock import patch
import os
import unittest

from App.person import Person
from App.room import Room
from App.models import create_db

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

        @patch.dict('App.room.Room.total_rooms', {'Michigan': []})
        def test_it_creates_rooms(self):
                msg = self.room.create_room('narnia', 'whimm', 'kelly')
                self.assertEqual(msg, "Rooms have been successfully created")

        def test_it_creates_empty_room(self):
                with patch('App.room.Room'):
                        mes = self.room.create_room()
                        self.assertEqual(mes, "You can't create an empty room!")

        def test_create_room_input_string_type(self):
                with patch('App.room.Room'):
                        self.room.create_room('vanish')
                        self.assertEqual(type(self.room.room_name), str, msg="Room names should be Strings")

        @patch.dict('App.room.Room.total_rooms', {'Michigan': [], 'galaxy': [], 'vanish': []})
        def test_it_allocates_room_type(self):
                ret_o_val = self.room.allocate_room_type('vanish', 'Office')
                ret_l_val = self.room.allocate_room_type('galaxy', 'LivingSpace')
                self.assertEqual(ret_o_val, "vanish has been added as an Office")
                self.assertEqual(ret_l_val, "galaxy has been added as a LivingSpace")

                res = self.room.allocate_room_type('samsung', 'Office')
                self.assertEqual(res, "The room doesn't exist")

        @patch.dict('App.room.Room.total_rooms', {'vanish': []})
        def test_it_prints_an_existing_room(self):
                self.room.print_room('vanish')
                self.assertIn('vanish', Room.total_rooms.keys())

        @patch.dict('App.room.Room.total_rooms', {'Michigan': [], 'galaxy': [], 'vanish': []})
        def test_it_prints_room_occupants(self):

                msg = self.room.print_room('samsung')
                self.assertEqual(msg, "The room does not exist!")

        def test_it_prints_allocations(self):
                self.room.print_allocations('list.txt')
                self.assertIsNotNone('list.txt')
                pass

        @patch.dict('App.room.Room.total_rooms', {'Michigan': [], 'Camelot': []})
        @patch('App.room.Room.offices')
        @patch('App.room.Room.livingspaces')
        def test_commit_rooms(self, mock_livingspaces, mock_offices):
                mock_livingspaces.__iter__.return_value = ['Michigan']
                mock_offices.__iter__.return_value = ['Camelot']

                msg = self.room.commit_rooms('test_amity.db')
                self.assertEqual(msg, 'rooms committed to session')

        @patch.dict('App.room.Room.total_rooms', {'Michigan': [], 'Camelot': []})
        @patch('App.room.Room.offices')
        @patch('App.room.Room.livingspaces')
        def test_load_rooms(self, mock_livingspaces, mock_offices):
                mock_livingspaces.__iter__.return_value = ['Michigan']
                mock_offices.__iter__.return_value = ['Camelot']

                msg = self.room.load_rooms('amity.db')
                self.assertEqual(msg, 'Room data added successfully')

