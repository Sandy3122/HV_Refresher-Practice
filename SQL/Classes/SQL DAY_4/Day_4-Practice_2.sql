/*
Day_4
*/

/* Creating Coustomer Database*/
CREATE DATABASE Customer;

/* Creating Table coustomer */
CREATE TABLE Customer(
	cust_Id INT  PRIMARY KEY NOT NULL,
    cust_name VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    grade INT,
    salesman_Id INT NOT NULL
);

/* Inserting Values Int Coustomer Table */
INSERT INTO Customer 
VALUES(101, "Seeram", "Bangalore", 100, 201),
(102, "Sandeep", "TataNagar", 90, 202),
(103, "Lakshman", "Vizag" , NULL, 203),
(104, "Kumar", "kakinada", 80, 204),
(105, "Taruni", "TataNagar", 80, 205),
(106, "Sona", "Vizag", NULL, 206);

/* COUNT CLAUSE */
SELECT COUNT(grade) FROM Customer;		-- Showing Only Graded Values, Except Null Values

/* Max And GROUP BY */
SELECT city, max(grade) FROM Customer GROUP BY city;	-- Showing only unique city from the table with max(grade)

/* Multiplying The Grade With 10 */
SELECT cust_Id, cust_name, grade*10 FROM Customer;

/* Grades Greater than 80 */
SELECT * FROM customer WHERE grade > 80;

/* Grades Greater than 80 And ORDER BY cust_name*/
SELECT * FROM customer WHERE grade > 70 ORDER BY cust_name;

/* GROUP BY & HAVIND */
/* HAVING ONLY Works With GROUP BY */
SELECT * FROM customer GROUP BY salesman_Id HAVING salesman_Id > 202;		-- worng

/* OR Clause */
SELECT * FROM customer WHERE city="Bangalore" or grade=80;

/* Second Largest Grade */
SELECT cust_name as "NAME", max(grade) FROM customer;

/* Second Highest Grade */
SELECT MAX(grade) as "Second Highest" FROM Customer WHERE grade < (SELECT MAX(grade) FROM Customer);

/* Third Highest Grade */
-- SELECT MAX(grade) as "Third Highest" FROM Customer WHERE grade < (SELECT MAX(grade) FROM Customer) WHERE grade < (SELECT MAX(grade) FROM Customer);







TRUNCATE TABLE Customer;
DROP TABLE Customer;