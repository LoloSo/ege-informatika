
lst = list()
for number in range(2476, 7857+1):
    if number % 2 == 0 and number % 8 != 0:
        if (number//100%10) <= 7:
            lst.append(number)
print(len(lst), (min(lst)+max(lst))//2)
