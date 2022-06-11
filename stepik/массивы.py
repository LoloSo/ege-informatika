import math
def mina(a, b):
    return "%.5f" % (a ** b / math.factorial(b))
print(mina(int(input()), int(input())))