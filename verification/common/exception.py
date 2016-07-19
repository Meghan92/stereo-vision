class MultiFaceException(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return repr(self.message)
		

class VerificationFailure(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return repr(self.message)
		
		
class DetectionFailure(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return repr(self.message)
