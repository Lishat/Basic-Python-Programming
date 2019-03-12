def calculate(List1, List2):
	i = 0;
	while i <= len(List1) - 1:
		if i != len(List1) - 1 and List1[i+1] == '-':
			if List1[i] == 'A':
				List2.append(9);
			elif List1[i] == 'B':
				List2.append(7);
			elif List1[i] == 'C':
				List2.append(5);
			i += 2;
		else:
			if List1[i] == 'A':
				List2.append(10);
			elif List1[i] == 'B':
				List2.append(8);
			elif List1[i] == 'C':
				List2.append(6);
			elif List1[i] == 'D':
				List2.append(4);
			elif List1[i] == 'F':
				List2.append(2);
			i += 1;

def grade(List2, List3):
	sum1 = 0;
	i = 0;
	while i <= 4:
		sum1 = sum1 + List2[i]*int(List3[i]);
		i += 1;
	return sum1;

def credits(List3):
	List3=list(str(List3));
	for i in range(len(List3)):
		List3[i] = int(List3[i]);
	sum2 = sum(List3);
	return sum2;


List1 = input();	
List3 = input();
List2 = [];
calculate(List1, List2);
grade(List2, List3);
print(grade(List2, List3)/credits(List3));
