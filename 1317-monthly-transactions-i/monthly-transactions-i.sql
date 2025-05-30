# Write your MySQL query statement below
SELECT 
    LEFT(trans_date,7) AS month,
    country,
    COUNT(state) AS trans_count,
    COUNT(IF(state='approved',1,null)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state='approved',amount,0)) AS approved_total_amount
FROM Transactions
GROUP BY YEAR(trans_date), MONTH(trans_date),country