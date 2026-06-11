for A in range(1, 10000):
    t = True

    for x in range(1, 10000):
        for y in range(1, 10000):
            if not (((y + 10 * x != 28) or (A > x - 1)) and (A < y + 50)):
                t = False
                break

    if t:
        print(A)
        break
