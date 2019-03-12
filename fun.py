def f(x = 6, y = 3):
	return x/y

def printf(*hello):
	for i in hello:
		print(i)
print(f(9), f(8, 2), f(y = 2, x = 6))
printf(1, 2, 3, 4, 'hello', 'getlost')
