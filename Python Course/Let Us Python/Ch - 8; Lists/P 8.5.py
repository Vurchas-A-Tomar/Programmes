import random

a = []
i = 1

while i < 16:
    numbers = random.randint(10, 100)
    a.append(numbers)
    i += 1

print(a)

for numbers in a:
    if 20 < numbers < 50:
        a.remove(numbers)

print(a)
