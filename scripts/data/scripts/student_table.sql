USE StereoVision;
CREATE TABLE Student(
	student_id INT NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	PRIMARY KEY (student_id)
);

ALTER TABLE Student
ADD create_date date;

ALTER TABLE Student
ADD update_date date;
