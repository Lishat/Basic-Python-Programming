List = [12, 34, 324,3243,32423, 4564, 454,234, 23,423, 324]
print([x for x in List if x%2 == 0 ])
print([List[x] for x in range(len(List)) if x%2 == 0])
