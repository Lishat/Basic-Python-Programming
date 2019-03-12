g = lambda n,k: n**k
n = int(input())
k = int(input())
for i in range(k):
	print(g(n,i+1), end=" ")
print()
