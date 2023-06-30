def create_list(list1, list2):
    lst = [x for x in list1 for y in list2 if x == y]
    return lst

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(create_list(list1, list2))
