import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#import lbp
import fpb
import output
import format
import common.constants as constants


#print(line + "\nrunning local binary pattern\n" + line)
#lbp.run()
def run(train=1):
	print(constants.LINE + constants.color_codes.OKBLUE + "Running face pattern byte" + constants.color_codes.ENDC + constants.LINE)
	fpb.run(constants.RESOLUTION)
	return format.run(train)
