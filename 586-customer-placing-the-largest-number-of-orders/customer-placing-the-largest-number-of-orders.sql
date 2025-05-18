# Write your MySQL query statement below

SELECT customer_number FROM (SELECT customer_number,COUNT(order_number) AS counted FROM orders GROUP BY customer_number ORDER BY counted DESC) counts LIMIT 1