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
                total_before = len(self.person.total_people)
                self.room.create_room('oculus')
                self.room.allocate_room_type('oculus', 'Office')
                self.person.add_person('Joseph', 'Muli', 'Fellow', 'Y')
                self.person.add_person('Michael', 'Kamau', 'Fellow', 'Y')
                total_after = len(self.person.total_people)
                print self.person.total_people
                self.assertEqual((total_after - total_before), 2)

        def test_reallocation(self):
                self.room.create_room('mordor')
                self.room.allocate_room_type('mordor', 'Office')
                self.person.reallocate_person(1, 'mordor')
                self.assertIn(1, self.room.total_rooms['mordor'])

        def test_loads_people(self):
                test_file = self.person.load_people('list.txt')
                self.assertEqual(len(self.person.total_people), 5)
                pass

        def test_printing_unallocated(self):
                self.person.print_unallocated('unallocated')
                self.assertIsNotNone('unallocated')




if __name__ == '__main__':
        unittest.main()
