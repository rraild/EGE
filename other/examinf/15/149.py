for a in range(1, 1000):
    ok = True
    for x in range(1, 10000):
        f = ((x & 103 == 0) and (x & 94 != 0)) <= (x & a != 0)
        if not f:
            ok = False
            break
    if ok:
        print(a)
        break
