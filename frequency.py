string = input().split();
List = [];
List1 = [];
for i in range(len(string)):
	List.append(1);
	List1.append(1);
i = 0;
while i <= len(string) - 1:
	j = 0;
	while j < i:
		if string[i] == string[j]:
			List[j] = List[j] + 1;
			List1[i] = 0;
		j += 1;
	i += 1;
for i in range(len(string)):
	if List1[i] != 0:	
		print(string[i], List[i])
