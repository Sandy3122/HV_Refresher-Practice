/* INSERTING DATA INTO TABLES */

/* INSERTING DATA INTO consumer Table */
INSERT INTO consumer
(consumer_id, consumer_name, consumer_city, sales_manager_id)
VALUES(101, "SEERAM", "Hyderabd", "201"),
(102, "Sandeep", "Kolkata", "203"),
(103, "Lakshman", "Mumbai", "204"),
(104, "Kumar", "Pune", "204"),
(105, "Sandy", "Hyderabd", "205"),
(106, "Jignesh", "Vizag", "206"),
(107, "Lokesh", "Kolkata", "207"),
(108, "Mahesh", "Pune", "208");


/* INSERTING DATA INTO orders Table */
INSERT INTO orders
(order_no, purchase_amount, order_date, consumer_id, sales_manager_id)
VALUES(1001, 200, "2020-10-12", 101, 301),
(1002, 400, "2020-08-13", 102, 302),
(1003, 900, "2021-06-14", 103, 303),
(1004, 300, "2022-04-15", 104, 304),
(1005, 500, "2021-02-16", 1005, 305),
(1006, 600, "2019-04-17", 106, 306),
(1007, 100, "2022-08-18", 107, 307),
(1008, 700, "2019-06-19", 108, 308),
(1009, 800, "2020-10-20", 109, 309),
(1010, 1000, "2019-04-22", 110, 310);


/* INSERTING DATA INTO sales_manager Table */
INSERT INTO sales_manager
(sales_manager_id, manager_name, manager_city)
VALUES(301, "Seeram", "Bangalore"),
(302, "Sandeep", "Pune"),
(303, "Lakshman", "Kolkata"),
(304, "Kumar", "Hyderabad"),
(305, "Sona", "Pune"),
(306, "Taruni", "Bangalore"),
(307, "Geethika", "Hyderabad"),
(308, "Jignesh", "Vizag"),
(309, "Lokesh", "Kolkata"),
(310, "Mahesh", "Vizag");