-- Creates a second_table
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
