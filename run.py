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
				if not verified or not recognized:
					complete.fail(student_number)
				option = enums.menu.QUIT
			except errors.InvalidLogin as error:
				option, student_number = menu.login_invalid(error.message, error.student_number)
		elif option == enums.menu.REGISTER:
			registered, student_number = register.start(student_number)
			if registered:
				viewport.show()
				capture.frontal()
				capture.save(student_number, enums.capture.FRONTAL)
				register.compare()
				option = enums.menu.QUIT
				complete.success(student_number)
			else:
				option = menu.register_fail()
		elif option == enums.menu.SETTINGS:
			training_type = menu.training()
			if training_type == enums.train.VERIFICATION:
				verification.train(constants.RESOLUTION)
			elif training_type == enums.train.RECOGNITION:
				recognition.train()
			else:
				option = enums.menu.RETURN
		else:
			option = enums.menu.RETURN
		
