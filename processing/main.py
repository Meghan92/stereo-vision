import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import lbp
import fpb
import output
import format

line = "---------------------------------------------"

print(line + "\nrunning local binary pattern\n" + line)
lbp.run()
print(line + "\nrunning face pattern byte\n" + line)
fpb.run(16)
print(line + "\nbytes have been stored in output/bytes.text\n" + line)
# print(line + "\ncleaning up processed files\n" + line)
# output.clean()
print(line + "\nformatting variables for input to the neural network\n" + line)
inputs = format.run()
