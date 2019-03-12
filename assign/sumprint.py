def index(elmt, ind):
	for i in range(ind + 1, len(string)):
		if string[i] == elmt:
			return i
	else:
		return -1
			
			
string=list(map(int, input().split()))
i = 0
j = 0
l = 0
m = 0
a = []
while True:
	if index(6, m) != -1 and index(7,l) != -1:
		if index(7, l) > index(6, m):
			i = index(6, m)
			j = index(7, l)
			for k in range(len(string)):
				if k < i:
					a.append(string[k])
				elif k > j:
					a.append(string[k])
			string = a
			a = []
		elif index(7, l) < index(6, m):
			l = index(7, l)
	else:
		break;
print(sum(string))		
