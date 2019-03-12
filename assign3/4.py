n = int(input())
List1 = []
List2 = []
for i in range(n):
	string = input().split(',')
	string[1] = int(string[1])
	List1.append(string[0])
	List2.append(string[1])
sumi = sum(List2)
for i in range(n):
	if List2[i] >= sumi/n:
		print(List1[i])

