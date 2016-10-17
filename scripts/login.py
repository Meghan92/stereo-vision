import display.types as display
import business.student
import common.exceptions as errors


def start():
	display.header("Login")
	student_number = raw_input("Please enter your student number (e.g. 123456789):")
	student = business.student.get(student_number)
	if student is not None:
		return student_number
	else:
		raise errors.InvalidLogin("Student number {} does not exist in database.".format(student_number), student_number)
	
