def dels(d):
    dls = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)

    return sorted(set(dls))


def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False

    return d > 1


ct = 0
for n in range(4_444_000 - 1, -1, -1):
    dls = [d for d in dels(n) if d != n and is_prime(d)]

    if dls:
        s = sum(dls)
    else:
        continue

    if s > 2_000_000 and s % 123 == 0:
        ct += 1
        print(n, s)

    if ct == 5:
        break
