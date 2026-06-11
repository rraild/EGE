res = []

for A in range(0, 100000):
    t = True
    for x in range(1, 16385):
        if 8 * x >= 131072:
            break

        y = 65536 - 4 * x

        f = (131072 != 2 * y + 8 * x) or (A > 2 * x and A > y)

        if not f:
            t = False
            break

    if t:
        res.append(A)
        print(A)
        break
