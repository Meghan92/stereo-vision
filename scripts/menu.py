import display.types as display
import common.enum as enum


def start():
	#display.clear()
	display.header("Welcome to the Stereo Vision Verification System")
	print "What would you like to do?\n\n"
	display.number_list(["Login", "Register", "Settings", "Quit"])
	response = raw_input("\nPlease enter a valid number (e.g. 1): ")
	if response == "1":
		return enum.menu.LOGIN
	if response == "2":
		return enum.menu.REGISTER
	if response == "3":
		return enum.menu.SETTINGS
	if response == "4":
		return enum.menu.QUIT
	return enum.menu.RETURN


def register_fail():
	print "What would you like to do?\n\n"
	display.number_list(["Retry","Return to Menu"])
	response = raw_input("\nEnter a number (e.g. 1): ")
	if response == "1":
		return enum.menu.REGISTER
	if response == "2":
		return enum.menu.RETURN
		

def login_invalid(message, student_number):
	display.fail(message)
	print "What would you like to do?\n\n"
	display.number_list(["Retry","Register","Return to Menu"])
	response = raw_input("\nEnter a number (e.g. 1): ")
	if response == "1":
		return enum.menu.LOGIN, student_number
	if response == "2":
		return enum.menu.REGISTER, student_number
	if response == "3":
		return enum.menu.RETURN, student_number
		
def verify_option(OPTION):
	if not OPTION.isdigit() or OPTION == enum.menu.INVALID:
		return enum.menu.INVALID
	else:
		return OPTION
	
		
def training():
	display.header("Training")
	print "Which algorithm would you like to use?\n\n"
	display.number_list(["Verification","Recognition","Cancel"])
	response = raw_input("\nEnter a number (e.g. 1): ")
	if response == "1":
		return enum.train.VERIFICATION
	elif response == "2":
		return enum.train.RECOGNITION
	elif response == "3":
		return enum.train.CANCEL
	
	
	
