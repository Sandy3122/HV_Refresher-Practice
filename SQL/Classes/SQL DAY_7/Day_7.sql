/* Day_7 */

create table customer1(
Id int not null primary key,
name varchar(30) not null,
age int not null,
address varchar(50) not null,
salary int not null
);
insert into customer1(Id,name,age,address,salary)
values(5001,"devi vara prasad",22,"rajahmundry",500000),(5002,"akhil radha krishna",21,"kakinada",45000),(5003,"nivesh",23,"hyderabad",990000);


create table cust_orders(
order_id int not null primary key,
date date not null,
customer_id int not null,
amount int not null
);
insert into cust_orders(order_id,date,customer_Id,amount)
values(601,"2022-12-25",5001,5000),(602,"2022-05-21",5003,6020),(603,"2022-11-16",5002,7500);



select Id,name,amount,date from customer1 left join cust_orders on customer1.Id = cust_orders.customer_Id
union all 
select Id,name,amount,date from customer1 right join cust_orders on customer1.Id = cust_orders.customer_Id;



