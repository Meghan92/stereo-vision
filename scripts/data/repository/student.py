import MySQLdb
import config


def insert(student):
	try:
		
		connection = config.ConnectionString()
		db = connection.database;
		cursor = db.cursor()
		query = """INSERT INTO Student VALUES ({sid}, '{fn}', '{ln}')""".\
			format(sid=student.student_id, fn=student.first_name, ln=student.last_name)
		cursor.execute(query)
		db.commit()
		db.close()
	except MySQLdb.IntegrityError:
		print("ERROR: ID already exists in PRIMARY KEY column {}".format(student.student_id))



