from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine('sqlite:///banco_dados.db')

Base = declarative_base()

Base.metadata.create_all(engine)