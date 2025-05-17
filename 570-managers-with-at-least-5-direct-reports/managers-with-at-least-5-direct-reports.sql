# Write your MySQL query statement below
with counting AS(
SELECT managerId, COUNT(*) AS counted
FROM Employee
GROUP BY managerId
HAVING counted>=5)

SELECT name
FROM Employee
WHERE id IN (SELECT managerId FROM counting)