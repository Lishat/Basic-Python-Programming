List = [1, 3, 2, 5, 6, 4]
for j in range(len(List)-2, -1, -1):
	for i in range(0, j+1):
		if List[i] > List[i+1]:
			List[i], List[i+1] = List[i+1], List[i]
print(List)
