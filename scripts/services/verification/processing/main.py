import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#import lbp
import fpb
import output
import format


#print(line + "\nrunning local binary pattern\n" + line)
#lbp.run()
def run(resolution, train=1):
	print("Running face pattern byte")
	fpb.run(resolution)
	return format.run(train)
