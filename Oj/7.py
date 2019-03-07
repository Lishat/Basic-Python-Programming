string=raw_input();
add = 0;
for j in string:
	if ord(j) >= 97 and ord(j) <= 122:
		add=add+ord(j) - 96;
	elif ord(j) >= 65 and ord(j) <= 90:
		add = add + ord(j) - 64;
print add
