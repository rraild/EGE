for A in range(1, 10000):
    t = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not (((y + 5 * x != 31) or (A > x - 2)) and (A < y + 37)):
                t = False
                break

    if t:
        print(A)
        break
