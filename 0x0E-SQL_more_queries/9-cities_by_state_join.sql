-- a script that lists all cities contained in the database htbn_0d_usa
SELECT cities.id, cities.name, states.name
FROM CITIES
INNER JOIN ON cities.states_id = states.id;