import display.types as display


def start():
	display.header("Welcome to the Stereo Vision Verification System")
	print "What would you like to do?\n\n"
	display.number_list(["Login", "Register", "Settings", "Quit"])
	return raw_input("\nEnter a number (e.g. 1): ")


