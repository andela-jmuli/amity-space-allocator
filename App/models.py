import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, Boolean

# engine = create_engine('sqlite:///amity.db', echo = False)

Base = declarative_base()



class AmityRoom(Base):
        __tablename__ = 'room'

        id = Column(Integer, primary_key=True)
        room_name = Column(String(20))
        room_type = Column(String(20))
        capacity = Column(Integer)


class AmityPerson(Base):
        __tablename__ = 'person'

        id = Column(Integer, primary_key=True)
        person_id = Column(Integer)
        username = Column(String(50))
        job_type = Column(String(20))
        is_accomodated = Column(Boolean, default=False)
        allocated_office = Column(String(20))
        allocated_livingspace = Column(String(20))


def create_db(db_name):
        engine = create_engine('sqlite:///'+db_name, echo=True)
        global Base
        Base.metadata.create_all(engine)


