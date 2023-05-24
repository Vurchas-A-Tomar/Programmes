print('---------- LICENCE COMPANY POLICY ----------')

ms = input('Enter Martial Status: ')
s = input('Enter Sex: ')
age = int(input('Enter Age: '))

if (ms == 'm') or (ms == 'u' and s == 'm' and age > 30) or (ms == 'u' and s == 'f' and age > 25):
    print('Insured')
else:
    print('Not Insured')
