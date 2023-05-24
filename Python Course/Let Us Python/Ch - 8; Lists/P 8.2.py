lst_even = [2, 4, 6, 8, 10]
lst_odd = [1, 3, 5, 7, 9]

lst = lst_odd + lst_even
print(lst)

lst = [11, 17, 29] + lst
print(lst)

length = len(lst)
print(length)

lst[length-3:length] = [100, 200, 300]
print(lst)

lst[:] = []
print(lst)

del lst
