names = {'Anil', 'Anda', 'Bholu', 'Anaconda'}
name_a = []
name_b = []


for item in names:
    if item[0].lower() == 'a':
        print(item[0].lower())
        name_a.append(item)
    elif item[0].lower() == 'b':
        print(item[0].lower())
        name_b.append(item)
    else:
        pass

name_a = set(name_a)
name_b = set(name_b)

print(f'Names starting with A are {name_a}')
print(f'Names starting with B are {name_b}')