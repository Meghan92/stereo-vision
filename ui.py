import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'verification'))
import common.constants as constants

def header(message):
	print constants.LINE + constants.color_codes.OKBLUE + message + constants.color_codes.ENDC + constants.LINE
	

def success(message):
	print constants.color_codes.OKGREEN + constants.LINE +  message + constants.LINE + constants.color_codes.ENDC
	
	
def fail(message):
	print constants.color_codes.FAIL + constants.LINE + message + constants.LINE +  constants.color_codes.ENDC
	
	
def warning(message):
	print constants.color_codes.WARNING + constants.LINE + message + constants.LINE + constants.color_codes.ENDC