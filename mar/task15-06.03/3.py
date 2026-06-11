for A in range(0, 20000):
    t = True
    for x in range(1, 12001):
        y = 60000 - 5 * x
        if y > 0:
            f = (A > x) or (A > y)
            if not f:
                t = False
                break
    if t:
        print(A)
        break
