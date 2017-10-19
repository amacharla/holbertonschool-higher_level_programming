-- Create table with 2 attributes, both not null.

CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT '1', name VARCHAR(256) NOT NULL);
