def Del(n, m):
    return n % m == 0


for A in range(1, 10000):
    t = True
    for x in range(1, 10000):
        if not (
            ((Del(x, 12) or Del(x, 36)) <= Del(x, A)) and (A**2 - A - 90 < 0)
        ):
            t = False
            break

    if t:
        print(A)
