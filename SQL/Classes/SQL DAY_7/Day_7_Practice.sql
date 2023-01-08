/* Practice */
/* Day_7 */

SELECT * FROM Customer WHERE Grade > 90;

SELECT * FROM Customer WHERE Grade >= 90;

SELECT * FROM Customer WHERE Grade BETWEEN 90 AND 100;



/* Inserting Data Into Customer Table */

INSERT INTO Customer(Cust_Id, Cust_Name, City, Grade, Salesman_Id)
VALUES
(107, "Seeram", "Vizag", 150, 307),
(108, "Lokesh", "Vijayawada", 120, 308),
(109, "Raju", "Delhi", 140, 309),
(110, "Krishna", "Delhi", 100, 310),
(111, "Ram", "Delhi", 130, 311),
(112, "Sita", "Singapore", 80, 312),
(113, "Jiggu", "Delhi", 900, 313),
(114, "Mahesh", "Kakinada", 160, 314);

TRUNCATE TABLE Customer;





/*
Write a SQL query where the city is "Kakinada" and the grade is greater than or equal to 100
from the customer table
*/
SELECT Cust_Id, Cust_name FROM Customer WHERE City = "Kakinada" AND Grade >= 100;


/*
write a SQL query to find customers who are either from the "Delhi" location or who do not have a grade greater than 100

*/
SELECT Cust_Id, Cust_name, Grade as "Grades " FROM Customer WHERE City = "Kakinada" OR Grade >= 100;


/*
write a SQL query to find customers who are either from the "Kakinada" location or who do not have a grade greater than 100

*/
SELECT * FROM Customer WHERE Grade > 100;

SELECT * FROM Customer WHERE NOT Grade>90;

SELECT * FROM Customer WHERE NOT Grade>=100;

SELECT * FROM Customer WHERE City = "Kakinada" OR NOT Grade > 100;

SELECT * FROM Customer WHERE City = "Vizag" AND NOT Grade > 100;


/* 
write a SQL query to identify customers who do not belong to the "Delhi"
location or have a grade value that exceeds 100.
*/
SELECT * FROM Customer WHERE NOT City = "Delhi" AND Grade > 100;

SELECT * FROM Customer WHERE City != "Delhi " AND Grade>100;

SELECT * FROM Customer WHERE City <> "Delhi " or Grade>100;
