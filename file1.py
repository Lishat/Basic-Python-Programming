"""f=open("file.txt","r")
t=f.readlines()
k=len(t)
avg=0
for i in range(k):
	t[i]=t[i][:-1].split('\t')
	avg += float(t[i][3])
	for j in range(len(t[i])):
		print(t[i][j],end="\t")
		if j==k:
			print("")
print(avg/k)"""
k=1
k1=id(k)
print(accessValue(k1))	
