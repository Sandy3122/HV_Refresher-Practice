/* Creating The DataBase */
CREATE DATABASE Student;

/* Creating The Table */
CREATE TABLE Student.Details(
	RedId VARCHAR(20) NOT NULL PRIMARY KEY UNIQUE,
    StdName VARCHAR(20) NOT NULL,
    Marks INT NOT NULL
);

/* Inserting The Values */
INSERT INTO Details VALUES
("S01", "Sandeep", 99),
("S02", "Taruni", 80),
("S03", "Hyndu", 70),
("S04", "Geethika", 80),
("S05", "Sandy", 60),
("S06", "Sona", 90),
("S07", "Hyndavi", 60),
("S08", "Spandu", 40),
("S09", "Jignesh", 30),
("S10", "Geethu", 50);

/* To See The Table */
SELECT * FROM Student.Details;

/* Filtering The Students With Marks By Using WHERE CLAUSE */
SELECT * FROM Details WHERE Marks <> 50; -- Excluding Marks 50
SELECT * FROM Details WHERE Marks != 50; -- Excluding Marks 50
SELECT * FROM Details WHERE Marks <= 50; -- Including Marks 50


/* Filtering The Students With Marks By Using WHERE And BETWEEN CLAUSE */
SELECT * FROM Details WHERE Marks BETWEEN 70 AND 90;

/* By Using Order By Showing Details In Asscending Order */
SELECT * FROM Details WHERE Marks BETWEEN 70 AND 90 ORDER BY Marks asc;

/*
Like And Not Like
*/

/* Showing StdName Starting With Letter S */
SELECT * FROM Details WHERE StdName LIKE "S%";

/* Showing StdName ARE NOT Starting With Letter S */
SELECT * FROM Details WHERE StdName NOT LIKE "S%";

/* Fetching StdName Whose Name Second Letter Starting With Letter A */
SELECT * FROM Details WHERE StdName LIKE "_A%";

/* Fetching StdName Whose Name Third Letter Starting With Letter A */
SELECT * FROM Details WHERE StdName LIKE "__A%";

/* Showing StdName Starting With Letter i */
SELECT * FROM Details WHERE StdName LIKE "%i";

/* IN operator allows you to specify multiple values in a WHERE clause */
/* With INT */
SELECT * FROM Details WHERE Marks IN (50,80);

/* With String */
SELECT * FROM Details WHERE StdName IN ( "Sandeep", "Sona" );

/* Using WHERE, AND Clauses (Two Statements Should Satisfy) */
SELECT * FROM Details WHERE StdName = "Sandeep" AND Marks > 50;

/* Using WHERE, OR Clauses (Any One Statements That Can Be Can True) */
SELECT * FROM Details WHERE StdName = "Sandeep" OR Marks > 70;

/* NOT Clause */
SELECT * FROM Details WHERE NOT StdName = "Sandeep";

/* AND & OR Clauses */
SELECT * FROM Details WHERE Marks = 70 And (StdName = "Sandy" Or StdName = "Hyndu");

SELECT * FROM Details WHERE StdName = "Sandeep" OR Marks = 80 And Marks = 50; 

SELECT * FROM Details WHERE StdName = "Sandeep" OR Marks = 80 OR Marks = 50; 

/* AND & NOT */
SELECT * FROM Details WHERE NOT StdName = "Sandeep" AND NOT StdName = "Sandy";

/* ORDER BY */
SELECT * FROM Details order by Marks;	-- BY Default It Is in Asscending Order
SELECT * FROM Details ORDER BY Marks DESC;

SELECT * FROM Details ORDER BY StdName DESC;

/* First Marks are arranged in descending and then if marks are same then it is arranged with name in asscending order */
SELECT * FROM Details ORDER BY Marks DESC, StdName ASC;

SELECT * FROM Details ORDER BY Marks, StdName DESC;

SELECT * FROM Details ORDER BY StdName DESC, Marks DESC;

/* Everything Will Be In Asscending Ordered */
SELECT * FROM Details ORDER BY Marks, StdName;


/* Update The Entries */
UPDATE Details SET StdName = "sandeep" WHERE RedId = "S09";
UPDATE Details SET Marks = 30 WHERE RedId = "S09";

/* Alter Clause */
ALTER TABLE Details RENAME COLUMN StdName TO SName;
ALTER TABLE Details RENAME COLUMN RedId TO RegId;


ALTER TABLE Details MODIFY COLUMN Marks VARCHAR(20) NOT NULL;

/* To Show The DataTypes Of The Columns */
DESCRIBE Details;

DELETE FROM Details WHERE StdName = "Sandeep"; -- Not Working

/* LIMIT KEYWORD */
 SELECT * FROM Details LIMIT 3;
 
 SELECT * FROM Details WHERE Marks > 50 LIMIT 4;


/* MIN KEYWORD */
SELECT MIN(Marks) as LowestMarks FROM Details;
/* Multiple Query  */
SELECT * FROM Details WHERE Marks = (SELECT MIN(Marks) from Details);



/* MAX KEYWORD */
SELECT MAX(Marks) as HighestMarks FROM Details;

/* Multiple Query  */
SELECT * FROM Details WHERE Marks = (SELECT MAX(Marks) from Details);

/* Getting Top 3 Highest Marks */
SELECT * FROM Details ORDER BY Marks DESC LIMIT 3;


/* COUNT KEYWORD */
SELECT COUNT(Marks) FROM Details;

/* SUM KEYWORD */
SELECT SUM(Marks) FROM Details;

/* AVG KEYWORD */
SELECT AVG(Marks) FROM Details;







/* To Delete Entire Table */
DROP TABLE Details;