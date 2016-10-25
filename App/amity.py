
class Amity(object):
        """Amity is the SuperClass to Rooms and Person Classes"""
        def __init__(self):
                self.total_rooms = []
                self.total_people = []
                self.room_occupants = []
                self.offices = []
                self.livingspaces = []
                self.allocated_office = None
                self.allocated_livingspace = None
