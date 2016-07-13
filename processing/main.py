import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#import lbp
import fpb
import output
import format

line = "---------------------------------------------"

#print(line + "\nrunning local binary pattern\n" + line)
#lbp.run()
print(line + "\nrunning face pattern byte\n" + line)
fpb.run(16)
format.run()
