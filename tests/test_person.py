import mock
import unittest
import os
from App.person import Person
from App.room import Room
from mock import mock_open, patch
from StringIO import StringIO
import sys

class TestPerson(unittest.TestCase):

        def setUp(self):
                self.person = Person()
                sys.stdout = StringIO()

        def test_person_class_instance(self):
                self.assertIsInstance(self.person, Person)

        @patch.dict('App.room.Room.total_rooms', {'oculus': [], 'haskel': []})
        @patch.dict('App.person.Person.total_people', {1: 'MigwiNdungu'})
        @patch('App.room.Room.offices')
        @patch('App.room.Room.livingspaces')
        @patch('App.person.Person.fellows')
        @patch('App.person.Person.staff')
        def test_it_adds_a_person(self, mock_staff, mock_fellows, mock_livingspaces, mock_offices):
                mock_livingspaces.__iter__.return_value = ['haskel']
                mock_offices.__iter__.return_value = ['oculus']
                mock_fellows.__iter__.return_value = []
                mock_staff.__iter__.return_value = []

                msg = self.person.add_person('Joseph', 'Muli', 'Fellow', 'Y')
                self.assertEqual(msg, 'JosephMuli Added successfully')
                already_present = self.person.add_person('Migwi', 'Ndungu', 'Fellow', 'Y')
                self.assertEqual(already_present, 'oops! Someone with the username MigwiNdungu already exists')

                staff_accomodation = self.person.add_person('Michelle', 'Korir', 'Staff', 'Y')
                self.assertEqual(staff_accomodation, 'NOTE: Staff members are not allocated livingspaces')

        @patch.dict('App.room.Room.total_rooms', {'oculus': [1,2,5,6,9,10], 'narnia': [3,4,7,8,11,12], 'haskel': [1,2,3,4]})
        @patch.dict('App.person.Person.total_people', {1: 'MigwiNdungu', 2: 'JosephMuli', 3: 'Josh', 4: 'Njira', 5:'kevin', 6:'mwangi', 7:'john', 8:'milkah', 9:'noelah', 10:'serah', 11:'sila', 12:'mary'})
        @patch('App.room.Room.offices')
        @patch('App.room.Room.livingspaces')
        @patch('App.person.Person.fellows')
        @patch('App.person.Person.staff')
        def test_adding_to_fully_occupied_rooms(self, mock_staff, mock_fellows, mock_livingspaces, mock_offices):
                mock_livingspaces.__iter__.return_value = ['haskel']
                mock_offices.__iter__.return_value = ['oculus']
                mock_fellows.__iter__.return_value = []
                mock_staff.__iter__.return_value = []

                fully_occupied_office = self.person.add_person('Jimmy', 'Kamau', 'Staff', 'N')
                self.assertEqual(fully_occupied_office, 'sorry all offices are currently fully occupied, adding to staff-unallocated-without-offices...')

                fully_occupied_ls = self.person.add_person('Alex', 'Magana', 'Fellow', 'Y')
                self.assertEqual(fully_occupied_ls, 'sorry all livingspaces are currently fully occupied, adding to unallocated...')

        @patch.dict('App.room.Room.total_rooms', {'oculus': []})
        @patch.dict('App.person.Person.total_people', {1: 'Migwi'})
        @patch('App.room.Room.offices')
        @patch('App.room.Room.livingspaces')
        @patch('App.person.Person.fellows')
        @patch('App.person.Person.staff')
        def test_response_on_no_rooms(self, mock_staff, mock_fellows, mock_livingspaces, mock_offices):
                mock_offices.__iter__.return_value = ['oculus']
                mock_livingspaces.__iter__.return_value = []
                mock_fellows.__iter__.return_value = []
                mock_staff.__iter__.return_value = []

                msg = self.person.add_person('joan', 'ngugi', 'Fellow', 'Y')
                self.assertEqual(msg, "There are currently no livingspaces")


        @patch.dict('App.room.Room.total_rooms', {'oculus': [1], 'mordor': [], 'shire':[23,43,52,12,32,32], 'haskel': []})
        @patch.dict('App.person.Person.total_people', {1: 'Migwi'})
        @patch('App.room.Room.offices')
        @patch('App.room.Room.livingspaces')
        @patch('App.person.Person.fellows')
        @patch('App.person.Person.staff')
        def test_reallocation(self, mock_staff, mock_fellows, mock_livingspaces, mock_offices):
                mock_livingspaces.__iter__.return_value = ['haskel']
                mock_offices.__iter__.return_value = ['oculus', 'mordor', 'shire']
                mock_fellows.__iter__.return_value = ['Migwi']
                mock_staff.__iter__.return_value = []

                fully_occupied = self.person.reallocate_person(1, 'shire')
                self.assertEqual(fully_occupied, "Sorry the office is occupied fully")

                already_present = self.person.reallocate_person(1, 'oculus')
                self.assertEqual(already_present, "The Person is already allocated in the requested room")

                msg = self.person.reallocate_person(1, 'mordor')
                self.assertEqual(msg, "Allocation to New office successfull!")

                person_msg = self.person.reallocate_person(3, 'mordor')
                self.assertEqual(person_msg, "The person ID does not exist!")

                room_msg = self.person.reallocate_person(1, 'shell')
                self.assertEqual(room_msg, "The room doesn't exist!")

        @patch('App.person.Person.add_person')
        def test_loads_people(self, mock_add_person):
                mock_add_person.return_value = ''
                sample_read_text = 'OLUWAFEMI SULE FELLOW Y'
                with patch("__builtin__.open", mock_open(read_data=sample_read_text)) as mock_file:
                        self.person.load_people_data('list.txt')
                # assert open("people.txt", 'r').readlines() == sample_read_text
                mock_file.assert_called_with("list.txt")


        def test_printing_unallocated(self):
                # self.person.print_unallocated('unallocated')
                # self.assertIsNotNone('unallocated')
                pass




if __name__ == '__main__':
        unittest.main()
