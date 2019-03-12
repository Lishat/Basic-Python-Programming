fp = open("getlost.txt","r")
List = fp.readlines()
List1 = []
List2 = []
for i in range(len(List)):
	if List[i][4] == '0':
		List1.append(List[i])
	else:
		List2.append(List[i])
f1 = open("CSE.txt", "w")
f2 = open("ECE.txt", "w")
f1.writelines(List1)
f2.writelines(List2)
fp.close()
f1.close()
f2.close()
