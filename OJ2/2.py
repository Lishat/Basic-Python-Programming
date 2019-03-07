string = input();
flag = 0;
if string.count('@') == 1 and string.count('.') >= 1:
		if string.find('@') != 0 and string.find('@') != len(string)-1:
			if string[string.find('@') + 1] != '.' and string[string.find('@') - 1] != '.':
				flag = 1;

for i in range(1, len(string) - 1):
	if string[i] == '.' and string[i+1] != '.':
		if string[i-1] == '.':
			flag = 0;

if string[-1] == '.':
	flag = 0;
		
if flag == 0:
	print("invalid");
elif flag == 1:
	print("valid");
