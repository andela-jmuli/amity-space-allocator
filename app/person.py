import os

from amity import Amity
from models import AmityPerson
from models import AmityRoom
from room import Room
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

engine = create_engine('sqlite:///amity.db', echo=False)
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

        total_ids = len(Person.total_people)
        new_person_id = total_ids + 1
        self.person_id = new_person_id

        # Append the user to the people dictionary
        if self.username not in Person.total_people.values():
            Person.total_people[new_person_id] = self.username

            # check the person's job type
            if job_type == 'Fellow' or job_type == 'FELLOW' or job_type == 'fellow':
                list(Person.fellows).append(self.username)

                # check if offices are available
                if len(list(Room.offices)) <= 0:

                    list(Person.fellows_not_allocated_office).append(self.username)
                    print "There are no offices available, adding {0} to unallocated-without-offices...".format(
                        self.username)
                else:
                    # allocate an office to the new fellow
                    offices_with_spaces = []
                    for office in list(Room.offices):
                        if len(Room.total_rooms[office]) < 6:
                            offices_with_spaces.append(office)
                    try:
                        allocated_office = random.choice(offices_with_spaces)
                        Room.total_rooms[allocated_office].append(self.person_id)

                    except Exception:
                        print "sorry all offices are currently fully occupied, adding to unallocated-without-offices..."
                        list(Person.fellows_not_allocated_office).append(self.username)

                if wants_accomodation == 'Y':
                    # sanity check for empty list
                    if len(list(Room.livingspaces)) <= 0:
                        list(Person.unallocated_people).append(self.username)
                        return "There are currently no livingspaces"
                    else:
                        livingspaces_with_spaces = []
                        for livingspace in list(Room.livingspaces):
                            if len(Room.total_rooms[livingspace]) < 4:
                                livingspaces_with_spaces.append(livingspace)

                        try:
                            # allocate a random living space
                            allocated_livingspace = random.choice(livingspaces_with_spaces)
                            # allocate the new person as an occupant of the living space
                            Room.total_rooms[allocated_livingspace].append(self.person_id)
                        except Exception:
                            list(Person.unallocated_people).append(self.username)
                            return "sorry all living spaces are currently fully occupied, adding to unallocated..."

                elif wants_accomodation == 'N':
                    list(Person.unallocated_people).append(self.username)
                    return "{0} added to unallocated-people".format(self.username)

            elif job_type == 'Staff' or job_type == 'STAFF' or job_type == 'staff':

                list(Person.staff).append(self.username)
                offices_with_spaces = []
                for office in list(Room.offices):
                    if len(Room.total_rooms[office]) < 6:
                        offices_with_spaces.append(office)
                try:

                    allocated_office = random.choice(offices_with_spaces)
                    Room.total_rooms[allocated_office].append(self.person_id)

                except Exception:
                    list(Person.staff_not_allocated_office).append(self.username)
                    return "all offices are currently fully occupied, adding to staff-unallocated-without-offices..."

                if wants_accomodation == 'Y':
                    print "Staff member added successfully"
                    return "NOTE: Staff members are not allocated livings paces"
                else:
                    return "Staff member added successfully"
                    # return "{0} Added successfully".format(self.username)
        else:
            return "oops! Someone with the username {0} already exists".format(self.username)

    def print_unallocated(self, filename=None):
        """
        prints out unallocated people to a specified file
        """
        print "A for fellows without living spaces"
        print "B for fellows without offices"
        print "C for staff members without offices"
        choice = raw_input("What would you like to print?")

        if choice == 'A':
            if filename is not None:
                with open(filename, 'w') as f:
                    for person in Person.unallocated_people:
                        f.write(person)
            else:
                for person in Person.unallocated_people:
                    if len(Person.unallocated_people) > 0:
                        print person
                    else:
                        return "All fellows are currently allocated"

        elif choice == 'B':
            if filename is not None:
                with open(filename, 'w') as f:
                    for person in Person.fellows_not_allocated_office:
                        f.write(person)
            else:
                for person in Person.fellows_not_allocated_office:
                    if len(Person.fellows_not_allocated_office) > 0:
                        print person
                    else:
                        return "All fellows have working spaces"

        elif choice == 'C':
            if filename is not None:
                with open(filename, 'w') as f:
                    f.write(str(Person.staff_not_allocated_office))
            else:
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
        if person_id in Room.total_rooms[room_name]:
            return "The Person is already allocated in the requested room"

        # start office allocation, if room is an office
        if room_name in list(Room.offices):
            for key in Room.total_rooms.keys():
                if key == room_name:
                    if len(Room.total_rooms[room_name]) < 6:
                        Room.total_rooms[room_name].append(person_id)
                    else:
                        return "Sorry the office is occupied fully"

            for room in Room.total_rooms.keys():
                if room != room_name and room not in list(Room.livingspaces):
                    for occupant in Room.total_rooms[room]:
                        if person_id == occupant:
                            Room.total_rooms[room].remove(person_id)
                            for person in Person.total_people:
                                if person_id == Person.total_people[person_id]:
                                    person_name = username
                                    Room.staff_not_allocated_office.remove(person_name)
                            return "Allocation to New office successfull!"

        # start living space re-allocation if room is a livingspace
        elif room_name in list(Room.livingspaces):
            for id in Person.total_people:
                if person_id == id:
                    username = Person.total_people[id]
                    if username in list(Person.staff):
                        return "Staff members are not allocated living spaces"

            for key in Room.total_rooms.keys():
                if key == room_name:
                    if len(Room.total_rooms[room_name]) > 4:
                        return "Sorry the LivingSpace is currently fully occupied!"
                    else:
                        Room.total_rooms[room_name].append(person_id)

            for room in Room.total_rooms.keys():
                if room != room_name and room not in list(Room.offices):
                    if person_id in Room.total_rooms[room]:
                        Room.total_rooms[room].remove(person_id)
                        return "Allocation to New livingSpace successful!"

        else:
            return room_name + '  was not  Allocated'

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
                        # line = line[:line]
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

    @staticmethod
    def commit_people(db_name):
        """
        method called to commit person objects to database class
        """
        global engine
        engine = create_engine('sqlite:///' + db_name, echo=False)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        for key in Person.total_people.keys():
            person_id = key
            username = Person.total_people[key]
            job_type = ''
            allocated_livingspace = ''
            allocated_office = ''
            is_accomodated = False

            if username in list(Person.fellows):
                job_type = 'fellow'
                # check whether person has an office
                if username in list(Person.fellows_not_allocated_office):
                    allocated_office = 'unallocated'
                else:
                    for room in Room.total_rooms:
                        if room in list(Room.offices):
                            for occupant in Room.total_rooms[room]:
                                if person_id == occupant:
                                    allocated_office = room

                # check whether fellow has a living space
                if username in list(Person.unallocated_people):
                    is_accomodated = False
                    allocated_livingspace = 'unallocated'
                else:
                    is_accomodated = True
                    for room in Room.total_rooms:
                        if room in list(Room.livingspaces):
                            for occupant in Room.total_rooms[room]:
                                if person_id == occupant:
                                    allocated_livingspace = room

            # if the person is a staff...
            else:
                job_type = 'staff'
                allocated_livingspace = 'unallocated'
                if username in list(Person.staff_not_allocated_office):
                    is_accomodated = False
                    allocated_office = 'unallocated'
                else:
                    for room in Room.total_rooms:
                        if room in list(Room.offices):
                            for occupant in Room.total_rooms[room]:
                                if person_id == occupant:
                                    allocated_office = room

            # commit person data as an object of AmityPerson class (database table for Person)
            person_info = AmityPerson(person_id=person_id, username=username, job_type=job_type,
                                      is_accomodated=is_accomodated, allocated_livingspace=allocated_livingspace,
                                      allocated_office=allocated_office)

            session.add(person_info)
            session.commit()
            session.close()

        return "Person data commit successfull"

    @staticmethod
    def load_people(db_name):
        """
        method called to load person data from database tables to respective data structures
        """
        engine = create_engine('sqlite:///' + db_name, echo=False)
        session = sessionmaker()
        session.configure(bind=engine)
        session = Session()
        all_people = session.query(AmityPerson).all()
        all_fellows = session.query(AmityPerson).filter_by(job_type="fellow")
        fellows_without_livingspaces = session.query(AmityPerson).filter_by(
            allocated_livingspace="unallocated").filter_by(job_type="fellow")
        fellows_without_offices = session.query(AmityPerson).filter_by(allocated_office="unallocated").filter_by(
            job_type="fellow")
        staff_without_offices = session.query(AmityPerson).filter_by(allocated_office="unallocated").filter_by(
            job_type="staff")
        all_staff = session.query(AmityPerson).filter_by(job_type="staff")
        all_unallocated = session.query(AmityPerson).filter_by(is_accomodated="0")
        rooms = session.query(AmityRoom).all()

        # Adds people to the people dictionary
        for person in all_people:
            username = str(person.username)
            p_id = int(person.person_id)
            Person.total_people[p_id] = username

        # get the fellows
        for person in all_fellows:
            username = str(person.username)
            Person.fellows.append(username)

        # get the staff
        for person in all_staff:
            username = str(person.username)
            Person.staff.append(username)

        # get fellows not allocated offices
        for person in fellows_without_offices:
            username = str(person.username)
            Person.fellows_not_allocated_office.append(username)

        # get fellows not allocated livingspaces
        for person in fellows_without_livingspaces:
            username = str(person.username)
            Person.unallocated_people.append(username)

        # get staff members without offices
        for person in staff_without_offices:
            username = str(person.username)
            Person.staff_not_allocated_office.append(username)

        # start allocations
        for room in rooms:
            room_name = str(room.room_name)
            room_type = str(room.room_type)
            if room_type == 'office':
                for person in all_people:
                    username = str(person.username)
                    p_id = int(person.person_id)
                    if person.allocated_office == room_name:
                        Room.total_rooms[room_name].append(p_id)
            elif room_type == 'livingspace':
                for person in all_people:
                    username = str(person.username)
                    p_id = int(person.person_id)
                    if person.allocated_livingspace == room_name:
                        Room.total_rooms[room_name].append(p_id)

        return "People loaded successfully"
