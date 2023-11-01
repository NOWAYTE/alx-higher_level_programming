-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) AS tmp FROM temperatures GROUP by CITY ORDER BY tmp DESC;
