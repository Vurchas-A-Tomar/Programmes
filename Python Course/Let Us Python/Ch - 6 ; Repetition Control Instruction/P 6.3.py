a = 1
while a <= 3:
    b = 1
    while b <= 3:
        c = 1
        while c <= 3:
            if a == b or b == c or a == c:
                c += 1
                continue
            else:
                print(a, b, c)
            c += 1
        b += 1
    a += 1
