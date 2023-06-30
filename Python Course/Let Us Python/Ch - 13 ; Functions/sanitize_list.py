def sanitize_list(lst):
    l = set(lst)
    return list(l)

l = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 5, 6, 7, 8]
print(sanitize_list(l))