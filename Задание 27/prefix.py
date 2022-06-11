F = open('27-Bdek.txt')
n = int(F.readline())

k = 30

left = [2 * 10**9] * k
right = [-1] * k

count = 0
summ = 0
maxsumm = 0
for i in range(n):
    num = int(F.readline())
    summ += num
    if num % 2 == 0 and num > 0:
        count += 1
    ost = count % k
    if left[ost] > summ:
        left[ost] = summ
    maxsumm = max(maxsumm, summ - left[ost])

print(maxsumm)