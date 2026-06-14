for A in range(1, 10000):
    t = True

    for x in range(1, 10000):
        if not ((x & A != 0) <= ((x & 31 == 0) <= (x & 61 != 0))):
            t = False
            break

    if t:
        print(A)
        break
