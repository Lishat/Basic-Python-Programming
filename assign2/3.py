List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([(x, y, x*y) for x in List for y in List if x*y in List])
