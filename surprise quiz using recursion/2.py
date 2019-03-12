def gcd(a, b):
	if b%a == 0:
		return a
	else:
		return gcd(b%a, a)
a = int(input())
b = int(input())
print(gcd(a, b))
