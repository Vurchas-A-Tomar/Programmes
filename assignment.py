# Coffee Bill
# Vurchas Aditya Tomar IX - B

print(f'''
Menu : 
1. Espresso      $ 5
2. Cappuccino    $ 2.5
3. Latte         $ 7
4. Caffe Mocha   $ 4
      
# If no coffe is ordered, please type none
''')

coffee = ['espresso', 'cappuccino', 'latte', 'caffe mocha', 'none']
coffee_num = [0, 0, 0, 0, 0]
coffee_price = [5, 2.5, 7, 4, 0]

i = 1
while True:
    inp = input(f'Person {i} : ')
    coffee_inp = inp.split(', ')

    for x in coffee_inp:
        for num,y in enumerate(coffee):
            if x.lower() == y:
                coffee_num[num] += 1
                break
        else:
            print('Please enter a valid option')
            i -= 1
    
    print('')
    i += 1
    if i == 6:
        break

total = 0
for num,a in enumerate(coffee_num):
    if num == 4:
        break

    total += float(coffee_num[num] * coffee_price[num])

    print(f'{a} {coffee[num]} : ${float(coffee_num[num] * coffee_price[num])}')

print(f'Total : ${total}')
print('------------------------------------------------')

