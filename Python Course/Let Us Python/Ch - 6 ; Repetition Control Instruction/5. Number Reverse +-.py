num = int(input('Enter a Number: '))
reversed_num = 0

while num != 0:
    current_digit = num % 10

    reversed_num *= 10
    reversed_num += current_digit

    num = num // 10

print(f'Reversed Number: {reversed_num}')
