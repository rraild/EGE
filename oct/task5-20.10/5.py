for N in range(1, 10000):
    s = str(bin(N))[2:]

    p1 = sum(int(d) for d in s) % 2

    R = 4 * N + 2 * p1
    if R > 630:
        print(N)
        break
