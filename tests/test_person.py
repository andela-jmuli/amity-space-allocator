import unittest
import os
from App.person import Person


class TestPerson(unittest.TestCase):

        # def setUp(self):
        #         self.person = Person()

        def test_person_class_instance(self):
                person = Person()
                self.assertIsInstance(person, Person)


        def test_it_creates_a_person(self):
                person = Person()
                person.add_person('Jojo', 'Fellow', 'Yes')
                self.assertEqual(person.person_name, 'Jojo')


        def test_reallocation(self):
                person = Person()
                person.reallocate_person(1, 'oculus')
                self.assertEqual(person.room_name, 'oculus')


        def test_loads_people(self):
                pass

        def test_printing_unallocated(self):
                pass




if __name__ == '__main__':
        unittest.main()
