lst = [1, 2, 3, 4, -45, -2, 33, -489, -3]

lstpos = [x for x in lst if abs(x) == x]
lstneg = [y for y in lst if abs(y) != y]

print(lstpos)
print(lstneg)