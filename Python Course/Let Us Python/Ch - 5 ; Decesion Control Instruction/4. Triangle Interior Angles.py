a1 = int(input('Enter 1st angle: '))
a2 = int(input('Enter 2nd angle: '))
a3 = int(input('Enter 3rd angle: '))

if a1 == 0 or a2 == 0 or a3 == 0:
    print('None of the Value should be 0 degrees')
elif a1 + a2 + a3 == 180:
    print('Valid Triangle')
else:
    print('Invalid Triangle')
