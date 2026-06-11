for A in range(1, 10000):
    t = True

    for x in range(1, 10000):
        if not (
            ((x & 35 == 0) and (x & 61 != 0))
            <= ((x & 10 != 0) <= (x & A != 0))
        ):
            t = False
            break

    if t:
        print(A)
        break
