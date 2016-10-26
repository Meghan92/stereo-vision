import webbrowser
import display.types as ui


def success(student_number):

	ui.success("Welcome {}!".format(student_number))
	print "Opening Web Browser"
	webbrowser.open_new("https://img.buzzfeed.com/buzzfeed-static/static/2015-04/14/11/enhanced/webdr13/enhanced-mid-13335-1429024178-2.jpg")
	print "Hit enter to close the application"
	raw_input()
	

def fail(student_number):
	#TODO: audit this login failure
	ui.fail("Invalid login for {}".format(student_number))
	print "Opening Web Browser"
	webbrowser.open_new("https://socialmediaweek.org/wp-content/blogs.dir/1/files/social-fail-940x492.jpg")
	print "Hit enter to close the application"
	raw_input()
	
