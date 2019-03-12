a = 20
b = 20
if (a is b):
	print(a, "is equal to ", b)
elif (a is not b):
	print(a, "is not equal to", b)

if (id(a) == id(b)):
	print("id of ", a, "is equal to id of ", b)
elif (id(a) != id(b)):
	print("id of ", a, "is not equal to id of", b) 
