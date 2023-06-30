-- Ranks Country origins of bands by number of (non-unique) fans
SELECT origin, COUNT(*) AS fans_count
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;