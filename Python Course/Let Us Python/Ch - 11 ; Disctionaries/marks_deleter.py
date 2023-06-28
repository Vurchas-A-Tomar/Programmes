marks = {
    'Vurchas' : 100,
    'Adi' : 20,
    'Avik' : 70,
    'Avika' : 50,
    'Era' : 95
}

reverse = dict(reversed(marks.items()))

for k, v in reverse.items():
    print(f'{k} : {v}')

print(reverse)