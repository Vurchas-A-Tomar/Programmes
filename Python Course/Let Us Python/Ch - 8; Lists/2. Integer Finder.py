import random

lst = []

for x in range(1, 21):
    lst.append(random.randint(1, 20))

num = int(input('Enter a number between 1 and 20: '))
print(f'Your Number {num} occurs {lst.count(num)} times in the list {lst}.')
