# Write your MySQL query statement below
SELECT id
FROM (SELECT id, temperature, 
LAG(temperature,1) OVER() AS temperature2,
recordDate,
LAG(recordDate,1) OVER() AS recordDate2
FROM weather ORDER BY recordDate ASC) AS two_days_weather
WHERE two_days_weather.temperature > two_days_weather.temperature2 AND DATEDIFF(recordDate, recordDate2)=1
