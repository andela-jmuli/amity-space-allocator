from amity import Amity
from room import Room

from random import randint

import os
import pickle
import random


class Person(Amity):
        """ Person subclasses Amity and is super to Fellow and Staff
                Person defines the main attributes and methods common
                to both Fellow and Class
         """
        total_people = {}
        # people_ids = len(total_people)
        def __init__(self):
            super(Amity, self).__init__()
            self.fellows = []
            self.staff = []
            self.allocated_people = []
            self.unallocated_people = []
            self.allocated_office = None
            self.allocated_livingspace = None

        def add_person(self, first_name, last_name, job_type, wants_accomodation):
            """
            Adds a person to the system and allocates a random room
            """
            self.first_name = first_name
            self.last_name = last_name
            self.job_type = job_type
            self.wants_accomodation = wants_accomodation

            p_name = first_name + last_name
            # add new person to the total people list with a new ID

            total_ids = len(Person.total_people)
            new_person_id = total_ids + 1

            Person.total_people[new_person_id] = p_name

            # check the person's job type
            if job_type == 'Fellow':
                self.fellows.append(p_name)

                # sanity check for empty list errors
                if len(Room.offices) > 1:
                    # allocate an office to the new fellow
                    self.allocated_office = random.choice(Room.total_rooms.items())
                else:
                    print "There are currently no offices"


                if wants_accomodation == 'Y':
                    # sanity check for empty list
                    if len(Room.livingspaces) > 1:
                        # allocate a random livingspace
                        self.allocated_livingspace = random.choice(self.livingspaces)
                    else:
                        print "There are currently no livingspaces"

                elif wants_accomodation == 'N':
                    self.unallocated_people.append(p_name)


            elif job_type == 'Staff':
                self.staff.append(p_name)
                self.allocated_office = random.choice(self.offices)

                if wants_accomodation == 'Y':
                    return "Staff members are not allocated livingspaces"

        def print_unallocated(self, filename, *args):
            """
            prints out unallocated people to a specified file
            """
            # if file output option specified in arguments, write to file
            if '-o' in args:
                with open(unallocated, 'wb') as f:
                    pickle.dump(self.unallocated_people, f)
            # if file output option not specified, write to screen(console)
            else:
                for person in self.unallocated_people:
                    print person

        def reallocate_person(self, person_id, room_name):
            """
            Reallocates a person to a new room
            """
            pass

        def load_people(self, filename):
            """
            Adds people to rooms from a text file
            """
            pass
