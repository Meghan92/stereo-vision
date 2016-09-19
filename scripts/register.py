import display.types as display
import business.student
import data.model


def start():
	display.header("Registration")
	student_id = raw_input("Please enter your student number (e.g. 123456789): ")
	first_name = raw_input("Please enter your first name: ")
	last_name = raw_input("Please enter your last name: ")
	response = business.student.create(student_id, first_name, last_name)
	if response.success:
		display.success("{}: Your credentials were created successfully".format(response.message))
	else:
		display.fail("Something went wrong during registration: {}".format(response.message))
	return response.success
		
	
def compare():
	display.header("Comparing Images")
	#TODO: Start comparing images captured
	
