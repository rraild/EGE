res = []

for A in range(-100, 100):
    t = True
    for x in range(-100, 100):
        for y in range(-100, 100):
            f = ((A < x) or (x**2 - 7 * x + 10 > 0)) and (
                (A >= y) or (y**2 + 7 * y + 12 > 0)
            )
            if not f:
                t = False
                break
        if not t:
            break

    if t:
        res.append(A)

print(len(res))
