import db
from sqlalchemy.orm import sessionmaker

class Database():
    def __init__(self):
        pass

    def criar_session(self):
        Session = sessionmaker(bind=db.engine)
        return Session()

