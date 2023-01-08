/* Day_8_2 */

CREATE DATABAsE Movie;

CREATE TABLE Movie
(
	Movie_id INT NOT NULL PRIMARY KEY UNIQUE,
    Movie_Title VARCHAR(50) NOT NULL,
    Ticket_price INT NOT NULL,
    Release_year YEAR NOT NULL,
    Language VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL
);

INSERT INTO Movie VALUES
(1, "Jalsa", "500", "2008", "Telugu", "India"),
(2, "Pokiri", "600", "2009", "Hindi", "Usa"),
(3, "Mirchi", "400", "2010", "Telugu", "Uk"),
(4, "Bahubali", "600", "2008", "Telugu", "Asia"),
(5, "Majili", "400", "2020", "Hindi", "Russia"),
(6, "Dhukudu", "800", "2016", "English", "Usa"),
(7, "Yemaya Chesaye", "400", "2008", "Telugu", "India"),
(8, "Raja Rani", "600", "2012", "Tamil", "Uk");


SELECT Movie_title, Ticket_price, Language FROM Movie;







-- Movie Name Released In 2010
SELECT Movie_title, Release_year FROM Movie WHERE Release_year = "2010";

-- Movie Name Released In 2010
SELECT Movie_title, Release_year FROM Movie WHERE Release_year < "2010";


/* CREATING REVIEWER TABLE */

CREATE TABLE Reviewer
(
	Reviewer_id INT NOT NULL PRIMARY KEY, 
	Reviewer_name VARCHAR(50) NOT NULL
);

INSERT INTO Reviewer VALUES
(101, "Seeram"),
(102, "Sandeep"),
(103, "Lakshman"),
(104, "Kumar"),
(105, "Jignesh"),
(106, "Lokesh"),
(107, "Mahesh"),
(108, "Nishanth");

SELECT Reviewer.Reviewer_name AS "Reviewer and Movie name" FROM Reviewer UNION (SELECT Movie.Movie_title FROM Movie);


CREATE TABLE Rating
(
	Movie_id INT PRIMARY KEY NOT NULL,
    Reviewer_id INT NOT NULL,
    Reviewer_star INT NOT NULL
);

INSERT INTO Rating VALUES
(2, 102, 8),
(4, 104, 9),
(6, 106, 8),
(8, 108, 7),
(10, 110, 6),
(12, 112, 5),
(14, 114, 8),
(16, 116, 9);


SELECT Reviewer.Reviewer_name, Rating.Reviewer_star From Reviewer, Rating WHERE Rating.Reviewer_id = Reviewer.Reviewer_id AND Rating.Reviewer_star >= 7;

/* Show Details Where Release Years Are 2008 AND 2020 */
SELECT * FROM Movie WHERE Release_year IN(2008,2020);

/* Show Details Where Ticket Prices Are 500 AND 600 */
SELECT * FROM Movie WHERE Ticket_price IN(500, 600);

/* INSERTING SOME MORE DATA INTO Movie TABLE */
INSERT INTO Movie VALUES
(9, "aabb", 900, "2006", "Kanada", "England"),
(10, "bbaa", 200, "2009", "Telugu", "Japan");


SELECT * FROM Movie WHERE Movie_title LIKE("%aa%") ORDER BY Release_year;
SELECT * FROM Movie WHERE Movie_title LIKE("%aa%") ORDER BY Release_year DESC;

/* Fetch number of movies released in same year */
SELECT Country, COUNT(Movie_title) AS "No.of Movies Released In Same Country" FROM Movie GROUP BY Country;

