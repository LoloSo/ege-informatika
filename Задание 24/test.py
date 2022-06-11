lst = [10,2,3,4,5,6,7,8,9,10]
print(lst.index(max(lst)))
print(lst.index(min(lst)))
maxl = lst.index(max(lst))
minl = lst.index(min(lst))
lst[maxl], lst[minl] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]
# lst[0], lst[1] = lst[1], lst[0]
print(lst, sep='\n')