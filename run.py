import scripts.capture as capture
import scripts.viewport as viewport
import scripts.menu as menu
import scripts.common.enum as enums
import scripts.register as register


option = menu.start()
if option == enums.menu.LOGIN:
	viewport.show()
	capture.frontal()
if option == enums.menu.REGISTER:
	register.start()
