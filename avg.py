n = int(input())
List = []
for i in range(n):
	List1 = []
	List1=input().split()
	List.append(List1)
name = input()
for i in range(n):
	if name == List[i][0]:
		print((float(List[i][1])+float(List[i][2])+float(List[i][3]))/3)
