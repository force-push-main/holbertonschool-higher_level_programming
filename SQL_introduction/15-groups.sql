-- lists number of records with same score
SELECT COUNT(score) AS number
FROM `second_table`
HAVING COUNT(*) > 1
ORDER BY number DESC;
