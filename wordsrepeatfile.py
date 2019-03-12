fp = open("file.py", "r")
fp1 = open("file1.txt", "w")
temp = "\n"
temp1 = " "
while temp != "":
	temp = fp.readline();
	temp2 = temp[:-1]+temp1+temp ;
	fp1.write(temp2);

