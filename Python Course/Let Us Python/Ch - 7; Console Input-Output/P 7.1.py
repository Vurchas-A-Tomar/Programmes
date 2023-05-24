r, l, b = input('Enter radius, length and breadth: ').split()

c = 2 * 3.14 * int(r)
a = int(l) * int(b)
p = 2 * (int(l) + int(b))

print(f'Circumference = {c}')
print(f'Area = {a}')
print(f'Perimeter = {p}')
