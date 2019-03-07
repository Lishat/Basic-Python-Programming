def syracuse(x):
	if x == 1:
		return 1
	elif x%2 == 0:
		if x != 2:
			print(int(x/2), ", ",sep="", end="" ); 
		else:
			print(1);
		return syracuse(int(x/2))
	elif x%2 != 0:
		print(3*x + 1, ", ",sep="", end="" );
		return syracuse(3*x + 1)

x = int(input());
if(x == 0 or x == 1):
	print(x);
else:
	print(x,", ",sep="", end="");
	syracuse(x);
