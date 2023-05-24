import random
p = int(input('How many numbers do you want: '))
q = int(input('How large should the numbers be: '))

l_n = []

for x in range(1, p + 1):
    l_n.append(random.randint(1, q))
print(f'Your List of Numbers : {l_n}')
print()

l_n.sort()
b = len(l_n)
median = b / 2
add = 0

# Mean --------------------------------------
for a in l_n:
    add = add + a
mean = add / len(l_n)
print(f'Mean: {mean}')

# Median ------------------------------------
while len(l_n) > 0:
    if len(l_n) % 2:
        median = int(median)
        print(f'Median : {l_n[median]}')
    else:
        median2 = median - 1
        median = int(median)
        median2 = int(median2)

        med = (l_n[median2] + l_n[median]) / 2
        print(f'Median : {med}')
    break

# Mode ---------------------------------------
for y in l_n:
    print(f'{y} {l_n.count(y)}')
