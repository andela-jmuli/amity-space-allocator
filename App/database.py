import os

from room import Room
from person import Person
from sqlalchemy import create_engine, Metadata
from sqlalchemy.orm import sessionmaker



class AmityDatabase(object):


        def __init__(self):
                self.db = None


        def connect_db(self, db_name):
                self.db.create_engine("sqlite:///"+db_name)
                session = sessionmaker()
                session.configure(bind=self.db)
                self.db.echo = False
                Base.metadata.create_all(self.db)

                amity_session = session()
                return amity_session

        def commit_rooms(self, amity_session):
                """
        Loads rooms from the total_rooms dictionary and commits to database
                """
                for room in Room.total_rooms.keys():
                        room_name = room
                for rm in Room.offices:
                        if rm in Room.offices:
                                room_type = 'office'
                                room_capacity = 6
                        elif rm in Room.livingspaces:
                                room_type = 'livingspace'
                                room_capacity = 4
                room_info = (room_name=room_name, room_type=room_type, capacity=room_capacity)

                try:
                        amity_session.add(room_info)
                except Exception:
                        return "room data save Failed!"

