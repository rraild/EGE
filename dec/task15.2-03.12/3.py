for A in range(1, 10000):
    t = True

    for x in range(1, 10000):
        if not ((x & 45 != 0) <= ((x & 23 == 0) <= (x & A != 0))):
            t = False
            break

    if t:
        print(A)
        break
