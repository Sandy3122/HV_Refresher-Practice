/* Day_8 Practice */


SELECT * FROM onlineshopping.customer;
INSERT INTO customer
VALUES(115, "Jignesh", "Vizag", 190, 315),
(116, "Lokesh", "Hyderabad", 160, 316);

/* IN Keyword */
SELECT * FROM customer WHERE City IN("Delhi", "Vizag", "Kakinada");

SELECT * FROM Customer WHERE City IN(SELECT City FROM salesman);

/* NOT IN Keyword */
SELECT * FROM customer WHERE City NOT IN("Delhi", "Vizag", "Kakinada");

SELECT * FROM customer WHERE City = "Delhi";


/* EXISTS Keyword */
SELECT Cust_Name FROM customer WHERE EXISTS
(SELECT Name FROM salesman WHERE salesman.Salesman_Id = customer.Salesman_Id);

SELECT * FROM customer WHERE EXISTS
(SELECT Name FROM salesman WHERE salesman.Salesman_Id = customer.Salesman_Id OR Grade > 200);

SELECT * FROM customer WHERE EXISTS
(SELECT Name FROM salesman WHERE Salesman.Salesman_Id = customer.Salesman_Id AND Grade > 200);


/* ANY KEYWORD */
SELECT Name FROM Salesman WHERE Salesman_Id = ANY(SELECT Salesman_Id FROM customer WHERE Grade = 100);






