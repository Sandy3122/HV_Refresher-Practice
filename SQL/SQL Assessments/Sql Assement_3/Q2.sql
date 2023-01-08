/* 2. Change the consumer_id in the orders table where order_no is equal to "1005" */


UPDATE orders SET consumer_id = 105 WHERE order_no = 1005;

SELECT * FROM orders;