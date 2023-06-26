marks = {
    'Subu' : {
        'Maths' : 88,
        'Eng' : 60,
        'SSt' : 95
    },
    'Amol' : {
        'Maths' : 78,
        'Eng' : 68,
        'SSt' : 89
    },
    'Raka' : {
        'Maths' : 56,
        'Eng' : 66,
        'SSt' : 77
    }
}

# Printing English Marks for Amol
for k, v in marks['Amol'].items():
    if k == 'Eng':
        print(v)

# Marks obtained by Raka in Maths to 77
marks1 = {
    'Maths' : 77
}
marks['Raka'].update(marks1)
