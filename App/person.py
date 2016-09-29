from amity import Amity


class Person(Amity):
        """ Person subclasses Amity and is super to Fellow and Staff
                Person defines the main attributes and methods common
                to both Fellow and Class
         """
        def __init__(self):
                pass


        def add_person(self, args):
                pass


        def reallocate_person(self, args):
                pass


        def load_people(self, args):
                pass


        def print_unallocated(self, args):
                pass


class Staff(Person):

    def __init__(self):
        pass



class Fellow(Person):

    def __init__(self):
        pass
