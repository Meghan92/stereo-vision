import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import preprocessing.detection.crop as crop
import preprocessing.detection.detect as detect
import preprocessing.convolution.verification as verify
import preprocessing.detection.config as detect_config
import capture.output as capture_output
import common.constants as constants
import clean
import detection.checker as checker


def run():
	try:	
		parent_folder = os.path.join(os.path.dirname(__file__), '..')
		capture_folder = os.path.join(parent_folder, "capture")
		database_folder = os.path.join(capture_folder, "database")
		databases = capture_output.get_database_paths()
		count = 0
		prefix = ""
		for database in databases:
			if "spoof" in database:
				prefix = "spoof"
			else:
				prefix = ""
			database_path = os.path.join(database_folder, database)
			print "- Detecting faces in %s set" % (database)
			for folder_number in os.listdir(database_path):
				folder_path = os.path.join(database_path, folder_number)
				count += 1
				for image in os.listdir(folder_path):
					name = image.split(".")[0]
					old_path = os.path.join(os.path.join("database", database), folder_number)
					old_image = os.path.join(old_path, image)					
					environment_settings = detect_config.Environment(detect_config.Ubuntu(old_image,  prefix + name + "_" + str(count) + ".jpg"))
					detect.run(environment_settings)
		checker.clean_duplicates()
		print("- Cropping faces")
		crop.run(constants.RESOLUTION)
		print("- Convolving")
		verify.run()
	except ReferenceError as refError:
		print("A reference occurred: " + refError.message)

