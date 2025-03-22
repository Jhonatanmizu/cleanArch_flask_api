CREATE DATABASE IF NOT EXISTS `clean_architecture_db`;

CREATE TABLE IF NOT EXISTS `clean_architecture_db`.`users` (
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birthdate DATETIME NOT NULL,
    PRIMARY KEY (id)
);