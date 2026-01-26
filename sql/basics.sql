-- Create students table (INPUT)
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    marks INT
);
-- Insert sample data (INPUT)
INSERT INTO students VALUES
(1, 'Arjun', 'CSE', 85),
(2, 'Meera', 'ECE', 72),
(3, 'Rahul', 'CSE', 90),
(4, 'Anita', 'ME', 65),
(5, 'Kiran', 'ECE', 80);

-- View all students (OUTPUT)
SELECT * FROM students;

SELECT name, marks FROM students WHERE marks > 75;
SELECT name, marks FROM students ORDER BY marks DESC;
SELECT department, COUNT(*) AS total_students FROM students GROUP BY department;
SELECT AVG(marks) AS average_marks FROM students;
