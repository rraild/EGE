for A in range(-100, 1000):
    t = True
    for x in range(1, 100):
        for y in range(1, 100):
            f = (x + 4 * y != 32) or ((A > x) and (A > y))
            if not f:
                t = False
                break
        if not t:
            break
    if t:
        print(A)
        break
