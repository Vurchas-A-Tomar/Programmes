grocery_price = {
    'potato' : 40,
    'tomato' : 50,
    'milk' : 45
}

grocery_quantity = {
    'potato' : 3,
    'tomato' : 2,
    'milk' : 4
}

grocery = {}

for key_price in grocery_price:
    for  key_quantity in grocery_quantity:
        if key_price == key_quantity:
            grocery[key_price] = grocery_price[key_price] * grocery_quantity[key_quantity]
        else:
            continue

total = 0
for amount in grocery:
    print(f'{amount} : {grocery[amount]}')
    total += grocery[amount]
print('')

print(f'Total Amount : {total}')