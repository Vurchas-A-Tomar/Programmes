lst = ['Shubha', 'Nisha', 'Sudha', ('Suresh',), ('Rajesh',), 'Radha']

b = 0
g = 0

for x in lst:
    if isinstance(x, tuple):
        b += 1
    else:
        g += 1

print(f'Number of Boys : {b}')
print(f'Number of Girls : {g}')
print()