def factorial(x):
	product = 1;
	i = 1;
	while(i <= x):
		product = product*i;
		i = i + 1;
	return product;

def ele(X, Y):
	return factorial(X)/(factorial(X-Y)*factorial(Y));

n = int(input());
i = 0;
while i <= n:
	print (" "*(n-i), end = "");
	j = 0;
	while j <= i:
		print (int(ele(i, j)), end=" ");
		j = j+1;
	i = i+1;
	print ();
 
