l = int(input('Enter the length of Rectangle: '))
b = int(input('Enter the breadth of Rectangle: '))

a = l * b
p = 2 * (l + b)

if a > p:
    print(f'Area of Rectangle: {a} is greater then Perimeter of Rectangle: {p}')
else:
    print(f'Perimeter of Rectangle: {p} is greater than Area of Triangle: {a}')
