for N in range(1, 10000):
    i = bin(N)[2:]
    if N % 3 == 0:
        i = i + i[-3:]
    else:
        r = (N % 3) * 3
        i = i + bin(r)[2:]
    R = int(i, 2)
    if R >= 200:
        print(N)
        break
