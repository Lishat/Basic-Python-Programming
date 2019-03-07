string = raw_input();
i = 0;
add = 0;
multiplier = 1;
while(i != len(string)):
		if string[i].isalpha():
			if i == len(string) - 1 or string[i+1].isalpha():  
				multiplier = 1;
				if string[i] == 'C' or string[i] == 'c':
					add=add+12.011*multiplier;
				elif string[i] == 'H' or string[i] == 'h':
					add=add+1.0079*multiplier;
				elif string[i] == 'O' or string[i] == 'o':
					add=add+15.9994*multiplier;
				i = i + 1;
			else:
				j = i + 1;
				while(j <= len(string) - 1):
					if string[j].isalpha():
						b = j;
						multiplier = int(string[i+1:b])
						if string[i] == 'C' or string[i] == 'c':
							add=add+12.011*multiplier;
						elif string[i] == 'H' or string[i] == 'h':
							add=add+1.0079*multiplier;
						elif string[i] == 'O' or string[i] == 'o':
							add=add+15.9994*multiplier;
						i = b;
						break;
					elif j == len(string) - 1:
						b = j+1;
						multiplier = int(string[i+1:b])
						if string[i] == 'C' or string[i] == 'c':
							add=add+12.011*multiplier;
						elif string[i] == 'H' or string[i] == 'h':
							add=add+1.0079*multiplier;
						elif string[i] == 'O' or string[i] == 'o':
							add=add+15.9994*multiplier;
						i = b;
						break;
					j = j + 1;
print add
