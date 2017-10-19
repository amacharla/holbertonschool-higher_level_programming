-- Create database and table with 2 attributes
-- add Foreign key for state_id <- state (id)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
	(id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id), 
       	name VARCHAR(256) NOT NULL);
