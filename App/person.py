import os

from amity import Amity
# import database
from models import AmityPerson
from models import AmityRoom
from room import Room
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from collections import defaultdict
from random import randint
import pickle
import random

engine = create_engine('sqlite:///amity.db', echo = False)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Person(Amity):
        """ Person subclasses Amity and is super to Fellow and Staff
                Person defines the main attributes and methods common
                to both Fellow and Class
         """

        total_people = {}
        staff = []
        unallocated_people = []
        allocated_people = []
        fellows = []
        fellows_not_allocated_office = []
        staff_not_allocated_office = []

        def __init__(self):
            super(Amity, self).__init__()
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
            self.username = first_name + last_name
            # add new person to the total people list with a new ID

            # add new person to the total people list with a new ID
            total_ids = len(Person.total_people)
            new_person_id = total_ids + 1
            self.person_id = new_person_id

            # Append the user to the people dictionary
            Person.total_people[new_person_id] = self.username

            # check the person's job type
            if job_type == 'Fellow' or job_type == 'FELLOW' or job_type == 'fellow':
                Person.fellows.append(self.username)

                # check if offices are available
                if len(Room.offices) <= 0:

                    Person.fellows_not_allocated_office.append(self.username)
                    print "There are no offices available, adding to unallocated-without-offices..."
                else:
                    # allocate an office to the new fellow
                    allocated_office = random.choice(Room.offices)

                    if len(Room.total_rooms[allocated_office]) < 6:
                        Room.total_rooms[allocated_office].append(self.person_id)
                    else:
                        Person.fellows_not_allocated_office.append(self.username)
                        return "sorry all offices are currently fully occupied, adding to unallocated-without-offices..."

                if wants_accomodation == 'Y':
                    # sanity check for empty list
                    if len(Room.livingspaces) <= 0:
                        return "There are currently no livingspaces"
                    else:
                        # allocate a random livingspace
                        allocated_livingspace = random.choice(Room.livingspaces)

                        # allocate the new person as an occupant of the livingspace
                        if len(Room.total_rooms[allocated_livingspace]) < 4:
                            Room.total_rooms[allocated_livingspace].append(self.person_id)

                        else:
                            Person.unallocated_people.append(self.username)
                            return "sorry all livingspaces are currently fully occupied, adding to unallocated..."


                elif wants_accomodation == 'N':
                    Person.unallocated_people.append(self.username)

            elif job_type == 'Staff' or job_type == 'STAFF' or job_type == 'staff':

                Person.staff.append(self.username)
                allocated_office = random.choice(Room.offices)

                if len(Room.total_rooms[allocated_office]) < 6:
                    Room.total_rooms[allocated_office].append(self.person_id)

                else:
                    Person.staff_not_allocated_office.append(self.username)
                    print "sorry all offices are currently fully occupied, adding to unallocated-without-offices..."

                if wants_accomodation == 'Y':
                    return "Staff members are not allocated livingspaces"
                else:
                    return "Staff member added successfully"

        def print_unallocated(self, *args):
            """
            prints out unallocated people to a specified file
            """

            # if file output option specified in arguments, write to file
            if '-o' in args:
                with open(unallocated, 'wb') as f:
                    pickle.dump(Person.unallocated_people, f)
            # if file output option not specified, write to screen(console)
            else:
                print "A for fellows without living spaces"
                print "B for fellows without offices"
                print "C for staff members without offices"
                choice = raw_input ("What would you like to print?")

                if choice == 'A':
                    for person in Person.unallocated_people:
                        if len(Person.unallocated_people) > 0:
                            print person
                        else:
                            return "All fellows are currently allocated"

                elif choice == 'B':
                    for person in Person.fellows_not_allocated_office:
                        if len(Person.fellows_not_allocated_office) > 0:
                            print person
                        else:
                            return "All fellows have working spaces"

                elif choice == 'C':
                    for person in Person.staff_not_allocated_office:
                        if len(Person.staff_not_allocated_office) > 0:
                            print person
                        else:
                            return "All staff members have working spaces"
                else:
                    return "Snap! please try again"

        def reallocate_person(self, person_id, room_name):
            """
            Reallocates a person to a new room
            """
            # check for the person's existance
            if person_id not in Person.total_people.keys():
                return "The person ID does not exist!"

            # check for the room's existance
            if room_name not in Room.total_rooms.keys():
                return "The room doesn't exist!"

            # check whether the person is already in the allocated room
            for room in Room.total_rooms.keys():
                if room == room_name:
                    for occupant in Room.total_rooms[room]:
                        if person_id == occupant:
                            return "The Person is already allocated in the requested room"

            # start office allocation, if room is an office
            if room_name in Room.offices:

                for key in Room.total_rooms.keys():
                    if key == room_name:
                        if len(Room.total_rooms[room_name]) > 6:
                            return "Sorry the office is occupied fully"
                        else:
                            Room.total_rooms[room_name].append(person_id)


                for room in Room.total_rooms.keys():
                    if room != room_name and room not in Room.livingspaces:
                        for occupant in Room.total_rooms[room]:
                            if person_id == occupant:
                                Room.total_rooms[room].remove(person_id)
                                print "Allocation to New office successfull!"

            # start livingspace re-allocation if room is a livingspace
            elif room_name in Room.livingspaces:
                for id in Person.total_people:
                    if person_id == Person.total_people[id]:
                        username = username
                        if username in Person.staff:
                            return "Staff members are not allocated living spaces"

                for key in Room.total_rooms.keys():
                    if key == room_name:
                        if len(Room.total_rooms[room_name]) > 4:
                            return "Sorry the LivingSpace is currently fully occupied!"
                        else:
                            Room.total_rooms[room_name].append(person_id)

                for room in Room.total_rooms.keys():
                    if room != room_name and room not in Room.offices:
                        for occupant in Room.total_rooms[room]:
                            if person_id == occupant:
                                Room.total_rooms[room].remove(person_id)
                                print "Allocation to New livingSpace successful!"

        def load_people_data(self, filename):
            """
            Adds people to rooms from a text file
            """
            # check whether the file specified exists
            if os.path.exists(filename):
                with open(filename) as input:

                    # file data is added to content as a list where each line is an element
                    content = input.readlines()

                    # if file is empty return message
                    if len(content) == 0:
                        return "The file is empty"
                    else:
                        for line in content:
                            person_data = line.split()
                            first_name = person_data[0]
                            last_name = person_data[1]
                            job_type = person_data[2]
                            try:
                                accomodation = person_data[3]
                            except Exception:
                                accomodation = 'N'
                            person = Person()
                            person.add_person(first_name, last_name, job_type, accomodation)

                        return "File data added successfully"
            else:
                return "The file doesn't exist"

        @staticmethod
        def commit_people(db_name):
            """
            method called to commit person objects to database class
            """
            global engine
            engine = create_engine('sqlite:///'+db_name, echo = True)
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            for key in Person.total_people.keys():
                person_id = key
                username = Person.total_people[key]
                if username in Person.fellows:
                    job_type = 'fellow'
                    import ipdb; ipdb.set_trace()
                    # check whether person has an office
                    if username in Person.fellows_not_allocated_office:
                        allocated_office = 'unallocated'
                    else:
                        for room in Room.total_rooms:
                            if room in Room.offices:
                                for occupant in Room.total_rooms[room]:
                                    if person_id == occupant:
                                        allocated_office = room

                    # check whether fellow has a living space
                    if username in Person.unallocated_people:
                        is_accomodated = False
                        allocated_livingspace = 'unallocated'
                    else:
                        is_accomodated = True
                        for room in Room.total_rooms:
                            if room in Room.livingspaces:
                                for occupant in Room.total_rooms[room]:
                                    if person_id == occupant:
                                        allocated_livingspace = room

                # if the person is a staff...
                elif username in Person.staff:
                    job_type = 'staff'
                    allocated_livingspace = 'unallocated'
                    if username in Person.staff_not_allocated_office:
                        is_accomodated = False
                        allocated_office = 'unallocated'
                    else:
                        for room in Room.total_rooms:
                            if room in Room.offices:
                                for occupant in Room.total_rooms[room]:
                                    if person_id == occupant:
                                        allocated_office = room
                # commit person data as an object of AmityPerson class (database table for Person)
                person_info = AmityPerson(person_id=person_id, username=username, job_type=job_type, is_accomodated=is_accomodated, allocated_livingspace=allocated_livingspace, allocated_office=allocated_office)
                try:
                    session.add(person_info)
                    session.commit()
                except Exception:
                    return "person data save not successful"

        @staticmethod
        def load_people(db_name):
            """
            method called to load person data from database tables to respective data structures
            """
            global engine
            engine = create_engine('sqlite:///'+db_name, echo = True)
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            all_people = session.query(AmityPerson).all()
            all_fellows = session.query(AmityPerson).filter_by(job_type="fellow")
            all_staff = session.query(AmityPerson).filter_by(job_type="staff")
            all_unallocated = session.query(AmityPerson).filter_by(is_accomodated="0")
            rooms = session.query(AmityRoom).all()

            # Adds people to the people dictionary
            for person in all_people:
                username = str(person.username)
                id = int(person.person_id)
                temporary = []
                temporary.append(username)
                for user in temporary:
                    Person.total_people[id] = username

            # get the fellows
            for person in all_fellows:
                username = str(person.username)
                Person.fellows.append(username)

            # get the staff
            for person in all_staff:
                username = str(person.username)
                Person.staff.append(username)

            # get unallocated
            for person in all_unallocated:
                username = str(person.username)
                Person.unallocated_people.append(username)

            # start allocations
            for room in rooms:
                room_name = str(room.room_name)
                room_type = str(room.room_type)
                if room_type == 'office':
                    for person in all_people:
                        username = str(person.username)
                        id = int(person.person_id)
                        if person.allocated_office == room_name:
                            Room.total_rooms[room_name].append(id)
                elif room_type == 'livingspace':
                    for person in all_people:
                        username = str(person.username)
                        id = int(person.person_id)
                        if person.allocated_livingspace == room_name:
                            Room.total_rooms[room_name].append(id)

            return "People loaded successfully"

