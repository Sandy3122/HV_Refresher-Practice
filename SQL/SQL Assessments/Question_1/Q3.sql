/* Insert 10 details in the “Employee Details” table  - 
1. Emp_id
2. Emp_name
3. Job_name
4. Manager_id\
5. Hire_date
6. Salary
7. Dep_id
 */ 
/* INSERTING DATA INTO EmployeeDetails Table */

INSERT INTO Employee.EmployeeDetails(Emp_id, Emp_name, Job_name, Manager_id, Hire_date, Salary, Dep_id)
VALUES(4001, "Sandeep", "Developer", 3001, "1999-10-22", 4500000, 1001),
(4002, "Taruni", "Doctor", 3002, "1998-12-31", 4500000, 1002),
(4003, "Geethu", "Architect", 3003, "1997-03-22", 2000000, 1003),
(4004, "Hyndu", "Inventor", 3004, "1996-08-14", 2400000, 1004),
(4005, "Honey", "Artist", 3005, "2001-09-29", 1800000, 1005),
(4006, "Jiggu", "Advocate", 3006, "2008-03-03", 1700000, 1006),
(4007, "Sona", "Enterpreneur", 3007, "1999-10-22", 2500000, 1007),
(4008, "Usha", "Artist", 3008, "1998-09-29", 1900000, 1008),
(4009, "Lakshman", "Enterpreneur", 3009, "2000-11-28", 2200000, 1009),
(4010, "Kumar", "Doctor", 3010, "2002-12-24", 2800000, 1010);

TRUNCATE TABLE employeedetails;