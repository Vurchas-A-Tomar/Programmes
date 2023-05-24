x1, y1 = input('Enter x1, y1: ').split(',')
x2, y2 = input('Enter x2, y2: ').split(',')
x3, y3 = input('Enter x2, y3: ').split(',')

if x1 == x2 == x3 or y1 == y2 == y3:
    print('Straight Line')
else:
    print('Not Straight Line')
