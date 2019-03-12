import string
string=input();
string = string.split('-');
string.sort();
i = 0
while i <= len(string) - 1:
	if ord(string[i][0]) >= 97 and ord(string[i][0]) <= 122:
		flag = i;
		break;
	i = i+1;
list1 = string[0:flag];
list2 = string[flag:len(string)];
for j in range(0, len(list2)):
	list2[j] = list2[j].capitalize();
list1=list1+list2;
list1.sort();
for k in range(0, len(list2)):
	for l in range(0, len(list1)):
		if list2[k] == list1[l]:
			list1[l] = list1[l].lower();
string1="-";
print (string1.join(list1));
