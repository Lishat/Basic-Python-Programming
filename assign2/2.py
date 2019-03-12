import math
n = int(input())
m = int(input())
for i in range(n+1, m):
	flag = 1
	if i == 0 or i == 1:
		flag = 0
	elif i == 2:
		flag = 1
	else:
		for j in range(2, math.floor(math.sqrt(i))+1):
			if i%j == 0:
				flag = 0;
				break;
	if flag == 1:
		print(i, end= " ")
print()
