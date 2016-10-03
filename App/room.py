from amity import Amity


class Room(object):
        """ Room class subclasses Amity and is super to Office and LIvingSpace
                Room also defines the common attributes between Office and LivingSpace
        """
        def __init__(self):
                pass


        def create_room(self, *args):
                if len(args) > 1:
                        new_room = []
                        for items in args:
                                new_room.append(items)
                        print new_room
                        for room in new_room:
                                self.room_name = room
                                # item.room_name = room_name
                else:
                        # item.room_name = room_name
                        for item in args:
                                self.room_name = item


        def print_room(self, args):
                pass


        def print_allocations(self, args):
                pass


