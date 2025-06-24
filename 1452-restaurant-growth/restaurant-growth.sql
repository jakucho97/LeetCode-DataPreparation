# Write your MySQL query statement below
WITH grouped AS(
    SELECT customer_id, name, visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)

SELECT visited_on, amount_s AS amount, average_amount
FROM
(SELECT *,
CASE WHEN
    ROW_NUMBER() OVER(ORDER BY visited_on)>=7 THEN
        ROUND(SUM(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2)
ELSE NULL
END AS amount_s,

CASE WHEN
    ROW_NUMBER() OVER(ORDER BY visited_on)>=7 THEN
        ROUND(AVG(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2)
ELSE NULL
END AS average_amount
FROM grouped) AS new
WHERE average_amount IS NOT NULL