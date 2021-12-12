
for s in range(2, 5000, 2):
    n = 1
    C = s
    a = 0
    while s * n < 4096:
        s = s // 2
        n = n * 4
        a += 1
        if a > 100:
            break
        # print(s)

    if n == 1024:
        print(C)
        break

# s = int(input())
# n = 1
# while s * n < 4096:
#     s //= 2
#     n *= 4
#     # print(s * n)
# print(n)