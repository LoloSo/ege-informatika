n = 4 ** 1014 + 2 ** 1012 - 7
k2 = 0
while n > 0:
    if n % 2 == 1:
        k2 += 1
    n //= 2
print(k2)