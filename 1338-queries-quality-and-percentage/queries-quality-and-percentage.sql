# Write your MySQL query statement below
SELECT query_name,
ROUND(AVG(rating/`position`),2) AS quality,
ROUND(SUM(IF(rating<3,1,0))*100/COUNT(rating),2) AS poor_query_percentage
FROM queries
GROUP BY
query_name
