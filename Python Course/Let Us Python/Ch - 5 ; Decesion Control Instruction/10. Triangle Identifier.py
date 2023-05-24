s1 = int(input('Enter Side 1: '))
s2 = int(input('Enter Side 2: '))
s3 = int(input('Enter Side 3: '))

if (s1 == s2 and s1 and s2 != s3) or (s2 == s3 and s2 and s3 != s1) or (s1 == s3 and s1 and s3 != s2):
    print('Isosceles Triangle')
elif s1 == s2 == s3:
    print('Equilateral Triangle')
elif s1 ** 2 == s2 ** 2 + s3 ** 2 or s2 ** 2 == s1 ** 2 + s3 ** 2 or s3 ** 2 == s1 ** 2 + s2 ** 2:
    print('Right-Angled Triangle')
else:
    print('Scalene Triangle')
