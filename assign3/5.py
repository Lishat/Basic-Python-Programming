try:
	List = list(map(int, input().split(',')))
except:
	List = list(map(int, input().split(', ')))
n = len(List)
count = []
for i in range(max(List)+1):
	count.append(0)
	for j in range(len(List)):
		if(i == List[j]):
			count[i] += 1
for i in range(max(List)):
	print("%d,"%count[i], sep="", end="") 
print(count[i+1])
