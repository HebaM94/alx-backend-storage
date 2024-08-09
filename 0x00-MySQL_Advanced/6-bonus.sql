-- Creates a procedure for AddBonus that adds a new correction for a student
DELIMITER $
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name CHAR(255), IN score INT)
BEGIN
    SET @project_id = (SELECT id from projects WHERE name=project_name);
    IF @project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET @project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
END$
DELIMITER ;