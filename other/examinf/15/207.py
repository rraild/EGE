for A in range(1, 1000):
    t = False
    for x in range(0, 120):
        for y in range(0, 120):
            f = (4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < A)
            if f == 0:
                t = True
                break
        if t:
            break

    if t:
        print(A)
