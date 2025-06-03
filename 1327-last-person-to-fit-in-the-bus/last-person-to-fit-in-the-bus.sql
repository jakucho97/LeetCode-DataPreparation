# Write your MySQL query statement below
SELECT person_name
FROM (SELECT person_name, turn, SUM(weight) OVER(ORDER BY turn) AS cumsum FROM Queue) test
WHERE cumsum <=1000
ORDER BY turn DESC
LIMIT 1
