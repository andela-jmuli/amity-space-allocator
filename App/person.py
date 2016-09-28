from amity import Amity


class Person(Amity):
        """ Person subclasses Amity and is super to Fellow and Staff
                Person defines the main attributes and methods common
                to both Fellow and Class
         """
        def __init__(self, id, person_name, job_type):
                self.id = id
                self.person_name = person_name
                self.job_type = job_type


        def add_person(self, args):
                pass


        def reallocate_person(self, args):
                pass


        def load_people(self, args):
                pass


        def print_unallocated(self, args):
                pass
