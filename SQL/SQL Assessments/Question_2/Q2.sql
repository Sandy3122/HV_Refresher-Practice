/* Create a table name - "Football Venue". */

CREATE TABLE FootballVenue
(
	venue_id INT PRIMARY KEY NOT NULL,
    venue_name VARCHAR(50) NOT NULL,
    city_id INT NOT NULL,
    capacity INT NOT NULL
);