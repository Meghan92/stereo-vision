import types


loaded_displayed = 0
def start():
	types.header("Loading viewport, please wait...")


def loaded():
	global loaded_displayed
	if loaded_displayed == 0:
		print "Hit any key when ready to capture"
		loaded_displayed = 1
