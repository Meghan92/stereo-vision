import cmd, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'verification'))
import capture.webcam as webcam
import capture.output as capture_output
import common.constants as constants
import preprocessing.training as preprocess_training
import preprocessing.test as preprocess
import processing.main as process
import ann.predict as predict
import ann.main as train
import common.exception as customException
sys.path.append(os.path.join(os.path.dirname(__file__), 'recognition'))
import preprocess as recognition_preprocess


try:
	print constants.LINE + constants.color_codes.OKBLUE + "Capturing Face" + constants.color_codes.ENDC + constants.LINE
	input = raw_input("Press any key when ready: ")
	webcam.capture()
	print constants.LINE + constants.color_codes.OKBLUE + "Saving capture" + constants.color_codes.ENDC + constants.LINE
	input = raw_input("Would you like to save your images to the database for training? (y/n): ").lower()
	
	if input == "y":
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
		
	input = raw_input("Would you like to run the training network? (y/n): ").lower()
	
	if input == "y":
		print constants.LINE + constants.color_codes.OKBLUE + "Preprocessing, please wait patiently..." + constants.color_codes.ENDC + constants.LINE
		preprocess_training.run()
		process.run(1)
		train.run()
	else:
		print constants.LINE + constants.color_codes.OKBLUE + "Preprocessing" + constants.color_codes.ENDC + constants.LINE
		preprocess.run()
		byte_array = process.run(0)
		print constants.LINE + constants.color_codes.OKBLUE + "Verifying" + constants.color_codes.ENDC + constants.LINE
		verified = predict.run(byte_array)
		if verified > 0:
			print constants.color_codes.OKGREEN + "Your image has been verified. Running recognition." + constants.color_codes.ENDC
		else:
			raise customException.VerificationFailure("Face not verified, your image has been logged.")
except customException.VerificationFailure as error:
	print constants.color_codes.FAIL + "An error occurred: " + error.message + constants.color_codes.ENDC
except customException.MultiFaceException as error:
	print constants.color_codes.WARNING + error.message + "\nRecognition will run." + constants.color_codes.ENDC
	print constants.LINE + constants.color_codes.OKBLUE + "Splitting Image Colours" + constants.color_codes.ENDC + constants.LINE
	recognition_preprocess.run()

	
