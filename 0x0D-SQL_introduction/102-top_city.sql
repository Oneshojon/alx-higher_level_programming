-- Write a script that displays the top 3 of cities temperature during
-- July and August ordered by temperature (descending)
SELECT city, value
FROM temperatures
WHERE month = July OR month = August
ORDER BY value DESC
LIMIT 3;
