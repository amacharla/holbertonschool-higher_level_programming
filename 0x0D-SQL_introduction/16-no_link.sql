--script that lists all records of the table second_table with cretria
-- `HAVING` ! says everything that has `name`

SELECT `score`, `name` FROM `second_table` HAVING !`name` ORDER BY `score` DESC;
