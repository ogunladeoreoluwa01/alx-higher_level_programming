-- This groups the scores aording to frequency
SELECT score AS "score",
COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
