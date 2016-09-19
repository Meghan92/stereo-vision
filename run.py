import scripts.capture as capture
import scripts.viewport as viewport
import scripts.menu as menu
import scripts.common.enum as enums
import scripts.register as register
import scripts.login as login


option = None
while option != enums.menu.QUIT:
	option = menu.start()
	while option != enums.menu.RETURN and option != enums.menu.QUIT:
		if option == enums.menu.LOGIN:
			exists = login.start()
			if exists:
				viewport.show()
				capture.frontal()
			else:
				option = menu.login_invalid()
		if option == enums.menu.REGISTER:
			registered = register.start()
			if registered:
				capture.frontal()
				register.compare()
			else:
				option = menu.register_fail()
		option = enums.menu.RETURN
		
