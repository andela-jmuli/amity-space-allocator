

# Amity Space Allocator

## Introduction:
Amity Space Allocator is a console application that allocates rooms to fellows and staff members.

## Dependencies:

1. [Docopt](http://docopt.org/)
2. [SQLAlchemy](http://www.sqlalchemy.org/)
3. [Python Mock lib](https://docs.python.org/3/library/unittest.mock.html)
4. [Python 2.7](https://www.python.org/)


## Installation and Setup:

* Navigate to your directory choice
* Clone the repository:
 * Using SSH: ``` git@github.com:andela-jmuli/amity-space-allocator.git ```
 * Using HTTP ``` https://github.com/andela-jmuli/amity-space-allocator.git ```
* Setup a virtualenvironment for dependencies:
 * virtualenv {{ desired name }}
* Activate your environment
 * ``` cd ``` into folder and run ``` source bin/activate ```
* Install the dependencies:
 * ``` pip install -r reqiuirements.txt ```

## Usage:
***create_room*** ```<room_name>```
Creates rooms in Amity. This command creates as many rooms as possible by specifying multiple room names after the create_room command.

***allocate_room_type*** ```<room_name> <Office| LivingSpace>```
Assign a room type, can be an office or livingspace, failure to which rooms will not accept allocations.  

***add_person*** ```<person_name> <FELLOW|STAFF> [wants_accommodation]```
Adds a person to the system and allocates the person to a random room. wants_accommodation here is an optional argument which can be either Yes or No. The default value if it is not provided is No.

***reallocate_person*** ```<person_identifier> <new_room_name>```
Reallocate the person with person_identifier to new_room_name.

***load_people*** ```<filename>```
Adds people to rooms from a txt file.

***print_allocations*** ```[-o=filename]```
Prints a list of allocations onto the screen. Specifying the optional -o option here outputs the registered allocations to a txt file.

***print_unallocated*** ```[-o=filename]```
Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the txt file provided.

***print_room*** ```<room_name>```
Prints  the names of all the people in room_name on the screen.

***save_state***  ```[--db=sqlite_database]```
Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified.

***load_state*** ```<sqlite_database>```
Loads data from a database into the application.


## Testing:
To test, run the command ``` nosetests ```

## Licence:
Check out the License file for more information

## Credits:
* [Joseph Muli](github.com/andela-jmuli)
