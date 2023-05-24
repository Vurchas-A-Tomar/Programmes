lst_even = [2, 4, 6, 8]

lst_odd = [1, 3, 5, 7, 9]
print(lst_odd)

lst = [1, 3, *lst_even, 7, 9]
print(lst)

print(sorted(lst))
