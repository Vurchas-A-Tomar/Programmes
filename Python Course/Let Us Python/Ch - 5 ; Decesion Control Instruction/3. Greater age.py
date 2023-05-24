r = int(input("Enter Ram's Age: "))
s = int(input("Enter Shyam's Age: "))
a = int(input("Enter Ajay's Age: "))

if r > s and r > a:
    print('Ram is the Oldest')
elif s > r and s > a:
    print('Shyam is the Oldest')
else:
    print('Ajay is the Oldest')

