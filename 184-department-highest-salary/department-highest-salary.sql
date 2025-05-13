# Write your MySQL query statement below
SELECT Department.name AS Department, e.name AS Employee, e.salary AS Salary
FROM 
(SELECT id, name, salary, departmentId, DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) `rank` FROM Employee) AS e
LEFT JOIN Department ON e.departmentId = Department.id
WHERE e.`rank` = 1