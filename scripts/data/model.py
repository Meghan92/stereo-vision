class Student():
	def __init__(self, _student_id, _first_name, _last_name):
		self.student_id = _student_id
		self.first_name = _first_name
		self.last_name = _last_name
		

class CompoundResponse():
	def __init__(self, success, message):
		self.success = success
		self.message = message
	
