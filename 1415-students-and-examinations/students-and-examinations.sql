# Write your MySQL query statement below
WITH Examinations_grouped AS(
    SELECT *, COUNT(*) AS attended_exams FROM Examinations
    GROUP BY student_id, subject_name
)

SELECT Students.student_id, Students.student_name, Subjects.subject_name, COALESCE(Examinations_grouped.attended_exams,0) AS attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN Examinations_grouped
ON Students.student_id=Examinations_grouped.student_id
AND Subjects.subject_name = Examinations_grouped.subject_name
ORDER BY student_id, subject_name