import services.verification.preprocessing.training as preprocess_training
import services.verification.preprocessing.test as preprocess_test
import services.verification.processing.main as process
import services.verification.ann.main as neural_network
import services.verification.capture.output as output
import services.verification.ann.predict as predict
import display.types as ui
import viewport
import capture
import webcam


def train(resolution):
	ui.header("Verification Training")
	input = raw_input("Would you like capture an image for training? (y/n): ").lower()	
	if input == "y":
		viewport.show()
		capture.frontal()
		paths = output.get_database_paths()
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
		preprocess_training.run(resolution)
		process.run(resolution, 1)
		ui.header("Training")
		neural_network.run()
		
	
def run(resolution):
	try:
		ui.header("Preprocessing")
		preprocess_test.run(resolution)
		byte_array = process.run(resolution, 0)
		ui.header("Verifying")
		verified = predict.run(byte_array) > 0	
		if verified:
			ui.success("Your image has been verified")
		else:
			ui.fail("Your image was not verified")
		return verified
	except ValueError as error:
		ui.fail(error.message)
		return False
