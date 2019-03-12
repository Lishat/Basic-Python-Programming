a = int(input())
b = int(input())
ans = 1
while a != 0:
	ans = a
	a = b%a
	b = ans
print(ans)
