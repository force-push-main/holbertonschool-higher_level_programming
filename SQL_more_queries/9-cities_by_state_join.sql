-- use join to find cities by state id
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN cities ON states.id = cities.state_id
WHERE states.name = 'California'
ORDER BY cities.id ASC
