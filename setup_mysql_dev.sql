-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'lorddark0008'@'localhost' IDENTIFIED BY 'lookylooky7';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'lorddark0008'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'lorddark0008'@'localhost';
FLUSH PRIVILEGES;
