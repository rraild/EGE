def Del(n, m):
    return n % m == 0


for A in range(1, 10000):
    t = True
    for x in range(1, 10000):
        if not ((Del(x, 15) <= ((not (Del(x, A))) <= (not (Del(x, 3)))))):
            t = False
            break

    if t:
        print(A)
