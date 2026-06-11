n, m = 1, 1000
for A in range(n, m):
    t = True
    for x in range(n, m):
        for y in range(n, m):
            f = (y + 2 * x < A) or (x > 30) or (y > 20)
            if not f:
                t = False
                break
        if not f:
            break

    if t:
        print(A)
        break
