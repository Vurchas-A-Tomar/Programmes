students = {
    'Vurchas' : {
        'Maths' : 100,
        'Science' : 100,
        'English' : 100
    },
    'Avik' : {
        'Maths' : 80,
        'Science' : 70,
        'English' : 20
    }
}

for key in students:
    avg_marks = 0
    for subject in students[key].values():
        avg_marks += subject
    students[key] = avg_marks

for x in students:
    print(f'Total Marks of {x} : {students[x]}')
    print(f'Average Marks of {x} : {round(students[x] / 3,  2)}')
    print('')