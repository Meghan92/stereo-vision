class CaptureError():

	def __init__(self):
		self.message = "Your image could not be captured. Please view the error log for details"
		
		
class InvalidLogin():

	def __init__(self, _message, _student_number):
		self.message = _message;
		self.student_number = _student_number;

