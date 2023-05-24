print('---------- COORDINATE PLACEMENT ----------')
print('')

x, y = input('Enter x, y: ').split(',')

x = int(x)
y = int(y)

if x == 0 and y == 0:
    print('In the Center')
elif x == 0:
    print('On Y Axis')
    if abs(x) == x and abs(y) == y:
        print('In Quadrant 1')
    elif abs(x) != x and abs(y) == y:
        print('In Quadrant 2')
    elif abs(x) != x and abs(y) != y:
        print('In Quadrant 3')
    else:
        print('In Quadrant 4')
elif y == 0:
    print('On X Axis')
    if abs(x) == x and abs(y) == y:
        print('In Quadrant 1')
    elif abs(x) != x and abs(y) == y:
        print('In Quadrant 2')
    elif abs(x) != x and abs(y) != y:
        print('In Quadrant 3')
    else:
        print('In Quadrant 4')
elif abs(x) == x and abs(y) == y:
    print('In Quadrant 1')
elif abs(x) != x and abs(y) == y:
    print('In Quadrant 2')
elif abs(x) != x and abs(y) != y:
    print('In Quadrant 3')
else:
    print('In Quadrant 4')
