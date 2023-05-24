import random
lst = []

for x in range(1, 21):
    lst.append(random.randint(1, 20))
print(lst)

for n in lst:
    for z in lst:
        if z == n:
            lst.remove(z)
print(lst)
