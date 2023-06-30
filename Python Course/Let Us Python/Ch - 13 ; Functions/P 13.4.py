def generate_list():
    lst = [(l, l**2, l**3) for l in range(1,11)]
    return lst

print(generate_list())
