CREATE TABLE students (
    id INTEGER,
    student_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    name TEXT,
    house TEXT,
    PRIMARY KEY(name)
);

CREATE TABLE house_assignments (
    house TEXT,
    head TEXT,
    PRIMARY KEY(head)
);

SELECT id, student_name, houses.house, house_assignments.head FROM students
    JOIN houses ON houses.name = students.student_name
        JOIN house_assignments ON house_assignments.house = houses.house;

