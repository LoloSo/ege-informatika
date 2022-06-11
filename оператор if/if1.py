num = input()
n = [int(digit) for digit in num]
num = int(num)
mult = 1
while (num != 0):
    mult = mult * (num % 10)
    num = num // 10

if 100 > sum(n) > 9:
    print('YES')
else:
    print('NO')
if mult > 99:
    print('YES')
else:
    print('NO')
