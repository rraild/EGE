def Del(n, m):
    return n % m == 0


for a in range(100, 0, -1):
    t = True
    for x in range(1, 10000):
        f = (Del(x, 24) or Del(x, 36)) <= Del(x, a)
        if not f:
            t = False
            break
    if t:
        print(a)
        break
