import os
from models import AmityRoom
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from amity import Amity
import person


class Room(Amity):
        """ Room class subclasses Amity and is super to Office and LIvingSpace
                Room also defines the common attributes between Office and LivingSpace
        """
        total_rooms = {}
        offices = []
        livingspaces = []

        def __init__(self, offices=offices, total_rooms=total_rooms):
                super(Amity, self).__init__()
                self.offices = offices
                self.total_rooms = total_rooms

        def create_room(self, *args):
                """
        This method creates rooms based on the input provided ~ multiple arguments suggest multiple rooms created
                """
                # first checks length of args(number of room names provided)
                if len(args) >= 1:
                        new_rooms = []
                        for items in args:
                                new_rooms.append(items)

                        for room in new_rooms:
                                self.room_name = room
                                # add new rooms to total rooms dictionary
                                Room.total_rooms[room]= []
                elif len(args) < 1:
                        return "You can't create an empty room!"

        def print_room(self, room_name):
                """
                This method prints out the name of all the people in the specified room
                """
                for rm in Room.total_rooms.keys():
                        # first check whether room is existent as key of total_rooms dict.
                        if room_name not in Room.total_rooms:
                                return "The room does not exist!"

                        # loop through rooms and identify
                        if rm == room_name:
                                # check number of occupants
                                if len(Room.total_rooms[rm]) < 1:
                                        print '------------------------------------------------------------------------'
                                        return "There are currently no occupants in {0}".format(rm)
                                else:
                                        for occupant, person_id in zip(Room.total_rooms[rm], person.Person.total_people.keys()):
                                                if occupant == person_id:
                                                        person_name = person.Person.total_people[person_id]
                                                        print '--------------------------------------'
                                                        print person_name


        def allocate_room_type(self, room_name, room_type):
                """
                This method allocates a room as either an office or livingspace
                """

                # first checks whether room exists in total_rooms list
                if room_name not in Room.total_rooms:
                        return "The room doesn't exist"

                # appends room to office list if type defined == office
                if room_type == 'Office':
                        Room.offices.append(room_name)

                # appends room to livingspace if type defined == livingspace
                elif room_type == 'LivingSpace':
                        Room.livingspaces.append(room_name)

        def print_allocations(self, *args):
                """
        Prints out a list of allocations -- room name and occupants -- an option to
        write to a specified file if '-o' is included as an argument
                """

                # loop through all rooms
                print "Room Allocation Data:"
                print '--------------------------------------'
                for room in Room.total_rooms.keys():
                        room_name = '{0}'.format(room)
                        print room_name

                        print '----------- {0} Occupants--------------'.format(room_name)
                        if len(Room.total_rooms[room]) < 1:
                                print '------------------------------------------------------------------------'
                                return "There are currently no occupants in {0}".format(room)
                        else:
                                for occupant, person_id in zip(Room.total_rooms[room], person.Person.total_people.keys()):
                                        if occupant == person_id:
                                                person_name = person.Person.total_people[person_id]
                                                print person_name
                                                print '--------------------------------------'

                if '-o' in args:
                        with open('allocations', 'wb') as f:
                                # write data as output
                                write_allocations = f.write(data)

        def commit_rooms(self, amity_session):
                """
        Loads rooms from the total_rooms dictionary and commits to database
                """
                for room in Room.total_rooms.keys():
                        room_name = room
                for rm in Room.offices:
                        if rm in Room.offices:
                                room_type = 'office'
                                room_capacity = 6
                        elif rm in Room.livingspaces:
                                room_type = 'livingspace'
                                room_capacity = 4
                amity_room = AmityRoom(room_name=room_name, room_type=room_type, capacity=room_capacity)

                try:
                        amity_session.add(amity_room)
                except Exception:
                        return "room data save Failed!"

        def commit_allocations(self):
                pass
