-- Creates a second_table
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.SCHEMATA WHERE schema_name = 'hbtn_0c_0') THEN
  CREATE DATABASE hbtn_0c_0;
END IF;

USE hbtn_0c_0;

IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE table_name = 'second_table') THEN
  CREATE TABLE second_table(
    id INT,
    name VARCHAR(256),
    score INT
  );
END IF;

INSERT INTO second_table(id, name, score)
VALUES(1, "john", 10),
  (2, "Alex", 3),
  (3, "Bob", 14),
  (4, "George", 8);
