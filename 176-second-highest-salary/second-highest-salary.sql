# Write your MySQL query statement below
SELECT(
SELECT salary
FROM (SELECT DISTINCT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS ranking FROM Employee) AS rtw
WHERE ranking = 2) AS SecondHighestSalary
