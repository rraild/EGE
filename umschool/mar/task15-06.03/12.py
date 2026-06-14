def Del(n, m):
    return n % m == 0


for a in range(1000, 0, -1):
    t = True
    for x in range(1, 10000):
        f = (not Del(x, a)) <= (Del(x, 15) <= (not Del(x, 9)))
        if not f:
            t = False
            break
    if t:
        print(a)
        break
