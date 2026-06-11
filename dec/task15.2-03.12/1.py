for A in range(1, 10000):
    t = True

    for x in range(1, 10000):
        if not ((x & 15 != 0) or (x & 34 == 0) or (x & A != 0)):
            t = False
            break

    if t:
        print(A)
        break
