i = 2;
while(i <= 100):
	j = 2;
	while(j**2 <= i):
		if not(i%j):
			break;
		j = j + 1;
	if(j > i/j):
		print(i, 'is prime');
	i += 1;
