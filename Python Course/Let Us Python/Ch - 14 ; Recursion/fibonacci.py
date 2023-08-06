# Fibonacci Sequence

y = 1
z = 1
i = 3

print(y)
print(z)

for x in range(1, 1000000):
    y += z
    print(f'{i}  {y}')
    i += 1

    z += y
    print(f'{i}  {z}')
    i += 1