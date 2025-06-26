# Write your MySQL query statement below
SELECT users.name, SUM(amount) AS BALANCE
FROM Transactions
JOIN Users
ON Transactions.account=Users.account
GROUP BY Transactions.account
HAVING SUM(amount)>10000