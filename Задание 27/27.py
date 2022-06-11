with open('27-6a.txt') as file:
    col = 0
    n = int(file.readline())
    lst = list(map(int, file.readlines()))
for i in range(n-5):
    for j in range(i+5, n):
        if (lst[i] + lst[j]) % 2 != 0 and lst[i] * lst[j] % 13 == 0:
            col += 1
print(col)