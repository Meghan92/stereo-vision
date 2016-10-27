import display.types as ui
import services.recognition.preprocess as preprocess
import services.recognition.predict as predict
import services.recognition.train as train


def run(username):
	ui.header("Running Recognition")
	preprocess.run()
	return predict.run(username)
	
	
def train():
	ui.header("Recognition Training")
	input = raw_input("Would you like to run the training network for the recognition database? (y/n): ").lower()
	if input == "y":
		ui.header("Training, please wait patiently...")
		train.run()
	
