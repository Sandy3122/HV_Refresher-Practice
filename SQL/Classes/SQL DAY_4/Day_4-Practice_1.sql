/*
Day - 2
Creating New(marks) Table
*/
CREATE TABLE marks(
	std_Id INT PRIMARY KEY NOT NULL,
    std_Name VARCHAR(50) NOT NULL,
    std_Marks INT NOT NULL
);

INSERT INTO marks 
VALUES(101, "Sandeep", 100),
(102, "Taruni", 100),
(103, "Hyndu", 90),
(104, "Geethika", 80),
(105, "Usha", 70),
(106, "Jignesh", 60);

SELECT * FROM marks;

/* Max Keyword (Showing Highest Marks)*/
SELECT MAX(std_marks) from marks;

/* MIN Keyword (Showing Lowest Marks) */
SELECT MAX(std_marks) as "Lowest Marks" from marks;

UPDATE marks SET std_marks=50 WHERE std_Id=104;

/* Showing Second Highest Marks */
SELECT MAX(std_marks) FROM marks WHERE std_marks < (SELECT MAX(std_marks) FROM marks);

DROP TABLE marks;



/*
DAY 4
*/

DESCRIBE marks;

INSERT INTO marks 
VALUES(107, "Sandy", 100),
(108, "Geethu", 80),
(109, "Hyndavi", 70);

/* GROUP BY */ 
SELECT COUNT(std_name),std_marks FROM marks GROUP BY std_marks;

/* GROUP BY, ORDER BY & ASC*/ 
SELECT COUNT(std_name), std_marks FROM marks GROUP BY std_marks ORDER BY std_marks DESC;

/* GROUP BY, ORDER BY & DESC*/ 
SELECT COUNT(std_name), std_marks FROM marks GROUP BY std_marks ORDER BY std_marks ASC;

/* GROUP BY & HAVIND */
/* HAVING ONLY Works With GROUP BY */
SELECT COUNT(std_name), std_marks FROM marks GROUP BY std_marks HAVING COUNT(std_name) > 1 ORDER BY std_marks;


/* LIKE CLAUSE */
SELECT *  FROM marks WHERE std_name LIKE "s%";

SELECT *  FROM marks WHERE std_name LIKE "[s]%";


SELECT *  FROM marks WHERE std_name LIKE "_a%";


/* NOT LIKE */
SELECT *  FROM marks WHERE std_name NOT LIKE "[S-p]%";


SELECT * FROM marks WHERE std_name LIKE "[h-i]%";


SELECT * FROM marks;