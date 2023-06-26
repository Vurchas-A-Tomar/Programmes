students = {
    1 : 'Vurchas',
    2 : 'Avik',
    3 : 'Adi'
}

while True:
    rollno = int(input('Enter Roll Number: '))
    names = students.get(rollno, 'Student')
    print(f'Congratulations {names}')