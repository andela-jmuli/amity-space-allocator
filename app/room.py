from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import person
from amity import Amity
from models import AmityRoom


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
        for item in args:
            if item in Room.total_rooms.keys():
                return "A room with that name already exists!"
        if len(args) >= 1:
            new_rooms = []
            for items in args:
                new_rooms.append(items)

            for room in new_rooms:
                self.room_name = room
                # add new rooms to total rooms dictionary
                Room.total_rooms[room] = []
            return "Rooms have been successfully created"
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
                    return "There are currently no occupants in {0}".format(rm)
                else:
                    for occupant in Room.total_rooms[room_name]:
                        for person_id in person.Person.total_people:
                            if person_id == occupant:
                                occupant_name = person.Person.total_people[person_id]
                                print occupant_name

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
            return "{0} has been added as an Office".format(room_name)

        # appends room to livingspace if type defined == livingspace
        elif room_type == 'LivingSpace':
            Room.livingspaces.append(room_name)
            return "{0} has been added as a LivingSpace".format(room_name)

    def print_allocations(self, *args):
        """
        Prints out a list of allocations -- room name and occupants -- an option to
        write to a specified file if '-o' is included as an argument
                """

        # loop through all rooms
        print "Room Allocation Data:"
        print '**********************'
        print " ID ----- Person Name"
        print '                                  '
        for room in Room.total_rooms.keys():
            if room in Room.offices:
                print '### ### {0} office occupants ######'.format(room)
            else:
                print '###### {0} living space occupants ######'.format(room)
            if len(Room.total_rooms[room]) < 1:
                print '------------------------------------------------------------------------'
                print "There are currently no occupants in {0}".format(room)
            else:
                for occupant in Room.total_rooms[room]:
                    for person_id in person.Person.total_people.keys():
                        if occupant == person_id:
                            person_name = person.Person.total_people[person_id]
                            if person_name in person.Person.fellows:
                                print "{0}, F ----- {1}".format(person_id, person_name)
                            elif person_name in person.Person.staff:
                                print "{0}, S ----- {1}".format(person_id, person_name)

    @staticmethod
    def commit_rooms(db_name):
        """
        Loads rooms from the total_rooms dictionary and commits to database
                """
        engine = create_engine('sqlite:///' + db_name, echo=False)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        # loop through all rooms dictionary and get room names which are the keys
        for room in Room.total_rooms.keys():
            room_name = room
            #  check for room type and capacity
            if room in list(Room.offices):
                room_type = 'office'
                room_capacity = 6
            elif room in list(Room.livingspaces):
                room_type = 'livingspace'
                room_capacity = 4

            amity_room = AmityRoom(room_name=room_name, room_type=room_type, capacity=room_capacity)

            session.add(amity_room)
            session.commit()
            session.close()

        return "rooms committed to session"

    @staticmethod
    def load_rooms(db_name):
        engine = create_engine('sqlite:///' + db_name, echo=False)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        all_rooms = session.query(AmityRoom).all()

        for room in all_rooms:
            room_name = str(room.room_name)
            room_type = str(room.room_type)
            if "office" in str(room.room_type):
                Room.offices.append(room_name)
            else:
                Room.livingspaces.append(room_name)
            Room.total_rooms[room_name] = []
        return 'Room data added successfully'
