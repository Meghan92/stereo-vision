import webbrowser


def success(student_number):
	webbrowser.open_new("https://img.buzzfeed.com/buzzfeed-static/static/2015-04/14/11/enhanced/webdr13/enhanced-mid-13335-1429024178-2.jpg")
	raw_input("Welcome {} ! Opening Web Browser. Hit enter to close the application".format(student_number))
	

def fail(student_number):
	#TODO: audit this login failure
	webbrowser.open_new("https://socialmediaweek.org/wp-content/blogs.dir/1/files/social-fail-940x492.jpg")
	raw_input("Invalid login for {}. Opening Web Browser. Hit enter to close the application".format(student_number))
	
