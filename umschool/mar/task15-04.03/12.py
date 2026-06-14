def Del(n, m):
    return n % m == 0


D = list(range(30, 45 + 1))
for A in range(1, 1000):
    t = True
    for x in range(1, 1000):
        f = ((not (Del(x, 6))) and x not in [45, 50, 55, 60]) <= (
            (abs(x - 15) <= 5) <= (x in D)
        ) or (x & A != 0)
        if not f:
            t = False
            break

    if t:
        print(A)
        break
