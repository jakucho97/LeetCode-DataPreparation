# Write your MySQL query statement below
SELECT mgr.employee_id, mgr.name, COUNT(mgr.name) AS reports_count,ROUND(AVG(emp.age),0) AS average_age
FROM Employees mgr
JOIN
Employees emp
ON
mgr.employee_id = emp.reports_to
GROUP BY mgr.employee_id
ORDER BY employee_id

