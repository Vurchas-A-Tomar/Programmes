for n in range(1, 501):
    reversed_num = 0
    print(n)
    while n != 0:
        current_digit = n % 10

        reversed_num *= 10
        reversed_num += current_digit

        n = n // 10

        print(n)
