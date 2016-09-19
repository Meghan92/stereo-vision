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
		

def get(student_id):
	response = repository.get(student_id)
	if response:
		return model.Student(response[0], response[1], response[2])
	else:
		return None
