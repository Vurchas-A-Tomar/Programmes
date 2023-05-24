qty = int(input('Enter value of quantity: '))
price = float(input('Enter value of Price: '))

if qty > 1000:
    dis = 10
else:
    dis = 0

totexp = qty * price - qty * price * dis / 100
print(f'Total expenses - Rs.{totexp}')
