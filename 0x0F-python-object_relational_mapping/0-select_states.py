#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
Usage: ./1-filter_states.py <mysql username>
                           <mysql password>
                           <database name>"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define base class for declarative class definitions
Base = declarative_base()

# Define State class which represents the states table
if __name__ == '__main__':
    class State(Base):
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True)
        name = Column(String(256))
        if __name__ == "__main__":
            if len(sys.argv) != 4:
                print("Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>")
                sys.exit(1)
                # Connect to the MySQL database using SQLAlchemy
                username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
                engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database)
                Base.metadata.create_all(engine)
                Session = sessionmaker(bind=engine)
                session = Session()
                # Query the states starting with "N"
                states_starting_with_n = session.query(State).filter(State.name.like('N%')).order_by(State.id).all()
                # Print the results
                for state in states_starting_with_n:
                print(state.name)

