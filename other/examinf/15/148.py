res = []

for a in range(1, 1000):
    t = True
    for x in range(1, 10000):
        f = (x % 10 == 0 and x % 26 == 0 and x >= 300) <= (a <= x)

        if not f:
            t = False
            break

    if t:
        res.append(a)

print(max(res))
