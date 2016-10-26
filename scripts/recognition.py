import display.types as ui
import services.recognition.preprocess as preprocess
import services.recognition.predict as predict


def run(username):
	ui.header("Running Recognition")
	preprocess.run()
	recognized = predict.run(username)
	return recognized == 1
