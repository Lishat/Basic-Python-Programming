List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([(i,j,k) for i in List1 for j in List2 for k in List3 if i+j>k])
