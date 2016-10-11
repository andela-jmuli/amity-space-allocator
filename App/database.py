import os

from sqlalchemy import create_engine
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

        def save_state(self, db_name):
                if os.path.exists(db_name):
                        os.remove(db_name)
                try:
                        save_amity_session = self.connect_db(db_name)
                        self.commit_people(save_amity_session)
                        self.commit_rooms(save_amity_session)
                except Exception:
                        message = "Error saving data to database"

                save_amity_session.commit()
                save_amity_session.close()

        def load_state(self, db_name):
                pass
