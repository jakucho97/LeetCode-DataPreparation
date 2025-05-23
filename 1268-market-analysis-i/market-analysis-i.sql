# Write your MySQL query statement below
WITH grouped AS(
    SELECT COUNT(order_id) AS orders_in_2019, buyer_id
    FROM Orders
    WHERE YEAR(order_date)=2019
    GROUP BY buyer_id
)

SELECT users.user_id AS buyer_id, users.join_date, COALESCE(grouped.orders_in_2019,0) AS orders_in_2019
FROM users
LEFT JOIN grouped
ON users.user_id=grouped.buyer_id