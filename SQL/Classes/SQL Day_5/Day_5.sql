/* DDay_5 */

CREATE DATABASE Delivery;

/* CREATING Orders TABLE */
CREATE TABLE Orders(
	Order_id INT PRIMARY KEY NOT NULL,
    Cust_id INT NOT NULL,
    Order_Date DATE NOT NULL,
    Emp_id INT NOT NULL
);

/* INSERTING DATA INTO TABLE */
INSERT INTO Orders (Order_id, Cust_id, Order_Date, Emp_id)
VALUES(101, 201, '1999-10-22', 1),
(102, 202, '1998-9-23', 2),
(103, 203, '1997-8-24', 3),
(104, 204, '1996-7-25', 4),
(105, 205, '1995-6-26', 5),
(106, 206, '1994-5-27', 6);


/* CREATING Customers TABLE */
CREATE TABLE Customers(
	Cust_id INT PRIMARY KEY NOT NULL,
    Cust_name VARCHAR(20) NOT NULL,
    Contact_name VARCHAR(40) NOT NULL,
    Country VARCHAR(50) NOT NULL
);

/* INSERTING DATA INTO TABLE */
INSERT INTO Customers(Cust_id, Cust_name, Contact_name, Country)
VALUES(201, "S.Sandeep", "Sandeep", "India"),
(202, "S.Sona", "Sona", "India"),
(203, "B.Hyndu", "Hyndu", "America"),
(204, "G.Geethika", "Geethika", "Australia");


/*
JOINS CONCEPT

## INNER JOIN & JOIN ##

INNER JOIN AND JOIN WILL GIVES THE SAME OUTPUT

Shows Common Data In These Two Tables 
*/

SELECT Orders.Order_id, Customers.Cust_id, Orders.Order_Date FROM Orders INNER JOIN Customers ON Orders.Cust_id = Customers.Cust_id; 

SELECT Orders.Order_id, Customers.Cust_id, Orders.Order_Date FROM Orders JOIN Customers ON Orders.Cust_id = Customers.Cust_id;		-- Same Output As INNER JOIN


/* LEFT JOIN */

SELECT Customers.Cust_name, Orders.Order_id FROM Customers LEFT JOIN Orders on Customers.Cust_id = Orders.Cust_id ORDER by Customers.Cust_name;

SELECT Customers.Cust_name, Orders.Order_id FROM Customers LEFT JOIN Orders on Customers.Cust_id = Orders.Cust_id;

/* Adding Column To Table */
ALTER TABLE Orders ADD Empl_id INT NOT NULL;

UPDATE Orders SET Emp_id = 1 WHERE Order_id = 101;

/* CREATING Employee TABLE */
CREATE TABLE Employee(
	Emp_id INT PRIMARY KEY NOT NULL,
    First_name VARCHAR(50) NOT NULL,
    Last_name VARCHAR(50) NOT NULL,
    DOB DATE NOT NULL
);

INSERT INTO Employee(Emp_id, First_name, Last_name, DOB)
VALUES(1, "Sandeep", "Seeram", "1999-10-22"),
(2, "Sona", "Mata", "1991-12-31"),
(3, "Hyndu", "Budapaneti", "1999-11-20"),
(4, "Geethika", "Seeram", "2000-3-22");

/* RIGHT JOIN */

SELECT Orders.Order_id, Employee.First_name, Employee.Last_name FROM Orders RIGHT JOIN Employee ON Orders.Emp_id = Employee.Emp_id;

/* FULL JOIN */
SELECT Customer.Cust_name, Orders.Order_id FROM Customers FULL JOIN Orders ON Customers.Cust_id = Orders.Cust_id;



SELECT * FROM Orders;






DROP TABLE Orders;