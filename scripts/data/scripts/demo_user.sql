CREATE USER 'demo'@'localhost' IDENTIFIED BY 'D3M0U53R';
GRANT UPDATE, SELECT, CREATE, INSERT, DELETE ON StereoVision . Student TO 'demo'@'localhost';
GRANT UPDATE, SELECT, CREATE, INSERT, DELETE ON StereoVision . Image TO 'demo'@'localhost';
GRANT UPDATE, SELECT, CREATE, INSERT, DELETE ON StereoVision . ImageType TO 'demo'@'localhost';
