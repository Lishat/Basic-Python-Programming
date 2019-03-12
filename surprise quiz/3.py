n = int(input())
a = 0
b = 1
c = 0
for i in range(n - 1):
	c = a
	a = b
	b += c
if(n == 0 or n == 1):
	print(n)
else:
	print(b)
