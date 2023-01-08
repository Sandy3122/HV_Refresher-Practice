/*
4. Return consumer_name, city, order_no, order_date, order_amount in ascending order
according to the order date to determine whether any of the existing consumers have placed an order or not
*/

SELECT c.consumer_name, s.manager_city, o.order_no, o.order_date, o.purchase_amount, s.manager_name
FROM consumer c
INNER JOIN orders o ON c.consumer_id = o.consumer_id
INNER JOIN sales_manager s ON o.sales_manager_id = s.sales_manager_id
ORDER BY o.order_date;
