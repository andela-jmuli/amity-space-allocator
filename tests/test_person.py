import unittest
import os
from App.person import Person


class TestPerson(unittest.TestCase):

        def setUp(self):
                self.person = Person()

        def test_person_class_instance(self):
                self.assertIsInstance(self.person, Person)


        def test_it_creates_a_person(self):
                self.person.add_person('Joseph', 'Muli', 'Fellow', 'Yes')
                self.assertEqual(self.person.first_name, 'Joseph')


        def test_reallocation(self):
                self.person.reallocate_person(1, 'oculus')
                self.assertEqual(self.person.room_name, 'oculus')


        def test_loads_people(self):
                test_file = self.person.load_people('list.txt')
                self.assertEqual(self.person.total_people, 5)


        def test_printing_unallocated(self):
                pass




if __name__ == '__main__':
        unittest.main()
