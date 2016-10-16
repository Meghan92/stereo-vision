import scripts.capture as capture
import scripts.viewport as viewport
import scripts.menu as menu
import scripts.common.enum as enums
import scripts.register as register
import scripts.login as login
import scripts.algorithm as algorithm
import scripts.complete as complete


option = None
while option != enums.menu.QUIT:
	option = menu.start()
	while option != enums.menu.RETURN and option != enums.menu.QUIT:
		if option == enums.menu.LOGIN:
			exists = login.start()
			if exists:
				viewport.show()
				capture.frontal()
				if algorithm.verify_capture():
					if algorithm.verify_student():
						complete.success()
					else:
						complete.fail()
				else:
					complete.fail()
				option = enums.menu.QUIT
			else:
				option = menu.login_invalid()
		if option == enums.menu.REGISTER:
			registered = register.start()
			if registered:
				capture.frontal()
				register.compare()
			else:
				option = menu.register_fail()
		if option == enums.menu.SETTINGS:
			training_type = menu.training()
			if training_type == enums.train.VERIFICATION:
				print "Call training algorithm"
			if training_type == enums.train.RECOGNITION:
				print "Call training algorithm"
		if option != enums.menu.QUIT
			option = enums.menu.RETURN
		
