-- Ranks Country origins of bands by number of (non-unique) fans
SELECT band_name, (IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
