for n in range(1, 301):
    i = 1

    if n == 1:
        print(f'1')
        continue

    while i < n:
        for x in range(1, 301):
            while x < n:
                if i != 1 or i != n:
                    if i * x == n:
                        continue
                    else:
                        i += 1
                    print(n)
