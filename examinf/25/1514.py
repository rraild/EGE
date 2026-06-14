def dels(d):
    dls = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)

    return sorted(set(dls))


res = []
for n in range(1_533_878, 0, -1):
    divs = [x for x in dels(n) if x != n and x != 1]

    if divs:
        f = max(divs) - min(divs)

    else:
        f = 0

    if f > 5000 and f % 1235 == 0:
        res.append((n, f))
        if len(res) == 5:
            break

print(res)
for n, f in sorted(res):
    print(n, f)
