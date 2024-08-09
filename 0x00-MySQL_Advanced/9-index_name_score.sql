-- Creates index on the table names using first letter of name and scores 
CREATE INDEX idx_name_first_score ON names (name(1), score);