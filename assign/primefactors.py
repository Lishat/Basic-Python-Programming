p = n = int(input());i = 2
while i <= p - 1:
	if n % i == 0:
		n /= i;
		print (i, end=" ");
	else:
		i += 1
print()
