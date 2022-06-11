lst = list()
lstk = 0
lstki = 0
for number in range(101000000, 102000000+1):
    for divider in range(1, int(number**0.5) + 1):
        if number % divider == 0:
            lst.append(divider)
            lst.append(number//divider)
    lst = list(set(lst))
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lstk += 1
    if lstk == 3:
        print(number)
    lstk = 0
    lst.clear()