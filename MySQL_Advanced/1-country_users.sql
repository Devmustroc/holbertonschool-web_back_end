-- Create table users with columns id, email, name, country.
-- Country ennumerated type with values: 'US', 'CO', And 'TN'.
-- Country Never Null default will be the US.
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
