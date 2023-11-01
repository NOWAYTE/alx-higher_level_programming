-- a script that displays the top 3 cities temperature during July and AUGUST
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DEC LIMIT 3;
