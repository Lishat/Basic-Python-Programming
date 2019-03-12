n = int(input())
for i in range(1, 2*n+1, 2):
	print(("H"*i).center(2*n-1, " "))
for i in range(n+1):
	print(" "*(n//2), "H"*n, " "*(n-2)*n, "H"*n, sep = "")
for i in range(n//2 + 1):
	print(" "*(n//2 - 1), "H"*n*n)
for i in range(n+1):
	print(" "*(n//2), "H"*n, " "*(n-2)*n, "H"*n, sep = "")
j = -1
for i in range(2*n-1, 0, -2):
	print(" "*(n*(n-1)+j), "H"*i, sep = " ")
	j += 1
