import MySQLdb
import config
import time


def insert(image):
	print image.student_id
	connection = config.ConnectionString()
	db = connection.database;
	cursor = db.cursor()
	now = time.strftime('%Y-%m-%d %H:%M:%S')
	query = """INSERT INTO Image (student_id, image_type_id, create_date, left_image, right_image) VALUES ({sid}, '{imt}', '{cdt}', '{li}', '{ri}')""".\
		format(sid=image.student_id, imt=image.image_type, cdt=now, li=image.left_image, ri=image.right_image)
	cursor.execute(query)
	db.commit()
	db.close()
	

def get(student_id, image_type_id):
	connection = config.ConnectionString()
	db = connection.database;
	cursor = db.cursor()
	query = """SELECT * FROM Image WHERE student_id = '{sid}' AND image_type_id = '{imt}'""".\
		format(sid=student_id, imt=image_type_id)
	cursor.execute(query)
	db.commit()
	db.close()
	return cursor.fetchone()
	
	
def get_type(image_type_id):
	connection = config.ConnectionString()
	db = connection.database;
	cursor = db.cursor()
	query = """SELECT * FROM ImageType WHERE image_type_id = '{imt}'""".\
		format(imt=image_type_id)
	cursor.execute(query)
	db.commit()
	db.close()
	return cursor.fetchone()
