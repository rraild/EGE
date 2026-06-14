for A in range(0, 1000):
    t = True
    for x in range(0, 100):
        for y in range(0, 100):
            f = (x**2 + y**2 > 1024 - x) or (y < -2 * x + A)
            if not f:
                t = False
                break
        if not t:
            break
    if t:
        print(A)
        break
