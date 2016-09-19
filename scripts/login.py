import display.types as display
import business.student


def start():
	display.header("Login")
	student_number = raw_input("Please enter your student number (e.g. 123456789):")
	student = business.student.get(student_number)
	if student is not None:
		return True
	else:
		return False
	
