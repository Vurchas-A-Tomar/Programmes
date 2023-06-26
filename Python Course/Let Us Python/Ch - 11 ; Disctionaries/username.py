username = {
    'vurchas' : 0,
    'adi' : 1,
    'mummy' : 2,
    'papa' : 3,
    'bua' : 4,
    'avik' : 5,
    'amma' : 6,
    'avika' : 7,
    'era' : 8,
    'masi' : 9
}

user = input('Enter username : ')

for key in username:
    if user == key:
        print(f'Password of {user} is {username[key]}')
    else:
        continue

