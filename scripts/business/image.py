import scripts.data.model as model
import scripts.data.repository.image as repository
import MySQLdb

def create(student_id, image_type_id, blob_array):
	image_description = repository.get_type(image_type_id)
	try:
		image = model.Image(student_id, image_type_id, blob_array[0], blob_array[1])	
		repository.insert(image)
		return model.CompoundResponse(True, "Saved {imt} Image for {sid}".format(imt=image_description, sid=student_id))
	except MySQLdb.IntegrityError as error:
		return model.CompoundResponse(False, "{imt} Image for {sid} already exists in the database".format(imt=image_description, sid=student_id))
		

def get(student_id, image_type_id):
	response = repository.get(student_id, image_type_id)
	if response:
		return model.Image(response[0], response[1], response[2], response[3])
	else:
		return None
