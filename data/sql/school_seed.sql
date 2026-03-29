-- Sample data for school.db (English)

PRAGMA foreign_keys = ON;

INSERT INTO departments (code, name) VALUES
    ('CS', 'Computer Science'),
    ('MATH', 'Mathematics'),
    ('ENG', 'English Literature');

INSERT INTO rooms (building, room_number, capacity) VALUES
    ('Science Hall', '101', 40),
    ('Science Hall', 'Lab-A', 24),
    ('Liberal Arts', '205', 35);

INSERT INTO teachers (employee_number, first_name, last_name, email, phone, department_id, hire_date, job_title) VALUES
    ('T-1001', 'Alice', 'Nguyen', 'alice.nguyen@school.edu', '555-0101', 1, '2018-08-15', 'Associate Professor'),
    ('T-1002', 'Robert', 'Chen', 'robert.chen@school.edu', '555-0102', 1, '2015-01-10', 'Professor'),
    ('T-2001', 'Maria', 'Garcia', 'maria.garcia@school.edu', '555-0201', 2, '2019-08-20', 'Assistant Professor'),
    ('T-3001', 'James', 'Wright', 'james.wright@school.edu', '555-0301', 3, '2012-08-01', 'Professor');

INSERT INTO students (student_number, first_name, last_name, email, phone, date_of_birth, enrollment_date, status) VALUES
    ('S-50001', 'Emma', 'Johnson', 'emma.j@student.school.edu', '555-5001', '2004-03-12', '2022-09-01', 'active'),
    ('S-50002', 'Liam', 'Martinez', 'liam.m@student.school.edu', '555-5002', '2003-11-02', '2022-09-01', 'active'),
    ('S-50003', 'Olivia', 'Lee', 'olivia.l@student.school.edu', '555-5003', '2004-07-21', '2023-09-01', 'active'),
    ('S-50004', 'Noah', 'Patel', 'noah.p@student.school.edu', '555-5004', '2002-05-30', '2021-09-01', 'active'),
    ('S-50005', 'Ava', 'Kim', 'ava.k@student.school.edu', '555-5005', '2005-01-14', '2024-09-01', 'active'),
    ('S-50006', 'Ethan', 'Brown', 'ethan.b@student.school.edu', '555-5006', '2003-09-09', '2022-09-01', 'withdrawn');

INSERT INTO student_guardians (student_id, full_name, email, phone, relationship) VALUES
    (1, 'Sarah Johnson', 'sarah.j@email.com', '555-6001', 'Mother'),
    (1, 'Tom Johnson', 'tom.j@email.com', '555-6002', 'Father'),
    (3, 'Helen Lee', 'helen.l@email.com', '555-6003', 'Mother'),
    (5, 'David Kim', 'david.k@email.com', '555-6004', 'Father');

INSERT INTO courses (code, title, credits, department_id, description) VALUES
    ('CS101', 'Introduction to Programming', 4, 1, 'Python and problem solving.'),
    ('CS201', 'Data Structures', 4, 1, 'Lists, trees, graphs, algorithms.'),
    ('CS301', 'Databases', 3, 1, 'SQL, design, and transactions.'),
    ('MATH150', 'Calculus I', 4, 2, 'Limits, derivatives, integrals.'),
    ('MATH151', 'Calculus II', 4, 2, 'Series and multivariable intro.'),
    ('ENG110', 'Composition', 3, 3, 'Academic writing and rhetoric.');

INSERT INTO course_prerequisites (course_id, prerequisite_course_id) VALUES
    (2, 1),
    (3, 2),
    (5, 4);

INSERT INTO course_offerings (course_id, teacher_id, semester, year, section_number, room_id, schedule_text) VALUES
    (1, 1, 'spring', 2026, 1, 1, 'Mon Wed Fri 09:00-10:00'),
    (2, 2, 'spring', 2026, 1, 2, 'Tue Thu 11:00-12:30'),
    (4, 3, 'spring', 2026, 1, 3, 'Mon Wed Fri 10:00-11:00'),
    (6, 4, 'spring', 2026, 1, 1, 'Tue Thu 14:00-15:15'),
    (3, 1, 'fall', 2025, 1, 2, 'Mon Wed 13:00-14:30');

INSERT INTO enrollments (student_id, offering_id, enrolled_at, status, final_grade) VALUES
    (1, 1, '2026-01-10', 'enrolled', NULL),
    (2, 1, '2026-01-10', 'enrolled', NULL),
    (3, 2, '2026-01-12', 'enrolled', NULL),
    (4, 3, '2026-01-08', 'enrolled', NULL),
    (1, 4, '2026-01-09', 'enrolled', NULL),
    (2, 4, '2026-01-09', 'completed', 'A-'),
    (4, 5, '2025-09-05', 'completed', 'B+'),
    (3, 5, '2025-09-06', 'completed', 'A');
