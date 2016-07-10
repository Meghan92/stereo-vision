import processing.lbp as lbp
import processing.fpb as fpb
import processing.output as output
import processing.format as format

line = "---------------------------------------------"

print(line + "\nrunning face pattern byte\n" + line)
fpb.run(16)
print(line + "\nbytes have been stored in output/bytes.text\n" + line)
print(line + "\nformatting variables for input to the neural network\n" + line)
inputs = format.run()
