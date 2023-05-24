lst = ['desert', 'dessert', 'to', 'too', 'lose','loose']
s = 'Mumbai'

for i, ele in enumerate(lst):
    if i > 3:
        break
    else:
        print(i, ele, s[i])
