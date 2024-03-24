#!/usr/bin/python3
"""
A python file that contains the class definition of state
and an instance Base = declarative()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base()



class State(Base):
    """inherits from the Base"""

    __tablename__ = 'states'

    id = Column(Integer, Primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=True)


