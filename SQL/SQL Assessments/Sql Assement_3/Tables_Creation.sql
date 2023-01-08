/* Assessment */

/* CREATING Order_Details DATABASE */
CREATE DATABASE Order_Details;

CREATE TABLE consumer
(
	consumer_id INT PRIMARY KEY NOT NULL UNIQUE,
    consumer_name VARCHAR(50) NOT NULL,
    consumer_city VARCHAR(50) NOT NULL,
    sales_manager_id INT NOT NULL  
);


CREATE TABLE orders
(
	order_no INT PRIMARY KEY NOT NULL UNIQUE,
    purchase_amount INT NOT NULL,
    order_date DATE NOT NULL,		-- "YYYY-MM-DD"
    consumer_id INT NOT NULL,
    sales_manager_id INT NOT NULL  
);

CREATE TABLE sales_manager
(
    sales_manager_id INT PRIMARY KEY NOT NULL UNIQUE,
    manager_name VARCHAR(50) NOT NULL,
    manager_city VARCHAR(50) NOT NULL
);