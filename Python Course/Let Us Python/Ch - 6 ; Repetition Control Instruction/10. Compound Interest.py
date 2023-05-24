for x in range(1, 11):
    p = int(input('Enter p: '))
    r = int(input('Enter r: '))
    n = int(input('Enter n: '))
    q = int(input('Enter q: '))

    a = p * (1 + r/q) ** n * q

    print(a)
