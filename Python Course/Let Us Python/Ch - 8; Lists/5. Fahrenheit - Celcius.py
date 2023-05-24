lst_f = []
lst_c = []

for x in range(1, 6):
    f = int(input('Enter temperature in Fahrenheit: '))
    lst_f.append(f)
print(f'Temperature in Fahrenheit: {lst_f}')

for n in lst_f:
    c = round((n - 32) * 5/9, 2)
    lst_c.append(c)

print(f'Temperature in Celsius: {lst_c}')
