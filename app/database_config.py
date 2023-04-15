import sqlite3
import sqlalchemy

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class Tasks(Base):
    __tablename__= "tasks"
    id = Column(Integer, primary_key=True)
    name= Column(String)

engine = create_engine('sqlite:///tasks_db.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)