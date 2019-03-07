string=input().split('/');
flag = 0;
Days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(len(string)):
	string[i] = int(string[i]);
if string[0] <= Days[string[1]]:
	flag = 1;
elif string[0] == 29 and (string[2])%4 == 0:
	if string[1] == 2:
		flag = 1;
sum1 = 0;
if flag == 1:
	if (string[2])%4 != 0 or string[1] <= 2:
		sum1 = sum(Days[:string[1]]) + string[0];
	elif string[1] >= 3:
		sum1 = sum(Days[:string[1]]) + string[0] + 1;
	print("valid,", sum1);
elif flag == 0:
	print("invalid, 0");
