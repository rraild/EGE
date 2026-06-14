res = []

for A in range(0, 1000):
    t = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x - 3 * y < A) or (y > 400) or (x > 56)
            if not f:
                t = False
                break
        if not t:
            break

    if t:
        res.append(A)
        print(A)
        break
