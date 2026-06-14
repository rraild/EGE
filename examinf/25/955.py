def dels(d):
    dls = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)

    return sorted(set(dls))


for n in range(1000, 10_000):
    s = sum(dels(n))
    if s % 100 == 23:
        print(n, s)
