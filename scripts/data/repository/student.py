import MySQLdb
import config
import time


def insert(student):
	connection = config.ConnectionString()
	db = connection.database;
	cursor = db.cursor()    
	now = time.strftime('%Y-%m-%d %H:%M:%S')
	query = """INSERT INTO Student (student_id, first_name, last_name, create_date)"""\
			"""VALUES ({sid}, '{fn}', '{ln}', '{cdt}')""".\
		format(sid=student.student_id, fn=student.first_name, ln=student.last_name,cdt=now)
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
