x = 1
y = 1
z = 1
n = 2
i = 0
List1 = []
List = [0, 0 ,0]
while List[0] <= x:
	List[1] = 0
	while List[1] <= y:
		List[2] = 0
		while List[2] <= z:
			if sum(List) != n:
				List1.append(List[:])
			List[2] += 1
		List[1] += 1
	List[0] += 1
print(List1)
