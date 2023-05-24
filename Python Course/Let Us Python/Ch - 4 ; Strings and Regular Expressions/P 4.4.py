s1 = 'Bring It On'
s2 = '   Flanked by spaces on either side      '
s3 = 'C:\\Users\\Kanetkar\\Documents'

# Bring It On
print(s1.upper())
print(s1.lower())
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())
print(s1.find('I'))
print(s1.find('O'))
print(s1.replace('It', 'Him'))

# Flanked by spaces on either side
print(s2.lstrip())
print(s2.rstrip())

# s3
print(s3.split('\\'))
print(s3.partition('\\'))
