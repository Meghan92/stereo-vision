import webcam
import display
import common.exceptions
import business.image as images

#capture.py is used for recording images
#if an image has not been captured,
#the user has an option to try again
#the capture should also make sure the viewport is closed

def frontal():
	is_captured = 0
	while is_captured == 0:
		is_captured = webcam.capture()

		if is_captured:
			display.types.success("Image Captured Successfully")
		else:
			is_captured = 0
			display.types.fail("Your image was not captured correctly")
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
				

def save(student_id, image_type_id):
	blob_array = webcam.get_blobs()
	array_length = len(blob_array)
	if array_length == 2:
		images.create(student_id, image_type_id, blob_array)
	else:
		raise ValueError("Two images are required for storing to the database. Current length: {}".format(array_length))	
			
