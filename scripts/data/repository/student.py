import MySQLdb
import config


def insert(student):
	connection = config.ConnectionString()
	db = connection.database;
	cursor = db.cursor()
	query = """INSERT INTO Student VALUES ({sid}, '{fn}', '{ln}')""".\
		format(sid=student.student_id, fn=student.first_name, ln=student.last_name)
	cursor.execute(query)
	db.commit()
	db.close()
	
	
def get(student_id):
	connection = config.ConnectionString()
	db = connection.database;
	cursor = db.cursor()
	query = """SELECT * FROM Student WHERE student_id = {}""".format(student_id)
	cursor.execute(query)
	db.commit()
	db.close()
	return cursor.fetchone()
