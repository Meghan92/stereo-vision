import display.types as display
import common.enum as enum


def start():
	display.clear()
	display.header("Welcome to the Stereo Vision Verification System")
	print "What would you like to do?\n\n"
	display.number_list(["Login", "Register", "Settings", "Quit"])
	response = raw_input("\nEnter a number (e.g. 1): ")
	if response == "1":
		return enum.menu.LOGIN
	if response == "2":
		return enum.menu.REGISTER
	if response == "3":
		return enum.menu.SETTINGS
	if response == "4":
		return enum.menu.QUIT


def register_fail():
	print "What would you like to do?\n\n"
	display.number_list(["Retry","Return to Menu"])
	response = raw_input("\nEnter a number (e.g. 1): ")
	if response == "1":
		return enum.menu.REGISTER
	if response == "2":
		return enum.menu.RETURN
		

def login_invalid():
	display.fail("Your details do not exist in the system")
	print "What would you like to do?\n\n"
	display.number_list(["Retry","Register","Return to Menu"])
	response = raw_input("\nEnter a number (e.g. 1): ")
	if response == "1":
		return enum.menu.LOGIN
	if response == "2":
		return enum.menu.REGISTER
	if response == "3":
		return enum.menu.RETURN
