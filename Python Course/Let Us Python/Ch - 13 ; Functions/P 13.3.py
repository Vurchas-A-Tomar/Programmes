def convert(s1):
    items = [s for s in s1.split('-')]
    items.sort()
    s2 = '-'.join(items)
    return s2

print(convert('here-come-the-dots-followed-by-the-dashes'))