def dels(d):
    dls = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))


res = []
for n in range(1533878, 0, -1):
    d = dels(n)

    if len(d) < 2:
        f = 0
    else:
        f = max(d) - min(d)

    if f > 5000 and f % 1235 == 0:
        res.append([n, f])
        if len(res) == 5:
            break

for row in sorted(res):
    print(row[0], row[1])
