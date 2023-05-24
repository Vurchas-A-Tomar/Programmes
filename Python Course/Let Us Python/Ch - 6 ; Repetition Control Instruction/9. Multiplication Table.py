num = int(input('Enter a Number: '))

print(f'---------- Table of {num} ----------')
print('')

for n in range(1, 11):
    print(f'{num} x {n} = {num * n}')
