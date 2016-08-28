import cmd, sys, os, ui
from shutil import copyfile
from shutil import rmtree
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
import file
import train as recognition_train
import predict as recognition_predict

system = 1
while (system != 4):
	try:
		ui.header("Stereo Vision - Menu")
		system = int(raw_input("[1] Log in \n[2] Register\n[3] Training\n[4] Quit\n\nPlease select an option (#): "))
		if system == 4:
			ui.header("Goodbye")
		elif system < 3:
			ui.header("Capturing Face")
			input = raw_input("Press any key when ready: ")
			webcam.capture()
			ui.header("Saving capture")
			
		if system == 1:	
			input = raw_input("Please enter your student number (e.g. 11019532): ")
			ui.header("Preprocessing")
			preprocess.run()
			byte_array = process.run(0)
			ui.header("Verifying")
			verified = predict.run(byte_array)
			if verified > 0:
				ui.success("Your image has been verified.")
				ui.header("Running Recognition")
				recognition_preprocess.run()
				recognized = recognition_predict.run(input)
				if recognized == 1:
					ui.success("Face verified, welcome %s" % (input))
				else:
					ui.fail("Face does not match. Please try again.")
			else:
				raise customException.VerificationFailure("Face not verified, your image has been logged.")
		elif system == 2:
			input = int(raw_input("Please enter your student number (e.g. 11019532): "))
			recognition_path = os.path.join(os.path.dirname(__file__), "recognition")
			database_path = os.path.join(recognition_path, "database")
			new_path = os.path.join(database_path, str(input))
			os.makedirs(new_path)
			verification_path = os.path.join(os.path.dirname(__file__), "verification")
			capture_path = os.path.join(verification_path, "capture")
			output_path = os.path.join(capture_path, "output")
			for images in os.listdir(output_path):
				copyfile(os.path.join(output_path, images), os.path.join(new_path, images))
			ui.success("Your images have been captured")
			ui.header("Preprocessing")
			try:
				preprocess.run()
				byte_array = process.run(0)
				ui.header("Verifying")
				verified = predict.run(byte_array)
				if verified > 0:
					ui.header("Storing Detected Face")
					recognition_preprocess.run()
					file.clean_and_move(str(input))
					ui.success("You have been registered.")
				else:
					raise customException.VerificationFailure("Your image was not verified by the system.")
			except (customException.DetectionFailure, customException.VerificationFailure) as error:
				ui.warning(error.message + "\nRemoving folder '%s'" % (input))	
				rmtree(new_path)
			
		elif system == 3:
			input = int(raw_input("There are two training algorithms: \n[1] Verification\n[2] Recognition\nSelect an algorithm (#): "))
			if input == 1:
				ui.header("Verification Training")
				input = raw_input("Would you like to save your images to the verification database for training? (y/n): ").lower()	
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
					
				input = raw_input("Would you like to run the training network for the verification database? (y/n): ").lower()
				if input == "y":
					ui.header("Preprocessing, please wait patiently...")
					preprocess_training.run()
					process.run(1)
					ui.header("Training")
					train.run()
			elif input == 2:
				ui.header("Recognition Training")
				input = raw_input("Would you like to run the training network for the recognition database? (y/n): ").lower()
				if input == "y":
					ui.header("Training, please wait patiently...")
					recognition_train.run()
				
	except (customException.VerificationFailure, customException.DetectionFailure) as error:
		ui.fail("Failed Verification: " + error.message)
	except customException.MultiFaceException as error:
		ui.warning(error.message)
		ui.header("Running Recognition")			
	except ValueError as error:
		ui.fail("An error occurred trying to convert values.\nPlease ensure that you do not include alpha characters in your student number")
	except OSError as error:
		ui.fail("A file system error occurred.\nIf you are registering, make sure your file does not already exist on the system.")


	
