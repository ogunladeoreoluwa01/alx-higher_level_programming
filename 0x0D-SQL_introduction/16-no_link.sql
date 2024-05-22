-- This shows all the records of the table with a non null name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC, name;
