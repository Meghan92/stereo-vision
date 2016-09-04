import scripts.capture as capture
import scripts.viewport as viewport
import scripts.menu as menu
import scripts.common.enum as enums


option = menu.start()
if option == enums.menu.LOGIN:
	viewport.show()
	capture.frontal()
