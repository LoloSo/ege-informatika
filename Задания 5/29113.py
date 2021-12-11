for N in range(128, 256):

    R = str(bin(N)).replace('0b', '')
    if len(R) % 8 != 0:
        b = 8 - (len(R) % 8)
        R = ('0' * b) + R

    w = ''
    for i in range(len(R)):
        if R[i] == '0':
            w += '1'
        else:
            w += '0'
    if 185 == N - int(w, 2):
        print(N)
        break