-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- * user_id, a users.id value (you can assume user_id is linked to an existing users)

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE project_count INT;
    SELECT SUM(score), COUNT(*) INTO total_score, project_count
    FROM corrections
    WHERE user_id = user_id;
    UPDATE users
    SET average_score = total_score / project_count
    WHERE id = user_id;
END //

DELIMITER ;
