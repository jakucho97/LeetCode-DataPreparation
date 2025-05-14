# Write your MySQL query statement below
WITH ranked AS(
    SELECT 
        employee.name AS Employee,
        salary AS Salary,
        departmentId,
        department.name AS Department,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY Salary DESC) AS `rank`
    FROM 
        employee
    LEFT JOIN Department ON employee.departmentId = department.id)

SELECT Department, Employee, Salary
FROM ranked
WHERE `rank`<=3

