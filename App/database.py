import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import room
import person
from models import Base, create_db


class AmityDatabase(object):

        def __init__(self):
                pass


        def save_state(self, db_name):
                if os.path.exists(db_name):
                        os.remove(db_name)
                create_db(db_name)

                try:
                        room.Room.commit_rooms(db_name)
                        person.Person.commit_people(db_name)
                except Exception as e:
                        print e
                        message = "Error saving data to database"

                return "Data Has been Saved to Database!"




        def load_state(self, db_name):
                pass
