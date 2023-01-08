/* Day_6 */


CREATE DATABASE OnlineShopping;

CREATE TABLE Salesman(
	Salesman_Id INT PRIMARY KEY NOT NULL,
    Name VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
	Commission FLOAT NOT NULL
);

INSERT INTO Salesman(Salesman_Id, Name, City, Commission)
VALUES(301, "Taruni", "Kakinada", 0.22),
(302, "Lakshman", "Hyderabad", 0.14),
(303, "Hyndu", "Pune", 0.16),
(304, "Govind", "Kakinada", 0.12),
(305, "Raju", "Vizag", 0.18),
(306, "Kumar", "Rajahmundary", 0.14);

DROP TABLE Salesman;



CREATE TABLE Customer(
	Cust_Id INT PRIMARY KEY NOT NULL,
    Cust_Name VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    Grade INT NOT NULL,
    Salesman_Id INT NOT NULL
);

INSERT INTO Customer(Cust_Id, Cust_Name, City, Grade, Salesman_Id)
VALUES(101, "Sandeep", "Kakinada", 100, 301),
(102, "Sona", "Delhi", 100, 302),
(103, "Taruni", "Jharkhad", 90, 303),
(104, "Geethu", "Kakinada", 60, 304),
(105, "Madhuri", "Kakinada", 110, 305),
(106, "Lakshmi", "Samalkot", 80, 306);

TRUNCATE TABLE Customer;

/*
To find the salesperson and customer who reside in the same city
*/
SELECT Salesman.Name, Customer.Cust_Name, Customer.City FROM Salesman, Customer WHERE Salesman.City =Customer.City;


/* Creating Orders Table */
CREATE TABLE Orders(
	Order_num INT PRIMARY KEY NOT NULL,
    Purchase_amount INT NOT NULL,
    Order_date DATE NOT NULL,
    Customer_id INT NOT NULL,
    Salesman_id INT NULL
);

INSERT INTO Orders()
VALUES(401, 500, "2022-08-22", 101, 301),
(402, 800, "2022-09-24", 102, 302),
(403, 600, "2022-10-26", 103, 303),
(404, 400, "2022-11-28", 104, 304);



/*
To find those orders where the order amount exists between 400 and 600
*/
SELECT a.Order_num, a.Purchase_amount, b.Cust_Name, b.City FROM Orders a, Customer b WHERE a.Customer_id = b.Cust_Id AND a.Purchase_amount BETWEEN 400 AND 600;

/*
Select Customer Name, City, Commission From Customer Table And Salesman Table
Where Customer.Salesman_Id And Salesman.Salesman_Id Are Same. 
*/
SELECT a.Cust_Name AS "Customer Name", a.City, b.Name AS "Salesman", b.Commission FROM Customer a INNER JOIN Salesman b ON a.Salesman_Id = b.Salesman_Id;