import unittest
import os
from App.person import Person
from App.room import Room



class TestPerson(unittest.TestCase):

        def setUp(self):
                self.person = Person()
                self.room = Room()

        def test_person_class_instance(self):
                self.assertIsInstance(self.person, Person)

        def test_it_adds_a_person(self):
                self.person.add_person('Joseph', 'Muli', 'Fellow', 'Y')
                self.person.add_person('Michael', 'Kamau', 'Fellow', 'Y')
                self.assertEqual(len(self.person.total_people), 2)

        def test_reallocation(self):
                self.room.create_room('oculus')
                self.person.add_person('Joseph', 'Muli', 'Fellow', 'Y')
                self.person.reallocate_person(1, 'oculus')
                self.assertIn(self.person.username, Room.total_rooms['oculus'])

        def test_loads_people(self):
                test_file = self.person.load_people('list.txt')
                self.assertEqual(len(self.person.total_people), 5)
                pass

        def test_printing_unallocated(self):
                self.person.print_unallocated('unallocated')
                self.assertIsNotNone('unallocated')




if __name__ == '__main__':
        unittest.main()
