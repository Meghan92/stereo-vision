import MySQLdb
import config


def insert(image):
	connection = config.ConnectionString()
	db = connection.database;
	cursor = db.cursor()
	query = """INSERT INTO Image VALUES ({sid}, '{imt}', '{li}', '{ri}')""".\
		format(sid=image.student_id, imt=image.image_type, li=image.left_image, ri=image.right_image)
	cursor.execute(query)
	db.commit()
	db.close()
	

