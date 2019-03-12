n = int(input())
List = []
List2 = []
for i in range(n):
	List1 = []
	List1.append(input())
	List1.append(float(input()))
	List.append(List1)
j = len(List) - 2
while j > 0:
	i = 0
	while i <= j:
		if List[i][1] >= List[i+1][1]:
			Temp = List[i]
			List[i] = List[i+1]
			List[i+1] = Temp
		i += 1
	j -= 1
j = 1
while j < len(List):
	if List[j][1] > List[0][1]:
		k = List[j][1]
		break;
	j += 1
j = 0;
while j < len(List):
	if k == List[j][1]:
		List2.append(List[j][0])
	j += 1
List2.sort()
for i in List2:
	print(i)
