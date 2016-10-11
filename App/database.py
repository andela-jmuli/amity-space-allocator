import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

class AmityDatabase(object):

        engine = create_engine('sqlite:///amity_class.db')
        Base.metadata.bind = engine
        AmitySession = sessionmaker(bind=engine)
        session = AmitySession()

        def __init__(self):
                self.db = None

        def save_state(self, db_name):
                if os.path.exists(db_name):
                        os.remove(db_name)
                try:
                        save_amity_session = session
                        Person.commit_people()
                        Room.commit_rooms()
                except Exception:
                        message = "Error saving data to database"

                save_amity_session.commit()
                save_amity_session.close()

        def load_state(self, db_name):
                pass
