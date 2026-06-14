def f(a, b, c):
    sds = sorted([a, b, c])
    return sds[0] ** 2 + sds[1] ** 2 == sds[2] ** 2


c = 0
for A in range(10, 100):
    if A % 2 != 0:
        continue

    ok = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            left = f(16, y, A) or f(x, y, A)
            right = x + A < 85
            if left != right:
                ok = False
                break
        if not ok:
            break

    if ok:
        c += 1

print(c)
