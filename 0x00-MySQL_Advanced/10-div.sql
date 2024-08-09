-- Creates a function SafeDiv that divides
-- (and returns) the first number by the
-- second number or returns 0 if the second number is 0
DELIMITER $
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    DECLARE res FLOAT DEFAULT 0;
    IF b != 0 THEN
        SET res = a / b;
    END IF;
    RETURN res;
END$
DELIMITER ;