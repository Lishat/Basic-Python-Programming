def hello(name, age):
	print("Name is:", name)
	print("Age is:", age)
hello("Subhadeep", 18)
hello(age=18, name="Subhadeep")

def getlost(name, age = 35):
	print("Name is:", name)
	print("Age is:", age)
getlost(name = "Subhadeep")
getlost("Subhadeep", 18)
