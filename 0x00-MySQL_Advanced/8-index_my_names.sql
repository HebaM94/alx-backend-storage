-- Creates index on the table names using first letter of name 
CREATE INDEX idx_name_first ON names (name(1));