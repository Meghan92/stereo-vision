import webcam
import display
import display.webcam
import common.exceptions

#capture.py is used for recording images
#if an image has not been captured,
#the user has an option to try again
#the capture should also make sure the viewport is closed

def frontal():
	is_captured = 0
	while is_captured == 0:
		is_captured = webcam.capture()

		if is_captured:
			display.webcam.success()
		else:
			is_captured = 0
			display.webcam.fail()
			#read in if user would like to try again
			valid_input = 0
			while valid_input == 0:
				try_again = raw_input("Try again? (y/n):")
				if try_again == "y":
					valid_input = 1
					continue
				if try_again == "n":
					valid_input = 1
					raise common.exceptions.CaptureError()
				print("\nInvalid input (" + try_again + ") Please either specify \"y\" or \"n\"")
			
			
			
