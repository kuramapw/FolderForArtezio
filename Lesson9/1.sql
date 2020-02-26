create table if not exists persons (
    name varchar(30) not null,
    surname varchar(30) not null,
    rang varchar(30) not null,
    cash float not null
);
insert into persons(name, surname, rang, cash) values ('Naruto','Uzumaki','Hokage',99999999);
insert into persons(name, surname, rang, cash) values ('Shikamaru','Nara','The Right Hand Hokage',999999);
insert into persons(name, surname, rang, cash) values ('Sasuke','Uchiha','Shadow Hokage',0);
insert into persons(name, surname, rang, cash) values ('KakaShi','Hatake','ExHokage',99999999);
