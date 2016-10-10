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

        def commit_people(self, amity_session):
                # loop through people dictionary and get person details
                for key, value in Person.total_people.items():
                        person_id = key
                        username = value["username"]
                for job in Person.fellows:
                        if username in Person.fellows:
                                job_type = 'fellow'
                        else:
                                job_type = 'staff'
                if username in Person.unallocated_people:
                        is_accomodated = 'False'
                        allocated_livingspace = None
                        for room in Room.total_rooms:
                                if room in Room.offices:
                                        for occupant in Room.total_rooms[room]:
                                                if person_id == occupant:
                                                        allocated_office = room
                else:
                        is_accomodated = 'True'
                        for room in Room.total_rooms:
                                if room in Room.offices:
                                        for occupant in Room.total_rooms[room]:
                                                if person_id == occupant:
                                                        allocated_office = room
                                elif room in Room.livingspaces:
                                        for occupant in Room.total_rooms[room]:
                                                if person_id == occupant:
                                                        allocated_livingspace = room

                person_info = (person_id=person_id, username=username, is_accomodated=is_accomodated, office_allocated=allocated_office, livingspace_allocated=allocated_livingspace, job_type=job_type)
                try:
                        amity_session.add(person_info)
                except Exception:
                        return "person data save not successful"



        def save_state(self, db_name='amity.db'):
                if os.path.exists(db_name):
                        os.remove(db_name)
                try:
                        save_amity_session = self.connect_db(amity.db)
                        self.commit_people(save_amity_session)
                        self.commit_rooms(save_amity_session)
                except Exception:
                        message = "Error saving data to database"

                save_amity_session.commit()
                save_amity_session.close()
