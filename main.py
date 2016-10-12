"""
    Commands:
        create_room <room_name>
        allocate_room_type <room_name> <room_type>
        add_person <first_name> <last_name> <job_type> [accomodation]
        reallocate_person <person_id> <room_name>
        load_people <filename>
        print_allocations [--o=filename]
        print_unallocated [--o=filename]
        print_room <room_name>
        save_state [--db=sqlite_db]
        load_state <sqlite_db>
        quit

    Options:
        -h, --help  Show this screen and exit
        -o filename  Specify filename
        --db    Name of SQLite DB
        --accomodation - prompt on whether one wants or doesn't want accomodation [default='N']
"""


from docopt import docopt, DocoptExit
import cmd
import os
from pyfiglet import figlet_format
from App.person import Person
from App.room import Room
from App.database import AmityDatabase



def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def intro():
    os.system("clear")
    print(figlet_format('AMITY', font='cosmic'))
    print('------------------------------------------------------------------------')
    print('Amity is an automated Allocation System')
    print('------------------------------------------------------------------------')
    print('To get started, enter "help" to view the available commands')


class Amitizer(cmd.Cmd):
    prompt = 'allocator@amity ~ '

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_name>..."""
        room = Room()
        rooms = arg['<room_name>']
        for rm in rooms:
            status = room.create_room(rm)
            print(status)

    @docopt_cmd
    def do_allocate_room_type(self, arg):
        """Usage: create_room <room_name>"""
        room = Room()
        room_name = arg['<room_name>']
        room_type = arg['<room_type>']
        status = room.allocate_room_type(room_name, room_type)
        print(status)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <job_type> [--accomodation]"""
        person = Person()
        first_name = arg['<first_name>']
        last_name = arg['<last_name>']
        job_type = arg['<job_type>']
        accomodation = arg['<accomodation>']
        added_status = person.add_person(first_name, last_name, job_type, accomodation)
        print(added_status)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person  <person_id> <room_name>"""
        person = Person()
        person_id = arg['<person_id>']
        room_name = arg['<room_name>']
        allocate_status = person.reallocate_person(person_id, room_name)
        print(allocate_status)

    @docopt_cmd
    def do_load_people(self, arg):
        '''Usage: load_people <filename>'''
        person = Person()
        status = person.load_people(arg['<filename>'])
        print(status)

    @docopt_cmd
    def do_print_allocations(self, arg):
        '''Usage: print_allocations [--o=filename]'''
        room = Room()
        file = arg['<filename>']
        option = arg['<-o>']
        if file is not None:
            if option in arg:
                room.print_allocations(file)
        else:
            room.print_allocations()

    @docopt_cmd
    def do_print_unallocated(self, arg):
        '''Usage: print_unallocated [filename]'''
        person = Person()
        file = arg['<filename>']
        status = person.print_unallocated(file)
        print(status)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        room = Room()
        room_name = arg['<room_name>']
        room.print_room(room_name)

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db=sqlitedb]"""

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <sqlite_database>"""

    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        print("Shutting Down Amity......")
        exit()

if __name__ == "__main__":
    intro()
    Amitizer().cmdloop()
