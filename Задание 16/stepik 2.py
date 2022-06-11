c = 0
def F(n,m):

    if n<m:

        n,m = m,n

    if n != m:

        return F(n-m,m)

    else:

        return n
for x in range(1, 100):
    for y in range(1, 100):

        if F(x,y) > 15 and x != y:
           print(x, y, F(x,y))
