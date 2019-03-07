import math;
string = input()
x = 0;
y = 0;
for i in string:
	if i == 'A':
		y += 1;
	elif i == 'B':
		y -= 1;
	elif i == 'C':
		x -= 1;
	elif i == 'D':
		x += 1;
m = (math.sqrt(x*x + y*y) * 10)
if m%1 > 0.5:
	m = m+1;
print("%d, %d, %0.1f" %(x, y, m/10));
