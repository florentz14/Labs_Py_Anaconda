-- School management database (SQLite)
-- Departments, rooms, teachers, students, guardians, courses, offerings, enrollments.

PRAGMA foreign_keys = ON;

-- Academic departments (e.g. Computer Science, Mathematics)
CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL
);

-- Physical rooms for lectures and labs
CREATE TABLE rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    building TEXT NOT NULL,
    room_number TEXT NOT NULL,
    capacity INTEGER NOT NULL CHECK (capacity > 0),
    UNIQUE (building, room_number)
);

-- Teaching staff
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_number TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    department_id INTEGER NOT NULL REFERENCES departments (id),
    hire_date TEXT NOT NULL,
    job_title TEXT NOT NULL,
    CHECK (email LIKE '%@%')
);
CREATE INDEX idx_teachers_department ON teachers (department_id);

-- Enrolled students
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_number TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    date_of_birth TEXT NOT NULL,
    enrollment_date TEXT NOT NULL,
    status TEXT NOT NULL CHECK (
        status IN ('active', 'graduated', 'withdrawn', 'suspended')
    ),
    CHECK (email LIKE '%@%')
);

-- Emergency / billing contacts for minors or next of kin
CREATE TABLE student_guardians (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES students (id) ON DELETE CASCADE,
    full_name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    relationship TEXT NOT NULL
);
CREATE INDEX idx_guardians_student ON student_guardians (student_id);

-- Catalog of courses (not a specific semester instance)
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    credits INTEGER NOT NULL CHECK (credits > 0 AND credits <= 30),
    department_id INTEGER NOT NULL REFERENCES departments (id),
    description TEXT
);
CREATE INDEX idx_courses_department ON courses (department_id);

-- Prerequisite: must pass prereq_course before taking course
CREATE TABLE course_prerequisites (
    course_id INTEGER NOT NULL REFERENCES courses (id) ON DELETE CASCADE,
    prerequisite_course_id INTEGER NOT NULL REFERENCES courses (id) ON DELETE CASCADE,
    PRIMARY KEY (course_id, prerequisite_course_id),
    CHECK (course_id != prerequisite_course_id)
);

-- A scheduled section (course in a given term with one instructor)
CREATE TABLE course_offerings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL REFERENCES courses (id),
    teacher_id INTEGER NOT NULL REFERENCES teachers (id),
    semester TEXT NOT NULL CHECK (
        semester IN ('fall', 'spring', 'summer', 'winter')
    ),
    year INTEGER NOT NULL CHECK (year >= 2000 AND year <= 2100),
    section_number INTEGER NOT NULL DEFAULT 1 CHECK (section_number >= 1),
    room_id INTEGER REFERENCES rooms (id),
    schedule_text TEXT,
    UNIQUE (course_id, semester, year, section_number)
);
CREATE INDEX idx_offerings_course ON course_offerings (course_id);
CREATE INDEX idx_offerings_teacher ON course_offerings (teacher_id);

-- Student registration in a section; grade when completed
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES students (id),
    offering_id INTEGER NOT NULL REFERENCES course_offerings (id),
    enrolled_at TEXT NOT NULL,
    status TEXT NOT NULL CHECK (
        status IN ('enrolled', 'dropped', 'completed', 'incomplete')
    ),
    final_grade TEXT,
    UNIQUE (student_id, offering_id)
);
CREATE INDEX idx_enrollments_student ON enrollments (student_id);
CREATE INDEX idx_enrollments_offering ON enrollments (offering_id);
