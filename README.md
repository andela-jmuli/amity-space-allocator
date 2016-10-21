

# Amity Space Allocator

## Introduction:
Amity Space Allocator is a console application that allocates rooms to fellows and staff members.

## Dependencies:

## Installation and Setup:

* Navigate to your directory choice
* Clone the repository:
 * Using SSH: ``` data ```
 * Using HTTP ``` data ```
* Setup a virtualenvironment for dependencies:
 * virtualenv {{ desired name }}
* Activate your environment
 * ``` cd ``` into folder and run ``` source bin/activate ```
* Install the dependencies:
 * ``` pip install -r reqiuirements.txt ```

## Usage:
create_room <room_name>... - Creates rooms in Amity. Using this command I should be able to create as many rooms as possible by specifying multiple room names after the create_room command.
add_person <person_name> <FELLOW|STAFF> [wants_accommodation] - Adds a person to the system and allocates the person to a random room. wants_accommodation here is an optional argument which can be either Y or N. The default value if it is not provided is N.
reallocate_person <person_identifier> <new_room_name> - Reallocate the person with person_identifier to new_room_name.
load_people - Adds people to rooms from a txt file. See Appendix 1A for text input format.
print_allocations [-o=filename]  - Prints a list of allocations onto the screen. Specifying the optional -o option here outputs the registered allocations to a txt file. See Appendix 2A for format.
print_unallocated [-o=filename] - Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the txt file provided.
print_room <room_name> - Prints  the names of all the people in room_name on the screen.
save_state [--db=sqlite_database] - Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified.
load_state <sqlite_database> - Loads data from a database into the application.

## Testing:
To test, run the command ``` nosetests ```

## Licence:

## Credits:
* [Joseph Muli](github.com/andela-jmuli)
