# Write your MySQL query statement below
SELECT DISTINCT customer_id
FROM Customer
WHERE Customer.product_key IN (SELECT product_key FROM Product)
GROUP BY customer_id
HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product)