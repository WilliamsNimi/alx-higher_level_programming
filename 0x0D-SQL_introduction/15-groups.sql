-- Number by score
SELECT score AS "score", COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
