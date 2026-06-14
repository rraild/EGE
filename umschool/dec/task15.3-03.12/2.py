for A in range(1, 10000):
    t = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((15 * x - y + 40 != 0) or (A < x) or (A < y)):
                t = False
                break

        if not (t):
            break

    if t:
        print(A)
