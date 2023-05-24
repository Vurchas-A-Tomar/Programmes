start, end, step = input('Enter start, end and step values: ').split()

start = int(start)
end = int(end)
step = int(step)

for n in range(start, end, step):
    print(f'{n}, {n ** 2}, {n ** 3}')
