import constants
import os


def header(message):
	print constants.text.LINE + constants.colour.BLUE + message + constants.colour.ENDC + constants.text.LINE
	

def success(message):
	print constants.colour.GREEN + constants.text.LINE +  message + constants.text.LINE + constants.colour.ENDC
	
	
def fail(message):
	print constants.colour.RED + constants.text.LINE + message + constants.text.LINE +  constants.colour.ENDC
	
	
def warning(message):
	print constants.colour.WARNING + constants.text.LINE + message + constants.text.LINE + constants.colour.ENDC
	
	
def clear():
	os.system('clear')


def number_list(message_array):
	number = 1
	for message in message_array:
		print constants.text.TAB + "[" + str(number) + "] " + message
		number+=1
