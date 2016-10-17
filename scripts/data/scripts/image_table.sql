USE StereoVision;
CREATE TABLE ImageType(
	image_type_id INT NOT NULL AUTO_INCREMENT,
	image_type VARCHAR(50),
	PRIMARY KEY (image_type_id)
);

CREATE TABLE Image(
	student_id INT NOT NULL,
	image_type_id INT NOT NULL,
	left_image BLOB NOT NULL,
	right_image BLOB NOT NULL,
	FOREIGN KEY (student_id) REFERENCES Student(student_id),
	FOREIGN KEY (image_type_id) REFERENCES ImageType(image_type_id),
	PRIMARY KEY (student_id, image_type_id)
);

INSERT INTO ImageType(image_type) values('Frontal');

ALTER TABLE ImageType
ADD create_date datetime;
ALTER TABLE ImageType
ADD update_date datetime;

ALTER TABLE Image
ADD create_date datetime;
ALTER TABLE Image
ADD update_date datetime;
ALTER TABLE Image
MODIFY left_image LONGBLOB NOT NULL;
ALTER TABLE Image
MODIFY right_image LONGBLOB NOT NULL;
