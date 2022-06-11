str = 3
fin = 18
mas = [0] * (fin+1)
mas[str] = 1
for i in range(str+1, fin+1):
    if i == fin-1:
        mas[i] += mas[i-2]
    else:
        mas[i] += mas[i-1]
        if i - 2 > str:
            mas[i] += mas[i-2]
print(mas)