def dels(d):
    dls = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)

    return sorted(set(dls))


for n in range(699_999, 0, -1):
    divs = [x for x in dels(n) if x != n and x != 1]

    if divs:
        sm = sum(divs) // len(divs)

    else:
        sm = 0

    if sm % 1000 == 313:
        print(n, sm)
