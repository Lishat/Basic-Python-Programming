List = input().split();
b = int(List[0]);
for i in List:
	if b < int(i):
		b = int(i);
print (b);
