# Write your MySQL query statement below
WITH first_login AS(
    SELECT player_id, MIN(event_date) AS first_login
    FROM activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(*)/ (SELECT COUNT(*) FROM first_login),2) AS fraction
FROM activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) IN (SELECT player_id, first_login FROM first_login)
