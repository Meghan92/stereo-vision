import colour


def success():
	print colour.GREEN + "Image Captured Successfully" + colour.ENDC
	
	
def fail():
	print colour.RED + "Your image was not captured, please try again?" + colour.ENDC