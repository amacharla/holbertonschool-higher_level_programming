--script that lists all records of the table second_table with cretria
-- `HAVING` ! dont show records without `name` attribute

SELECT `score`, `name` FROM `second_table` HAVING !`name` ORDER BY `score` DESC;
