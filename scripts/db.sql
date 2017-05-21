CREATE USER 'ams'@'%' IDENTIFIED BY 'ams_pass';

GRANT SELECT ON `mysql`.`user` TO 'ams'@'%';

GRANT SELECT, INSERT, UPDATE, REFERENCES, DELETE, CREATE, DROP, ALTER, INDEX, TRIGGER, CREATE VIEW, SHOW VIEW, EXECUTE, ALTER ROUTINE, CREATE ROUTINE, CREATE TEMPORARY TABLES, LOCK TABLES, EVENT ON `ams`.* TO 'ams'@'%';

GRANT GRANT OPTION ON `ams`.* TO 'ams'@'%';

