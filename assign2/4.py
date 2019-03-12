string=input()
print([string[:i][j:] for i in range(len(string)+1) for j in range (0, i)])
