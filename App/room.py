from amity import Amity


class Room(Amity):
        """ Room class subclasses Amity and is super to Office and LIvingSpace
                Room also defines the common attributes between Office and LivingSpace
        """
        def __init__(self, room_name, room_type):
                self.room_name = room_name
                self.room_type = room_type


        def create_room(self, room_name):
                pass


        def print_room(self, args):
                pass


        def print_allocations(self, args):
                pass
