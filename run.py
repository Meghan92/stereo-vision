import scripts.capture as capture
import scripts.viewport as viewport
import scripts.menu as menu
import scripts.common.enum as enums
import scripts.register as register
import scripts.login as login
import scripts.algorithm as algorithm
import scripts.complete as complete
import scripts.common.exceptions as errors
import scripts.common.constants as constants


option = None
student_number = None
recognized = False
verified = False
registered = False
verification = algorithm.verification()
recognition = algorithm.recognition()
while option != enums.menu.QUIT:
	option = menu.start()
	while option != enums.menu.RETURN and option != enums.menu.QUIT:
		if option == enums.menu.LOGIN:
			try:
				student_number = login.start()
				viewport.show()
				capture.frontal() 
				verified = verification.run(constants.RESOLUTION)
				if verified:
					recognized = recognition.run(student_number)
					if recognized:
						complete.success(student_number)
				if not (verified and recognized):
					complete.fail(student_number)
				option = enums.menu.QUIT
			except errors.InvalidLogin as error:
				option, student_number = menu.login_invalid(error.message, error.student_number)
		elif option == enums.menu.REGISTER:
			try:
				studentModel = register.start(student_number)
				viewport.show()
				capture.frontal()
				verified = verification.run(constants.RESOLUTION)
				if verified:
					registered = register.create(studentModel)
					if registered:
						capture.save(studentModel.student_id, enums.capture.FRONTAL)			
						option = enums.menu.QUIT
						complete.success(studentModel.student_id)
				if not (verified and registered):
					option = menu.register_fail()
			except ValueError as error:
				raw_input("Hit enter to continue")	
		elif option == enums.menu.SETTINGS:
			settings_type = menu.settings()
			if settings_type == enums.settings.TRAIN:
				training_type = menu.training()
				if training_type == enums.train.VERIFICATION:
					verification.train(constants.RESOLUTION)
				elif training_type == enums.train.RECOGNITION:
					recognition.train()
				else:
					option = enums.menu.RETURN
			elif settings_type == enums.settings.CAPTURE:
				capturing = True
				while capturing:
					filename = capture.training()
					if filename is not None:
						viewport.show()
						capture.frontal()
					else:
						option = enums.menu.SETTINGS
						capturing = False					
			else:
				option = enums.menu.RETURN
		else:
			option = enums.menu.RETURN
		
