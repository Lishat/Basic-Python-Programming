D1 = list(map(int, input().split('/')))
D2 = list(map(int, input().split('/')))
D3 = [0,0,0]
flag = 0
if D2[2] > D1[2]:
	flag = 1
elif D2[2] == D1[2] and D2[1] > D1[1]:
	flag = 1
elif D2[2] == D1[2] and D2[1] == D1[1]:
	if D2[0] > D1[0]:
		flag = 1
if flag == 1:
	D1, D2 = D2, D1
			
if D1[0] >= 1 and D1[0] <= 30:
	if D1[1] >= 1 and D1[1] <= 12:
		if D1[2] >= 1:
			if D2[0] >= 1 and D2[0] <= 30:
				if D2[1] >= 1 and D2[1] <= 12:
					if D2[2] >= 1:
						D3[0] = D1[0] - D2[0]
						D3[1] = D1[1] - D2[1]
						D3[2] = D1[2] - D2[2]
						while D3[0] < 0 or D3[1] < 0:
							if D3[0] < 0:
								D3[0] += 30
								D3[1] -= 1
							elif D3[1] < 0:
								D3[1] += 12
								D3[2] -= 1
						print("%d/%d/%d\n%d/%d/%d\n%d,%d,%d" %(D1[0], D1[1], D1[2], D2[0], D2[1], D2[2], D3[2], D3[1], D3[0]))
if D1[2] < 0 or D2[2] < 1:
	print("Invalid")
else:
	if D1[1] < 1 or D2[1] < 1:
		print("Invalid")
	elif D1[1] > 12 or D2[1] > 12:
		print("Invalid")
	elif D1[0] > 30 or D2[0] > 30:
		print("Invalid")
