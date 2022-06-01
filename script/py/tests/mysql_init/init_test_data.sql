use db_test;

create table if not exists t_trans_csv_mysql(
    id int primary key auto_increment,
    name varchar(50),
    field1 datetime,
    field2 int,
    field3 varchar(50),
    unique key idx1 (name)
);
