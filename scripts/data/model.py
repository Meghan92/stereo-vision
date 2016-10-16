class Student():
	def __init__(self, _student_id, _first_name, _last_name):
		self.student_id = _student_id
		self.first_name = _first_name
		self.last_name = _last_name
		
		
class Image():
	def __init__(self, _student_id, _image_type, _left_image, _right_image):
		self.student_id = _student_id
		self.image_type = _image_type
		self.left_image = _left_image
		self.right_image = _right_image
		

class CompoundResponse():
	def __init__(self, success, message):
		self.success = success
		self.message = message
	
