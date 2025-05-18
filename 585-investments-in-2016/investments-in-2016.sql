# Write your MySQL query statement below
SELECT round(sum(tiv_2016),2) as tiv_2016
FROM Insurance
WHERE
Insurance.tiv_2015 IN (SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(pid)>1)
AND
(Insurance.lat, Insurance.lon) IN (SELECT lat,lon FROM Insurance GROUP BY lat,lon HAVING COUNT(pid)=1)