-- create the history table
-- stores the function call 
create table history(
    id integer primary key autoincrement,
    func_name varchar(255) not null,
    nr_params integer default 0,
    params_name varchar(255),
    params_value varchar(255),
    date varchar(255) not null
);

-- create the user table
-- used to store infos for the authentification
create table user(
    name varchar(255) not null,
    email varchar(255) primary key,
    password varchar(255) not null, 
    date varchar(255) not null
)