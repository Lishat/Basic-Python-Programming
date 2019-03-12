string=input()
count = 0
for i in string:
	if i.isupper():
		count += ord(i) - 64
	elif i.islower():
		count += ord(i) - 96
print(count)
