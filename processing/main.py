import processing.lbp as lbp
import processing.fpb as fpb

line = "---------------------------------------------"

print(line + "\nrunning local binary pattern\n" + line)
lbp.run()
print(line + "\nrunning face pattern byte\n" + line)
fpb.run(16)
print(line + "\nbytes have been stored in output/bytes.text\n" + line)
