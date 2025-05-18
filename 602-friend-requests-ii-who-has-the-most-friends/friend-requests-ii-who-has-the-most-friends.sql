# Write your MySQL query statement below
with concated AS(
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)

SELECT id, COUNT(id) AS num
FROM concated
GROUP BY id
HAVING num = (SELECT MAX(counts) FROM (SELECT COUNT(id) AS counts FROM concated GROUP BY id) g)