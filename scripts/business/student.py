import scripts.data.model as model
import scripts.data.repository.student as repository
import MySQLdb

def create(student_id, first_name, last_name):
	try:
		student = model.Student(student_id, first_name, last_name)	
		repository.insert(student)
		return model.CompoundResponse(True, "Created")
	except MySQLdb.IntegrityError as error:
		return model.CompoundResponse(False, "User {} already exists in the database".format(student_id))
