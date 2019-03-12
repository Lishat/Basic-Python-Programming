"""def NodeCreate(value, next):
	return [value, next]
def NodeValue(n):
	return n[0]
def NodeNext(n):
	return n[1]
def NodeSetValue(n, value):
	n[0] = value
def NodeSetNext(n, next):
	n[1] = next"""
count = 0
first = []
first.append(int(input()))
first.append(None)
head = first
while(head[0] != 0):
	temp=[]
	head[1] = temp
	temp.append(int(input()))
	temp.append(None)
	head = temp;
head = first
while head[1][1] != None:
	head = head[1]
head[1] = None
head = first
while True:
	print(head[0], end = " ")
	if head[1] == None:
		break;
	head = head[1]
	
print()

print(first)

