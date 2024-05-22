-- THis selects the top three cities witht e highes temperature during 
-- July and August
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY CITY
ORDER BY avg_temp DESC
LIMIT 3;
