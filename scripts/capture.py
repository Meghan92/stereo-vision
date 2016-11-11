import webcam
import display
import common.exceptions
import business.image as images
import services.verification.capture.output as output
import shutil, os

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
				print("\nInvalid input (" + try_again + ") Please either\
				 specify \"y\" or \"n\"")
				

def save(student_id, image_type_id):
	blob_array = webcam.get_blobs()
	array_length = len(blob_array)
	if array_length == 2:
		images.create(student_id, image_type_id, blob_array)
	else:
		raise ValueError("Two images are required for storing to the database.\
		 Current length: {}".format(array_length))
		
		
def training():
	display.types.header("Face Capture Automation")
	print "Face Capture Automation is a setting used to capture multiple images into"
	print "a dataset for training purposes.\nWhich database would you like to use?\n\n"
	paths = output.get_database_paths()
	count = 0
	for path in paths:
		count += 1
		print "[" + str(count) + "] " + path
	input = raw_input("\nEnter a number (e.g. 1): ").lower()
	database_num = int(input) - 1
	filename = paths[database_num]
	display.types.warning("Your pictures will be saved to the \"{}\" database".format(filename))
	input = raw_input("Are you sure? (y/n): ").lower()
	if input == "y":
		return filename
	else:
		return None
		
		
def training_save(filename):
	display.types.header("Saving Face")
	file_path = os.path.dirname(os.path.realpath(__file__))
	source_path = os.path.join(file_path, "output")
	services_path = os.path.join(file_path, "services")
	verification_path = os.path.join(services_path, "verification")
	capture_path = os.path.join(verification_path, "capture")
	database_path = os.path.join(capture_path, "database")
	chosen_path = os.path.join(database_path, filename)
	directories = os.listdir(chosen_path)
	index_path = "1"
	if len(directories) > 0:
		index_path = str(max([int(numbers) for numbers in directories]) + 1)
	destination_path = os.path.join(chosen_path, index_path)
	os.makedirs(destination_path)
	for images in os.listdir(source_path):
		simage_path = os.path.join(source_path, images)
		shutil.move(simage_path, destination_path)
	input = raw_input("Image Saved. There are {} image(s) in database. Continue? (y/n): ".format(index_path)).lower()
	if input == "y":
		return True
	else:
		return False
	
	
	
	
		
	
	
	
	
	
	
			
