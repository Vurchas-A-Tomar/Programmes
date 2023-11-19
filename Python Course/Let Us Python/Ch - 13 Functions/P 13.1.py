def cal_sun_prod(a, b, c):
    s = a + b + c
    p = a * b * c
    return s, p

a = int(input('Enter num: '))
b = int(input('Enter num: '))
c = int(input('Enter num: '))
print((cal_sun_prod(a, b, c)))