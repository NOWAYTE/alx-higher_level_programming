-- a script that diplays the average temperature 
SELECT city, AVG(value) AS temp FROM temperatures GROUP BY city ORDER BY temp DESC;
