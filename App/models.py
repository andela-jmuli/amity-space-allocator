import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, Boolean


engine = create_engine('sqlite:///amity.db', echo = False)

Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


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


class AmityAllocations(Base):
        __tablename__ = 'allocations'

        id = Column(Integer, primary_key=True)
        room_name = Column(String(20))
        occupants = Column(String(20))




Base.metadata.create_all(engine)
