import display.types as display
import business.student
import data.model


def start(student_number):
	display.header("Registration")
	details_confirmed = False
	while not details_confirmed:
		if student_number is None:
			student_id = raw_input("Please enter your student number (e.g. 123456789): ")
		else:
			student_id = raw_input("Please enter your student number (enter to confirm {}): ".format(student_number))
			if student_id == "":
				student_id = student_number
			display.success("Student number: {}".format(student_id))
		first_name = raw_input("Please enter your first name: ")
		last_name = raw_input("Please enter your last name: ")
		display.warning("About to create {surname}, {name} ({number})".format(surname=last_name,name=first_name,number=student_id))
		details_confirmed = raw_input("Are the above details correct? (y/n):") == "y"	
	response = business.student.create(student_id, first_name, last_name)
	if response.success:
		display.success("{}: Your credentials were created successfully".format(response.message))
	else:
		display.fail("Something went wrong during registration: {}".format(response.message))
	return response.success, student_id
		
	
def compare():
	display.header("Comparing Images")
	#TODO: Start comparing images captured
	
