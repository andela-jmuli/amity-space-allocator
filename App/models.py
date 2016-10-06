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


class Room(Base):
        __tablename__ = 'room'

        id = Column(Integer, primary_key=True)
        room_name = Column(String(20))
        room_type = Column(String(20))
        capacity = Column(Integer)
        occupant_no = Column(Integer)


class Person(Base):
        __tablename__ = 'person'

        id = Column(Integer, primary_key=True)
        first_name = Column(String(50))
        last_name = Column(String(50))
        accomodated = Column(Boolean, default=False)
        office_allocated = Column(String(20))
        livingspace_allocated = Column(String(20))




Base.metadata.create_all(engine)