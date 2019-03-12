import math
string = input()
x1 = int(string[1:string.find(',')])
y1 = int(string[string.find(',')+1:string.find(')')])
string1 = input()
x2 = int(string1[1:string.find(',')])
y2 = int(string1[string.find(',')+1:string.find(')')])
p = math.degrees(math.atan((y2-y1)/(x2-x1)))
if (x1 != x2):
	if((p*10)%1 > 5):
		p *= 10
		p += 1
		p /= 10
	print("%0.1f" %p)
elif((y2 - y1) > 0):
	print(90.0)
else:
	print(-90.0)
	
