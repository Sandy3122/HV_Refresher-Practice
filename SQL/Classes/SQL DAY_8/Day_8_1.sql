/* DAY_8_1 */

/*
UNIQUE Keyword
The Values Should Be Only Unique Without Duplicates
*/
CREATE TABLE Sample
(
	Id INT PRIMARY KEY NOT NULL UNIQUE,
    Text VARCHAR(50) NOT NULL
);

INSERT INTO Sample(Id, Text)
VALUES(1, "Text1"),
(2, "Text2"),
(3, "Text3"),
(4, "Text4");

SELECT * FROM Sample;



/*
AUTO_INCREMENT Keyword
The Values Should Be Only Unique Without Duplicates
*/
CREATE TABLE Test
(
	Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Data VARCHAR(50) NOT NULL
);

INSERT INTO Test(Data)
VALUES("Data1"),
("Data2"),("Data3"),("Data4");

ALTER TABLE Test AUTO_INCREMENT=100;

UPDATE Test SET Id = Id + 200;
/* Updating By Using range Function */
UPDATE Test SET Id = Id + 200 WHERE Id BETWEEN 1 AND 4;

Truncate Table Test;
SELECT * FROM Test;