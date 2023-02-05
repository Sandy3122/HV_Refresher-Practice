create database movie_db;


create table actor(
actor_id int not null primary key,
actor_firstname varchar(30) not null,
actor_lastname varchar(30) not null,
actor_gender varchar(15) not null
);


insert into actor(actor_id,actor_firstname,actor_lastname,actor_gender)
values(101,"Allu","Arjun","male"),
(102,"ram","charan","male"),
(103,"Ntr","r","male"),
(104,"samantha","akkineni","female"),
(105,"sunny","leone","female");


create table movie_cast(
actor_id int not null,
movie_id int not null primary key,
role varchar(25) not null 
);



insert into movie_cast(actor_id,movie_id,role)
values(101,201,"hero"),
(102,202,"child artist"),
(103,203,"comedian"),
(104,204,"heroine"),
(105,205,"singer");


create table movie(
movie_id int not null primary key,
movie_name varchar(30) not null,
movie_year int not null,
movie_language varchar(25) not null,
movie_realeasedate date not null,
movie_releasecountry varchar(20) not null 
);

insert into movie(movie_id,movie_name,movie_year,movie_language,movie_realeasedate,movie_releasecountry)
values(201,"pushpa",2021,"telugu","2021-11-10","india"),
(202,"avengers",2022,"english","2022-10-25","USA"),
(203,"RRR",2022,"telugu","2022-05-12","india"),
(204,"kgf",2021,"kannada","2021-04-06","india"),
(205,"ginna",2022,"telugu","2022-11-25","india");


create table director(
director_id int not null primary key,
director_firstName varchar(30) not null,
director_lastName varchar(30) not null
);


insert into director(director_id,director_firstName,director_lastName)
values(4001,"sai","nikhil"),
(4002,"akhil","radha"),
(4003,"devi","varaPrasad"),
(4004,"veerendra","matsa"),
(4005,"sandeep","seeram");


create table movie_direction(
director_id int not null primary key,
movie_id int not null
);


insert into movie_direction(director_id,movie_id)
values(4001,201),
(4002,202),
(4003,203),
(4004,204),
(4005,205);




select * from actor where actor_id 
IN(select actor_id from movie_cast where movie_id 
IN(select movie_id from movie where movie_name="RRR"));

select * from director 
where director_id in (select director_id from movie_direction 
where movie_id in(select movie_id from movie_cast 
where role=any(select role from movie_cast 
where movie_id in (select movie_id from movie 
where movie_name="RRR"))));

-- write a SQL query to find those movies that have been released in countries other than the USA
Select movie_name from movie where movie_releasecountry <>'USA';

select * from movie where movie_releasecountry<>"USA";

select movie_name as "Movie Title",
movie_realeasedate as "Realease Date",
movie_releasecountry as "Releasing Country"  
FROM movie WHERE movie_releasecountry <> "USA";

