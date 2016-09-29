from amity import Amity


class Room(object):
        """ Room class subclasses Amity and is super to Office and LIvingSpace
                Room also defines the common attributes between Office and LivingSpace
        """
        def __init__(self):
                pass


        def create_room(self, args):
                pass


        def print_room(self, args):
                pass


        def print_allocations(self, args):
                pass


class Office(Room):

        def __init__(self):
                pass

        max_capacity = 4


class LivingSpace(Room):

        def __init__(self):
                pass

        max_capacity = 6
