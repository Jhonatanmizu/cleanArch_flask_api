create database if not  exists `clean_architecture_db`;


create table if not exists `clean_architecture_db`.`users`(
    id int not null auto_increment,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    primary key(id)
)