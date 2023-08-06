def factorize(n, i):
    if i <= n:
        if n % i == 0:
            print(i, end='')
            n = n // i
        else:
            i += 1
    factorize(n, i)

factorize(4, 2)