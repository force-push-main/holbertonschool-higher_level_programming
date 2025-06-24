-- lists number of records with same score
SELECT score, COUNT(score) AS number
FROM `second_table`
HAVING COUNT(*) > 0
ORDER BY number ASC;
