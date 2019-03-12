f=open("file.txt","r")
t=f.readlines()
k=len(t)
avg=0
for i in range(k):
	t[i]=t[i].split('\t')
	avg += float(t[i][3][:-1]);
	print(t[i][0], t[i][1], t[i][2], t[i][3], sep="\t", end="");
print(avg/k);
	
