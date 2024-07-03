-- Prepares a MySQL server for the project.
-- Create a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a localhost user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant the user all privileges on a specific db
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- Grant the user SELECT privileges only on another db
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
