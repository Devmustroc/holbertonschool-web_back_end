-- SQL script creates a trigger that decreases the quantity of
-- an item adding a new order.
-- quantity in the table items can be negative.

DELIMITER //
CREATE TRIGGER decrease AFTER INSERT
ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_id;
END;//
DELIMITER ;