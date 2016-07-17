import training.capture.webcam as webcam
import training.capture.output as capture_output
import cmd
import training.constants as constants
import training.preprocessing.training as preprocess_training
import training.preprocessing.main as preprocess


print constants.LINE + "Capturing Face" + constants.LINE
input = raw_input("Press any key when ready: ")
#webcam.capture()
print constants.LINE + "Saving capture" + constants.LINE
input = raw_input("Would you like to save your images to the database for training? (y/n): ").lower()
if input == "y":
	train()
else:
	test()
	
	
def test():
	print constants.LINE + "Preprocessing" + constants.LINE
	preprocess.run()
	
	
def train():
	paths = capture_output.get_database_paths()
	count = 0
	print "The following databases are: "
	for path in paths:
		count += 1
		print "[" + str(count) + "] " + path
	input = raw_input("Which database number would you like to save to? (#): ")
	database_num = int(input) - 1
	filename = paths[database_num]
	input = raw_input("Your picture will be saved to the \"%s\" database. Are you sure? (y/n): " % (filename))
	number = webcam.save_to_database(filename)
	print "Your image has been saved to the \"%s\" database, which now has %s records" % (filename, number)
	input = raw_input("Would you like to run the training network? (y/n): ")
	if input == "y":
		print constants.LINE + "Preprocessing, please wait patiently..." + constants.LINE
		preprocess_training.run()