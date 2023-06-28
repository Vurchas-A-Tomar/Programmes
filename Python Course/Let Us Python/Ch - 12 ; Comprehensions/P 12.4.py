lst = [(), (), (10), ('',)]
lst = [tpl for tpl in lst if tpl != ()]
print(lst)