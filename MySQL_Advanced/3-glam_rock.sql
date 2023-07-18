-- Title: Glam Rock
-- Description: Glam Rock bands and their lifespan
-- Database: metal_bands
SELECT band_name, (IFNULL(split, YEAR(CURDATE())) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
