# Write your MySQL query statement below
SELECT 
id,
CASE
    WHEN id%2=0 THEN LAG(student) OVER()
    ELSE COALESCE(LEAD(student) OVER(), student)
END AS student
FROM Seat