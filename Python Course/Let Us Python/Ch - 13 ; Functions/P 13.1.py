def cal_sum_prod(a, b, c):
    sum = a + b + c
    product = a  * b * c
    return sum, product

a = int(input('Enter number: '))
b = int(input('Enter number: '))
c = int(input('Enter number: '))
s, p = cal_sum_prod(a, b, c)
print(s, p)