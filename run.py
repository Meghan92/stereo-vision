import verification.capture.webcam as webcam
import verification.capture.output as capture_output
import cmd
import verification.constants as constants
import verification.preprocessing.training as preprocess_training
import verification.preprocessing.main as preprocess
import verification.processing.main as process
import verification.ann.predict as predict
import verification.ann.main as train


def run():
	try:
		print constants.LINE + constants.color_codes.OKBLUE + "Capturing Face" + constants.color_codes.ENDC + constants.LINE
		input = raw_input("Press any key when ready: ")
		webcam.capture()
		print constants.LINE + constants.color_codes.OKBLUE + "Saving capture" + constants.color_codes.ENDC + constants.LINE
		input = raw_input("Would you like to save your images to the database for training? (y/n): ").lower()
		if input == "y":
			save_capture()
		ran_training = train_pre_processing()
		if ran_training == "y":
			process.run(1)
			train.run()
		else:
			test_pre_processing()
			byte_array = process.run(0)
			print constants.LINE + constants.color_codes.OKBLUE + "Verifying" + constants.color_codes.ENDC + constants.LINE
			verified = predict.run(byte_array)
			if verified > 0:
				print constants.color_codes.OKGREEN + "Your image has been verified. Running recognition." + constants.color_codes.ENDC
			else:
				raise ReferenceError("Face not verified, your image has been logged.")
	except ReferenceError as refError:
		print constants.color_codes.FAIL + "An error occurred: " + refError.message + constants.color_codes.ENDC


def test_pre_processing():
	print constants.LINE + constants.color_codes.OKBLUE + "Preprocessing" + constants.color_codes.ENDC + constants.LINE
	preprocess.run()
	
	
def save_capture():
	paths = capture_output.get_database_paths()
	count = 0
	print "The following databases are: "
	for path in paths:
		count += 1
		print "[" + str(count) + "] " + path
	input = raw_input("Which database number would you like to save to? (#): ").lower()
	database_num = int(input) - 1
	filename = paths[database_num]
	input = raw_input("Your picture will be saved to the \"%s\" database. Are you sure? (y/n): " % (filename))
	number = webcam.save_to_database(filename)
	print "Your image has been saved to the \"%s\" database, which now has %s records" % (filename, number)
	
	
def train_pre_processing():
	input = raw_input("Would you like to run the training network? (y/n): ").lower()
	if input == "y":
		print constants.LINE + constants.color_codes.OKBLUE + "Preprocessing, please wait patiently..." + constants.color_codes.ENDC + constants.LINE
		preprocess_training.run()
	return input
	
run()