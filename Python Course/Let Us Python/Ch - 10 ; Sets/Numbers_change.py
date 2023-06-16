import random

num = set()
x = True

while x == True:
    if len(num) < 10:
        y = random.randint(15, 45)
        num.add(y)
    else:
        x = False
print(num)

z = 1
for ele in num:
    if ele < 30:
        z += 1

num2 = set()
for ele2 in num:
    if ele2 > 35:
        num2.add(ele2)
num -= num2

print(f'Number of elements smaller than 30 are {z}')
print(num)