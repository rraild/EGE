for A in range(1, 10000):
    t = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((3 * y - x < A) or (x >= 35) or (y >= 51)):
                t = False
                break

        if not (t):
            break

    if t:
        print(A)
        break
