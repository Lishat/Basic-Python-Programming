n = int(input())
List = list(map(int,input().split()))
List.sort()
i = len(List) - 2;
while i >= 0:
	if List[i] < List[-1]:
		print(List[i])
		break
	i -= 1
