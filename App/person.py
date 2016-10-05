from amity import Amity

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
            self.room_occupants = []


        def add_person(self, first_name, last_name, type, accomodation):
                self.first_name = first_name
                self.last_name = last_name
                self.type = type
                self.accomodation = accomodation

                p_name = first_name + last_name
                # add new person to the total people list
                self.total_people.append(p_name)

                if accomodation == 'Y':
                    if len(self.total_rooms) > 1:

                        # allocates a random room to the new person added
                        self.person_room = random.choice(self.total_rooms)
                        # adds new person added as an occupant of the selected room
                        self.person_room.room_occupants.append(p_name)
                        return "Person allocated to room"
                    else:
                        return "There are currently no rooms in Amity"


            def print_room(self, room_name):
                for rm in self.total_rooms:
                        # first check whether room is existent
                        if room_name not in self.total_rooms:
                                return "The room does not exist!"

                        # loop through rooms and identify
                        if rm == room_name:
                                # check number of occupants
                                if rm.room_occupants > 1:
                                        for p in rm.room_occupants:
                                                print p
                                else:
                                        print "The room is empty!"



        def reallocate_person(self, person_id, room_name):
                pass


        def load_people(self, filename):
                pass


        def print_unallocated(self, filename):
                pass

