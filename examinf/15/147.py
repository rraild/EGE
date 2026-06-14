res = []

for a in range(1, 200):
    ok = True
    for x in range(1, 1000):
        f = (a + x < 123) <= ((x % 5 == 0) <= (x % 7 != 0))

        if not f:
            ok = False
            break

    if ok:
        res.append(a)

print(min(res))
