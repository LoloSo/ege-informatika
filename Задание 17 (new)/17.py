with open('17 (1).txt') as file:
    mas = list(map(int, file.readlines()))
del17 = 0
kol = 0
pmax = 0
for i in range(len(mas)):
    if mas[i] % 171 == 0:
        del17 = max(del17, mas[i])
for i in range(len(mas)-1):
    if (mas[i] < del17 or mas[i+1] < del17) and (mas[i] % 2 == 0 or mas[i+1] % 2 == 0):
        kol += 1
        pmax = max(pmax, mas[i] + mas[i+1])
print(kol, pmax)