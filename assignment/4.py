def check(x, y):
	if id(string1) == id(string2):
		print id(string1);
	else:
		print id(string1), id(string2);
string1 = "HelloWorld"
string2 = "HelloWorld"
check(string1, string2);
string2="HelloSir"
check(string1, string2);
