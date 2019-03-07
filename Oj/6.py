import sys
import string
p = raw_input().split();
for i in range(len(p)):
	sys.stdout.write(p[i][0:1].capitalize())
sys.stdout.flush();
print

