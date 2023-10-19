-- listin cities called california
SELECT name FROM hbtn_0d_usa.cities
WHERE states_id=(SELECT id FROM hbtn_0d_usa.states WHERE name = 'California')
ORDER BY hbtn_0d_usa.cities(id) ASC;