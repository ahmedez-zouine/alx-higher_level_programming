-- This Script use for the lists of number record the same score ...
SELECT score , COUNT(*) as number FROM second_table GROUP BY score DESC;
