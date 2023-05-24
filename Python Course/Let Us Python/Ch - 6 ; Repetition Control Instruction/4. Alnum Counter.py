s = input('Enter anything: ')

i = 1
a = 0
n = 0
sc = 0

while i < len(s):
    if s[i].isalpha():
        a += 1
    elif s[i].isdigit():
        n += 1
    else:
        sc += 1

    i += 1

print(f'''Number of Alphabets : {a}
Number of Digits : {n}
Number of Special Characters : {sc}
''')
