sentence = input('> ')
dict = {}

for alphabet in sentence:
    dict[alphabet] = 0

for key in dict:
    for alph in sentence:
        if alph == key:
            dict[key] += 1
            

for key in dict:
    print(key + ' ' + str(dict[key]) + ' ')

