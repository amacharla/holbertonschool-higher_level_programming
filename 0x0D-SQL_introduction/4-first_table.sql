-- create a table called first_table in the current database
-- `IF NOT EXISTS` doesnt spit of error if table already exist

CREATE TABLE IF NOT EXISTS `first_table` (`id` INT, `name` VARCHAR(256));
