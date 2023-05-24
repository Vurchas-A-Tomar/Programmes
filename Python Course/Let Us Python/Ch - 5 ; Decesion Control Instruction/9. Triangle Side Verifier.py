s1 = int(input('Enter Side 1: '))
s2 = int(input('Enter Side 2: '))
s3 = int(input('Enter Side 3: '))

if s2 < s1 < s2 + s3 and s1 > s3:
    print('Valid Triangle Sides')
elif s1 < s2 < s1 + s3 and s3:
    print('Valid Triangle Sides')
elif s1 < s3 < s1 + s2 and s2:
    print('Valid Triangle Sides')
else:
    print('Invalid Triangle Sides')
