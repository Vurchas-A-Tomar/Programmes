for n in range(1, 25):
    if n < 12:
        print(f'{n} AM')
    elif n == 12:
        print(f'{n} Noon')
    elif n < 24:
        print(f'{n} PM')
    else:
        print(f'{n} Midnight')
