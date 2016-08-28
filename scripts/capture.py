import webcam
import display
import display.webcam


def run():
	is_captured = 0
	while is_captured == 0:
		is_captured = webcam.capture()

		if is_captured:
			display.webcam.success()
		else:
			is_captured = 0
			display.webcam.fail()