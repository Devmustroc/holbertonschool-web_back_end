-- Title: Glam Rock
-- Description: Glam Rock bands and their lifespan
-- Database: metal_bands
SELECT DISTINCT `band_name`,
                IFNULL(`split`,  2023) - `formed` AS `lifespan`
FROM `metal_bands` WHERE FIND_IN_SET('Glam Rock', `style`)
ORDER BY `lifespan` DESC;

