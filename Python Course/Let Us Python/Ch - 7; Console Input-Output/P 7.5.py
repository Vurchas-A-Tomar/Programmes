import math

for n in range(1, 11):
    s = round(math.sqrt(n), 3)
    c = round(math.pow(n, 1/3), 3)
    print(f'Square Root of n = {s}')
    print(f'Cube Root of n = {c}')