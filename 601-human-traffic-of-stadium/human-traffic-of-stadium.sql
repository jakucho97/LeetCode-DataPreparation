# Write your MySQL query statement below
with consecutive AS (SELECT *, id-(ROW_NUMBER() OVER(ORDER BY id ASC)) AS cons FROM Stadium WHERE people>=100)

SELECT id, visit_date, people
FROM (SELECT *, COUNT(*) OVER(PARTITION BY cons) AS counted FROM consecutive) temp
WHERE counted>=3
ORDER BY id


