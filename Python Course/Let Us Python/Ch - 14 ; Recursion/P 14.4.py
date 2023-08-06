def fibonacci(old, now, terms):
    if terms <= 4000:
        new = old + now
        print(f'{new} ', end='\t')
        terms += 1
        fibonacci(now, new, terms)


print(1, end='\t')
print(1, end='\t')

fibonacci(1, 1, 1)