import scripts.data.model as model
import scripts.data.repository.student as repository

def create(student_id, first_name, last_name):
	student = model.Student(student_id, first_name, last_name)	
	repository.insert(student)
