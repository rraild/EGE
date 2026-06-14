for A in range(1, 10000):
    t = True

    for x in range(1, 10000):
        if not (
            ((x & 46 == 0) or (x & 18 == 0))
            <= ((x & 115 != 0) <= (x & A == 0))
        ):
            t = False
            break

    if t:
        print(A)
