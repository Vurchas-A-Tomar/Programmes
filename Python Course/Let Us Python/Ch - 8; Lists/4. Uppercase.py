lst = []
lst_upper = []

for x in range(1, 6):
    wrd = input('Enter a word: ')
    lst.append(wrd)

print(f'Normal List - {lst}')

i = 0
while True:
    lst_upper.append(lst[i].upper())

    i += 1

    if i == len(lst):
        break

print(f'Uppercase List - {lst_upper}')
