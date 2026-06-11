res = []
for A in range(0, 10000):
    t = True

    for x in range(0, 1000):
        for y in range(0, 1000):
            if not (
                ((x > 15) <= (x * y + 10 * x >= A))
                and ((y * x + y > A) <= (y >= 1))
            ):
                t = False
                break

        if not (t):
            break

    if t:
        print(A)
        res.append(A)

print(len(res))
