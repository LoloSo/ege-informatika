def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    if a == 1:
        return True
    else:
        return False

for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        if ((gcd(x,360) <= (gcd(x,A))) and ((gcd(x,A)) <= (gcd(x,240)))) is False:
            flag = False
            break
    if flag:
        print(A)
        break