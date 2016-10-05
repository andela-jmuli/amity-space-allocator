from amity import Amity


class Room(Amity):
        """ Room class subclasses Amity and is super to Office and LIvingSpace
                Room also defines the common attributes between Office and LivingSpace
        """
        def __init__(self):
                super(Amity, self).__init__()
                self.offices = []
                self.livingspaces = []
                self.total_rooms = []
                self.total_people = []
                self.room_occupants = []


        def create_room(self, *args):
                # first checks length of args(number of room names provided)
                if len(args) > 1:
                        new_rooms = []
                        for items in args:
                                new_rooms.append(items)
                        for room in new_rooms:
                                self.room_name = room
                                # add new rooms to total rooms list
                                self.total_rooms.append(room)
                else:
                        for item in args:
                                self.room_name = item
                                # add new room to total rooms list
                                self.total_rooms.append(item)


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


        def allocate_room_type(self, room_name, room_type):
                # first checks whether room exists in total_rooms list
                if room_name not in self.total_rooms:
                        return "The room doesn't exist"

                # appends room to office list if type defined == office
                if room_type == 'Office':
                        self.offices.append(room_name)

                # appends room to livingspace if type defined == livingspace
                elif room_type == 'LivingSpace':
                        self.livingspaces.append(room_name)


        def print_allocations(self, filename, *args):
                # loop through all rooms
                for room in self.total_rooms:
                        data +=  '{0}'.format(room.room_name)
                        if room.room_occupants:
                                for person in room.room_occupants:
                                        # save to output object
                                        data +=  '{0}'.format(person.p_name)
                        else:
                                data +=  "The room is currently empty"
                        return data
                if '-o' in args:
                        with open('allocations.txt', 'w') as f:
                                # write data as output
                                write_allocations = f.write(data)

