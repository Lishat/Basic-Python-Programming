def fibonacci(n):
	if n == 0 or n == 1:
		return n
	elif(A[n] != -1):
		return A[n]	
	else:
		A[n] = fibonacci(n - 1)+fibonacci(n - 2)
		return A[n]
n = int(input())
A = []
for i in range(n+1):
	A.append(-1)

for i in range(n+1):
	print(fibonacci(i), end=" ")
print()
