# Write your MySQL query statement below
SELECT weather.id AS id
FROM weather
JOIN weather AS w
ON DATEDIFF(weather.recorddate, w.recorddate) = 1
AND weather.temperature > w.temperature;