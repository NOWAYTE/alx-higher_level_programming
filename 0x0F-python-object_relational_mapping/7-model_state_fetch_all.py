#!/usr/bin/python3
"""Defines a script that list all states objects from the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(username, password, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).all()

    for i in states:
        print("{}: {}".forma(state.id, state.name))

    session.close()



