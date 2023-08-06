def all_sum(number):
    if number != 0:
        digit = number % 10
        number = int(number / 10)
        sum = digit + all_sum(number)
    else:
        return 0
    return sum

print(all_sum(620))