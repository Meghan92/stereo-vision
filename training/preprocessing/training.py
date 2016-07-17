import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import preprocessing.detection.crop as crop
import preprocessing.detection.detect as detect
import preprocessing.convolution.verification as verify
import preprocessing.detection.config as detect_config
import capture.output as capture_output
import constants
import clean


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
				for image in folder_path:
					name = image.split(".jpg")[0]
					print folder_path
					environment_settings = detect_config.Ubuntu(os.path.join(folder_path, image),  prefix + name + "_" + str(count) + ".jpg")
					detect.run(environment_settings)
		print("- Cropping faces")
		crop.run(constants.RESOLUTION)
		print("- Convolving")
		verify.run()
	except ReferenceError as refError:
		print("A reference occurred: " + refError.message)

