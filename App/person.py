from amity import Amity
from room import Room

import os
import random

class Person(Amity):
        """ Person subclasses Amity and is super to Fellow and Staff
                Person defines the main attributes and methods common
                to both Fellow and Class
         """
        def __init__(self):
            super(Amity, self).__init__()
            self.total_people = []
            self.total_rooms = []



        def add_person(self, first_name, last_name, job_type, wants_accomodation):
            """
            Adds a person to the system and allocates a random room
            """
                self.first_name = first_name
                self.last_name = last_name
                self.job_type = job_type
                self.wants_accomodation = wants_accomodation


                p_name = first_name + last_name
                # add new person to the total people list
                self.total_people.append(p_name)

                if wants_accomodation == 'Y':
                    if len(self.total_rooms) > 1:
                        # allocates a random room to the new person added
                        allocated_room = random.choice(self.total_rooms)

                        # adds new person as an occupant of the selected room
                        allocated_room.room_occupants.append(p_name)
                        return "Person allocated to room"
                    else:
                        return "There are currently no rooms in Amity"


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


        def print_unallocated(self, filename):
            """
            prints out unallocated people to a specified file
            """
                pass

