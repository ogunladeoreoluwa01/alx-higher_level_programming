-- Creates a table with an id field with a default value of 1
CREATE TABLE IF NOT EXISTS unique_id
(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
