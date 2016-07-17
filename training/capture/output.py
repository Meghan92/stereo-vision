import os


file_path = os.path.dirname(os.path.realpath(__file__))


def get_database_paths():
	databases_location = os.path.join(file_path, "database")
	return os.listdir(databases_location)