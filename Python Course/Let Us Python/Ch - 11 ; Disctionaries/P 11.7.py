d = {
    'Anuj' : {'salary' : 10000, 'age' : 20, 'height': 6},
    'Aditya' : {'salary' : 6000, 'age' : 26, 'height': 5.6},
    'Rahul' : {'salary' : 7000, 'age' : 26, 'height': 5.9}
}
list_salary = [] 

for x in d.values():
    list_salary.append(x['salary'])

print(f'Maximum salary : {max(list_salary)}')
print(f'Minimum salary : {min(list_salary)}')