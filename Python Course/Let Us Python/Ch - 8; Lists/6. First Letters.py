lst_wrd = []
lst_l = []

for x in range(1, 11):
    wrd = input('Enter a word: ')
    lst_wrd.append(wrd)
print(f'Words - {lst_wrd}')

for n in lst_wrd:
    a = n[0]
    lst_l.append(a)

print(f'Letters - {lst_l}')
